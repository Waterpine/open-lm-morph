import json
import os
import random
import string
import time
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, LlamaConfig, AutoModelForCausalLM
from huggingface_hub import login


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

cache_directory = "/home/sbian"

gpu_id = 0
# num_prompts = 32
input_tokens = 128
output_tokens = 1
num_prompts_list = [1, 2, 4, 8, 16, 32, 64]
gpu_type = "A100"

model_name = "meta-llama/Llama-2-7b-hf"

with open(f"config_files/{gpu_type}_variants_1b.json", "r") as file:
    json_str = file.read()
    parameter_dict = json.loads(json_str)

os.makedirs(f"{gpu_type}_rebuttal/results_variants", exist_ok=True)

for num_prompts in num_prompts_list:
    for variant in parameter_dict.keys():
        # 1. Load tokenizer and model
        tokenizer = LlamaTokenizer.from_pretrained(model_name, cache_dir=cache_directory)
        config = LlamaConfig.from_pretrained(model_name, cache_dir=cache_directory)

        num_hidden_layers = parameter_dict[variant]["num_hidden_layers"]
        hidden_size = parameter_dict[variant]["hidden_size"]
        intermediate_size = 256 * ((int(2 * 4 * hidden_size / 3) + 256 - 1) // 256)
        config.num_hidden_layers = num_hidden_layers
        config.hidden_size = hidden_size
        config.intermediate_size = intermediate_size
        config.num_attention_heads = 16
        config.num_key_value_heads = 16
        config.head_dim = config.hidden_size // config.num_attention_heads
        config.torch_dtype = torch.bfloat16
        model = LlamaForCausalLM(
            config=config
        )
        checkpoint_path = "my_llama_checkpoint_variants_hf_1b"
        os.system(f"rm -rf {checkpoint_path}")
        model.save_pretrained(checkpoint_path)
        tokenizer.save_pretrained(checkpoint_path)

        model = AutoModelForCausalLM.from_pretrained(
            checkpoint_path,
            torch_dtype=torch.bfloat16
        )
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
                    f"{gpu_type}_rebuttal/results_variants/variants_hf_latency_hs_{hidden_size}_layers_{num_hidden_layers}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}.txt",
                    'w'
                ) as f:
                    f.write(f"Inference latency: {latency:.4f} seconds")
                print(f"variants_hf_hs_{hidden_size}_layers_{num_hidden_layers}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}")
                print(f"Inference latency: {latency:.4f} seconds")

            if trial >= 5:
                break

        del model
        del input_ids
        torch.cuda.empty_cache()


