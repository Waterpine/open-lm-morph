# llama-2-7b-hf
vocab_size = 32000
heads_dim = 128
n_heads = 32
hidden_size = heads_dim * n_heads
assert hidden_size % n_heads == 0
assert hidden_size / n_heads % 8 == 0
layers = 64
# swiglu
intermediate_size = 256 * ((int(2 * 4 * hidden_size / 3) + 256 - 1) // 256)
print(hidden_size)
print(intermediate_size)
total_num_param = (2 * vocab_size * hidden_size
                   + layers * (4 * hidden_size * hidden_size + 3 * intermediate_size * hidden_size + 2 * hidden_size)
                   + hidden_size)
print(total_num_param)
# print(2 * vocab_size * hidden_size / total_num_param)


# llama-3
# multiple_of = 256
# dim = 4096
# intermediate_size = 4 * dim
# intermediate_size = int(2 * intermediate_size / 3)
# # custom dim factor multiplier
# intermediate_size = multiple_of * ((intermediate_size + multiple_of - 1) // multiple_of)
# print(intermediate_size)
