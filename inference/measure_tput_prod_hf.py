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

os.makedirs("results", exist_ok=True)
model_list = [
    "meta-llama/Llama-2-7b-hf",
    "meta-llama/Llama-2-13b-hf",
    "meta-llama/Llama-3.2-1B",
    "meta-llama/Llama-3.2-3B",
    "meta-llama/Llama-3.1-8B",
    "Qwen/Qwen2.5-0.5B",
    "Qwen/Qwen2.5-1.5B",
    "Qwen/Qwen2.5-3B",
    "Qwen/Qwen2.5-7B",
    "Qwen/Qwen2.5-14B",
    "google/gemma-2b",
    "google/gemma-7b",
    "google/gemma-2-2b",
    "google/gemma-2-9b",
    "mistralai/Mistral-7B-v0.1",
    "openbmb/MiniCPM-2B-sft-bf16-llama-format",
    "openbmb/MiniCPM-1B-sft-bf16"
]

gpu_id = 3
# num_prompts = 8
input_tokens = 128
output_tokens = 256
# A100: 1, 2, 4, 8
# A30: 1, 2, 4
num_prompts_list = [1, 2, 4, 8]

for num_prompts in num_prompts_list:
    for model_name in model_list:
        # 1. Load tokenizer and model
        if model_name == "openbmb/MiniCPM-1B-sft-bf16":
            tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                trust_remote_code=True
            )
            if tokenizer.pad_token is None:
                tokenizer.add_special_tokens({'pad_token': '[PAD]'})
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.bfloat16,
                trust_remote_code=True
            )
            model.to(f"cuda:{gpu_id}")
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            if tokenizer.pad_token is None:
                tokenizer.add_special_tokens({'pad_token': '[PAD]'})
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.bfloat16
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

            # Calculate metrics
            elapsed_time = end_time - start_time
            total_tokens = outputs.shape[1]  # total tokens in the output
            generated_tokens = (total_tokens - input_tokens) * outputs.shape[0]
            throughput = generated_tokens / elapsed_time

            print(generated_tokens)
            if generated_tokens == int(output_tokens * num_prompts):
                trial += 1
                with open(
                    f"results/prod_hf_tput_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}.txt",
                    'w'
                ) as f:
                    f.write(f"Throughput: {throughput:.2f} tokens/sec")
                print(f"prod_hf_tput_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}")
                print(f"Throughput: {throughput:.2f} tokens/sec")

            if trial >= 5:
                break

        del model
        del input_ids
        torch.cuda.empty_cache()


