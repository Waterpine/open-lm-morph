import os
import random
import string
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
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


login(token="hf_key")

cache_directory = "/home/sbian"

model_list = [
    "facebook/opt-1.3b",
    "EleutherAI/pythia-1.4b-v0",
    "facebook/opt-iml-1.3b",
    "EleutherAI/gpt-neo-1.3B"
]

gpu_id = 0
# num_prompts = 8
input_tokens = 128
output_tokens = 1
# A100: 1, 2, 4, 8
# A30: 1, 2, 4
num_prompts_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]
gpu_type = "A100"

os.makedirs(f"{gpu_type}_rebuttal/results", exist_ok=True)

for num_prompts in num_prompts_list:
    for model_name in model_list:
        # 1. Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir=cache_directory,
        )
        if tokenizer.pad_token is None:
            tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            cache_dir=cache_directory,
        )
        model.to(f"cuda:{gpu_id}")

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
                    f"{gpu_type}_rebuttal/results/baseline_hf_latency_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}.txt",
                    'w'
                ) as f:
                    f.write(f"Inference latency: {latency:.4f} seconds")
                print(f"baseline_hf_latency_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}")
                print(f"Inference latency: {latency:.4f} seconds")

            if trial >= 5:
                break

        del model
        del input_ids
        torch.cuda.empty_cache()


