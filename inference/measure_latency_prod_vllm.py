import os
import random
import string
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from huggingface_hub import login
from vllm import LLM, SamplingParams


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

model_list = [
    "meta-llama/Llama-2-7b-hf",
    "meta-llama/Llama-3.2-1B",
    "meta-llama/Llama-3.2-3B",
    "meta-llama/Llama-3.1-8B",
    "Qwen/Qwen2.5-0.5B",
    "Qwen/Qwen2.5-1.5B",
    "Qwen/Qwen2.5-3B",
    "Qwen/Qwen2.5-7B",
    "google/gemma-2b",
    "google/gemma-7b",
    "google/gemma-2-2b",
    "google/gemma-2-9b",
    "mistralai/Mistral-7B-v0.1",
    "openbmb/MiniCPM-2B-sft-bf16-llama-format",
    "openbmb/MiniCPM-1B-sft-bf16"
]

gpu_id = 1
# num_prompts = 1
input_tokens = 128
output_tokens = 256
# A100: 1, 2, 4, 8
# A30: 1, 2, 4
num_prompts_list = [1]
gpu_type = "A100"

if gpu_type == "A100":
    model_list.append("meta-llama/Llama-2-13b-hf")
    model_list.append("Qwen/Qwen2.5-14B")

os.environ["CUDA_VISIBLE_DEVICES"] = f"{gpu_id}"

os.makedirs(f"{gpu_type}/results_vllm", exist_ok=True)

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
            model = LLM(
                model=model_name,
                tensor_parallel_size=1,
                dtype=torch.bfloat16,
                max_model_len=2048,
                trust_remote_code=True
            )
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            if tokenizer.pad_token is None:
                tokenizer.add_special_tokens({'pad_token': '[PAD]'})
            model = LLM(
                model=model_name,
                tensor_parallel_size=1,
                dtype=torch.bfloat16,
                max_model_len=2048
            )
        sampling_params = SamplingParams(
            min_tokens=5,
            max_tokens=5,
            temperature=0.8,
            top_p=0.95
        )

        # 2. Warm-up
        warm_up_text = ["Hello, this is a warm-up."]
        _ = model.generate(warm_up_text, sampling_params)

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
            )
            decoded_texts = [tokenizer.decode(ids, skip_special_tokens=True) for ids in input_ids['input_ids']]

            sampling_params = SamplingParams(
                min_tokens=output_tokens,
                max_tokens=output_tokens,
                temperature=0.8,
                top_p=0.95
            )

            start_time = time.time()
            with torch.inference_mode():
                outputs = model.generate(
                    decoded_texts,
                    sampling_params
                )
            end_time = time.time()

            latency = end_time - start_time
            total_tokens_generated_per_prompt = 0
            for output in outputs:
                generated_text = output.outputs[0].token_ids
                total_tokens_generated_per_prompt = len(generated_text)
                print("total_tokens_generated_per_prompt:", total_tokens_generated_per_prompt)

            if total_tokens_generated_per_prompt == output_tokens:
                trial += 1
                with open(
                    f"{gpu_type}/results_vllm/prod_vllm_latency_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}.txt",
                    'w'
                ) as f:
                    f.write(f"Inference latency: {latency:.4f} seconds")
                print(f"prod_vllm_{model_name.split('/')[1]}_bs_{num_prompts}_InputTokens_{input_tokens}_OutputTokens_{output_tokens}_trial_{trial}")
                print(f"Inference latency: {latency:.4f} seconds")

            if trial >= 5:
                break

        del model
        del input_ids
        torch.cuda.empty_cache()


