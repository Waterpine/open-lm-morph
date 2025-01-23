import os

directory = "results_hidden_size_vllm"

# List all entries in the directory
entries = os.listdir(directory)

# Filter out directories, keeping only files
files = [f for f in entries if os.path.isfile(os.path.join(directory, f))]

data_dict = {}
for file in files:
    split_ls = file.split("_")
    if directory == "results" or directory == "results_vllm":
        assert len(split_ls) == 12
        key = (split_ls[3], split_ls[5], split_ls[7], split_ls[9])
    elif directory == "results_variants" or directory == "results_variants_vllm":
        assert len(split_ls) == 15
        key = (split_ls[4], split_ls[6], split_ls[8], split_ls[10], split_ls[12])
    elif directory == "results_layers" or directory == "results_layers_vllm":
        assert len(split_ls) == 15
        key = (split_ls[4], split_ls[6], split_ls[8], split_ls[10], split_ls[12])
    elif directory == "results_hidden_size" or directory == "results_hidden_size_vllm":
        assert len(split_ls) == 15
        key = (split_ls[4], split_ls[6], split_ls[8], split_ls[10], split_ls[12])
    else:
        raise ValueError("no directory")
    if split_ls[2] == "latency":
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                line_split = line.split(' ')
                if key in data_dict.keys():
                    data_dict[key].append(float(line_split[2]))
                else:
                    data_dict[key] = [float(line_split[2])]

key_list = list(data_dict.keys())
key_list.sort()
for key in key_list:
    if (directory == "results" or directory == "results_vllm") and int(key[1]) == 1:
        print(key, data_dict[key])
    if (directory == "results_variants" or directory == "results_variants_vllm") and int(key[2]) == 1:
        print(key, data_dict[key])
    if (directory == "results_layers" or directory == "results_layers_vllm") and int(key[2]) == 1:
        print(key, data_dict[key])
    if (directory == "results_hidden_size" or directory == "results_hidden_size_vllm") and int(key[2]) == 1:
        print(key, data_dict[key])

