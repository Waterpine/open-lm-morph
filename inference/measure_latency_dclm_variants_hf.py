import json
import os
import random
import string
import time
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, LlamaConfig, AutoModelForCausalLM, AutoTokenizer, AutoConfig
from huggingface_hub import login
from open_lm.hf import *


def generate_random_sentence(sentence_length=256):
    """
    Generates a sentence of `sentence_length` "words",
    each word is randomly chosen letters (2–8 letters).
    """
    words = []
    for _ in range(sentence_length):
        # Generate a random word between 2 and 8 characters
        rand_word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 8)))
        words.append(rand_word)
    return ' '.join(words)


login(token="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")

cache_directory = "/users/Master/checkpoint"

os.makedirs("results_dclm_variants", exist_ok=True)

gpu_id = 2
# num_prompts = 8
input_tokens = 128
output_tokens = 256
num_prompts_list = [1]
gpu_type = "A100"

model_name = "apple/DCLM-7B"

with open(f"config_files/{gpu_type}_dclm_variants_1b.json", "r") as file:
    json_str = file.read()
    parameter_dict = json.loads(json_str)

os.makedirs(f"{gpu_type}/results_dclm_variants", exist_ok=True)

for num_prompts in num_prompts_list:
    for variant in parameter_dict.keys():
        # 1. Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_directory)
        config = AutoConfig.from_pretrained(model_name, cache_dir=cache_directory)
        print(config)

        n_layers = parameter_dict[variant]["n_layers"]
        dim = parameter_dict[variant]["dim"]
        # intermediate_size = 256 * ((int(2 * 4 * dim / 3) + 256 - 1) // 256)
        config.n_layers = n_layers
        config.dim = dim
        # config.intermediate_size = intermediate_size
        config.n_heads = 32
        # config.head_dim = config.hidden_size // config.num_attention_heads
        config.torch_dtype = torch.bfloat16
        model = AutoModelForCausalLM.from_config(config)
        checkpoint_path = "my_dclm_checkpoint_variants_hf_1b"
        os.system(f"rm -rf {checkpoint_path}")
        model.save_pretrained(checkpoint_path)
        tokenizer.save_pretrained(checkpoint_path)

        model = AutoModelForCausalLM.from_pretrained(
            checkpoint_path,
            torch_dtype=torch.bfloat16
        )
        print(model)
        model.to(f"cuda:{gpu_id}")

        if tokenizer.pad_token is None:
            tokenizer.add_special_tokens({'pad_token': '[PAD]'})

        # 2. Warm-up
        warm_up_text = "Hello, this is a warm-up."
        warm_up_inputs = tokenizer(warm_up_text, return_tensors="pt").to(f"cuda:{gpu_id}")
        _ = model.generate(**warm_up_inputs, max_new_tokens=5)

        trial = 0
        # 3. Measure latency
        while True:
            prompt = [generate_random_sentence(input_tokens) for _ in range(num_prompts)]
            input_ids = tokenizer(
                prompt,
                max_length=input_tokens,
                padding='max_length',
                truncation=True,
                return_tensors="pt"
            ).to(f"cuda:{gpu_id}")

            start_time = time.time()
            with torch.inference_mode():
                outputs = model.generate(
                    **input_ids,
                    min_new_tokens=output_tokens,
                    max_new_tokens=output_tokens,
                    do_sample=True,
                    temperature=0.8,
                    top_p=0.95
                )
            end_time = time.time()

            latency = end_time - start_time
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            total_tokens_generated_per_prompt = outputs.shape[1] - input_tokens
            print(total_tokens_generated_per_prompt)

            if total_tokens_generated_per_prompt == output_tokens:
                trial += 1
                with open(
                    f"{gpu_type}/results_dclm_variants/variants_hf_latency_hs_{dim}_layers_{n_layers}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}.txt",
                    'w'
                ) as f:
                    f.write(f"Inference latency: {latency:.4f} seconds")
                print(f"variants_hf_hs_{dim}_layers_{n_layers}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}")
                print(f"Inference latency: {latency:.4f} seconds")

            if trial >= 5:
                break

        del model
        del input_ids
        torch.cuda.empty_cache()


