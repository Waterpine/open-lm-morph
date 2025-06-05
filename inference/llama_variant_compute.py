import torch

from transformers import (AutoModelForCausalLM,
                          LlamaForCausalLM, LlamaTokenizer, LlamaConfig, Qwen2ForCausalLM, Qwen2Tokenizer, Qwen2Config)

from huggingface_hub import login

login(token="hf_key")

cache_directory = "/users/Master/checkpoint"

# Load the model and tokenizer
model_name = "meta-llama/Llama-2-7b-hf"
tokenizer = LlamaTokenizer.from_pretrained(model_name, cache_dir=cache_directory)
config = LlamaConfig.from_pretrained(model_name, cache_dir=cache_directory)

hidden_size = 3584
intermediate_size = 256 * ((int(2 * 4 * hidden_size / 3) + 256 - 1) // 256)
config.num_hidden_layers = 42
config.hidden_size = hidden_size
config.intermediate_size = intermediate_size
config.num_attention_heads = 32
config.num_key_value_heads = 32
config.head_dim = config.hidden_size // config.num_key_value_heads

model = LlamaForCausalLM(config=config)

print(sum(p.numel() for p in model.parameters()))
for name, param in model.named_parameters():
    print(f"{name}: {param.numel()} parameters")
    print(param.size())

# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
#
# torch.save(model.state_dict(), "/users/Master/checkpoint/Llama-2-7b-hf.pt")
#
# checkpoint_path = "/users/Master/checkpoint/Llama-2-7b-hf.pt"
# ck_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))
#
# for key, value in ck_dict.items():
#     print(key, value.size())
