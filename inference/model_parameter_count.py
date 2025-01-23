import torch

from transformers import AutoModelForCausalLM, AutoTokenizer, GPT2PreTrainedModel, AutoModel, GPT2LMHeadModel, GemmaForCausalLM

from huggingface_hub import login

login(token="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")

# Load the model
model = AutoModelForCausalLM.from_pretrained("openbmb/MiniCPM-1B-sft-bf16")

print(sum(p.numel() for p in model.parameters()))
for name, param in model.named_parameters():
    print(f"{name}: {param.numel()} parameters")

