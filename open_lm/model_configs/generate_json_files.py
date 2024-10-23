import json


data_dict_61M = {
    '61m_v1': {
        "hidden_dim": 448,
        "n_layers": 6,
        "n_heads": 7,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '61m_v2': {
        "hidden_dim": 504,
        "n_layers": 3,
        "n_heads": 7,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '61m_v3': {
        "hidden_dim": 392,
        "n_layers": 10,
        "n_heads": 7,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '61m_v4': {
        "hidden_dim": 336,
        "n_layers": 18,
        "n_heads": 7,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_80M = {
    '80m_v1': {
        "hidden_dim": 512,
        "n_layers": 8,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '80m_v2': {
        "hidden_dim": 448,
        "n_layers": 13,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '80m_v3': {
        "hidden_dim": 384,
        "n_layers": 22,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '80m_v4': {
        "hidden_dim": 576,
        "n_layers": 5,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '80m_v5': {
        "hidden_dim": 640,
        "n_layers": 3,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_86M = {
    '86m_v1': {
        "hidden_dim": 576,
        "n_layers": 7,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '86m_v2': {
        "hidden_dim": 640,
        "n_layers": 4,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_116M = {
    '116m_v1': {
        "hidden_dim": 640,
        "n_layers": 10,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v2': {
        "hidden_dim": 720,
        "n_layers": 6,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v3': {
        "hidden_dim": 800,
        "n_layers": 4,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v4': {
        "hidden_dim": 560,
        "n_layers": 15,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v5': {
        "hidden_dim": 480,
        "n_layers": 24,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_126M = {
    '126m_v1': {
        "hidden_dim": 720,
        "n_layers": 8,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '126m_v2': {
        "hidden_dim": 800,
        "n_layers": 5,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_164M = {
    '164m_v1': {
        "hidden_dim": 768,
        "n_layers": 12,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '164m_v2': {
        "hidden_dim": 672,
        "n_layers": 17,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '164m_v3': {
        "hidden_dim": 576,
        "n_layers": 26,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '164m_v4': {
        "hidden_dim": 864,
        "n_layers": 8,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '164m_v5': {
        "hidden_dim": 960,
        "n_layers": 6,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_178M = {
    '178m_v1': {
        "hidden_dim": 864,
        "n_layers": 10,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '178m_v2': {
        "hidden_dim": 960,
        "n_layers": 7,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_237M = {
    '237m_v1': {
        "hidden_dim": 896,
        "n_layers": 14,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '237m_v2': {
        "hidden_dim": 1008,
        "n_layers": 10,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '237m_v3': {
        "hidden_dim": 1120,
        "n_layers": 8,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '237m_v4': {
        "hidden_dim": 1232,
        "n_layers": 6,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '237m_v5': {
        "hidden_dim": 784,
        "n_layers": 20,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '237m_v6': {
        "hidden_dim": 672,
        "n_layers": 31,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_254M = {
    '254m_v1': {
        "hidden_dim": 1008,
        "n_layers": 12,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '254m_v2': {
        "hidden_dim": 1120,
        "n_layers": 9,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '254m_v3': {
        "hidden_dim": 1232,
        "n_layers": 7,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_313M = {
    '313m_v1': {
        "hidden_dim": 1024,
        "n_layers": 16,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '313m_v2': {
        "hidden_dim": 1152,
        "n_layers": 12,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '313m_v3': {
        "hidden_dim": 1280,
        "n_layers": 9,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '313m_v4': {
        "hidden_dim": 1408,
        "n_layers": 7,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '313m_v5': {
        "hidden_dim": 896,
        "n_layers": 22,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '313m_v6': {
        "hidden_dim": 768,
        "n_layers": 33,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_339M = {
    '339m_v1': {
        "hidden_dim": 1152,
        "n_layers": 14,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '339m_v2': {
        "hidden_dim": 1280,
        "n_layers": 10,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '339m_v3': {
        "hidden_dim": 1408,
        "n_layers": 8,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_469M = {
    '469m_v1': {
        "hidden_dim": 1280,
        "n_layers": 16,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '469m_v2': {
        "hidden_dim": 1360,
        "n_layers": 14,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '469m_v3': {
        "hidden_dim": 1440,
        "n_layers": 12,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '469m_v4': {
        "hidden_dim": 1520,
        "n_layers": 11,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '469m_v5': {
        "hidden_dim": 1200,
        "n_layers": 19,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '469m_v6': {
        "hidden_dim": 1120,
        "n_layers": 23,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_499M = {
    '499m_v1': {
        "hidden_dim": 1440,
        "n_layers": 14,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '499m_v2': {
        "hidden_dim": 1520,
        "n_layers": 12,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_712M = {
    '712m_v1': {
        "hidden_dim": 1536,
        "n_layers": 19,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '712m_v2': {
        "hidden_dim": 1632,
        "n_layers": 17,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '712m_v3': {
        "hidden_dim": 1728,
        "n_layers": 15,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '712m_v4': {
        "hidden_dim": 1824,
        "n_layers": 13,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '712m_v5': {
        "hidden_dim": 1440,
        "n_layers": 22,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '712m_v6': {
        "hidden_dim": 1344,
        "n_layers": 26,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


for key in data_dict_61M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_61M[key], json_file, indent=4)
    assert data_dict_61M[key]["hidden_dim"] % data_dict_61M[key]["n_heads"] == 0
    assert data_dict_61M[key]["n_heads"] == 7
    assert data_dict_61M[key]["hidden_dim"] / data_dict_61M[key]["n_heads"] % 8 == 0


for key in data_dict_80M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_80M[key], json_file, indent=4)
    assert data_dict_80M[key]["hidden_dim"] % data_dict_80M[key]["n_heads"] == 0
    assert data_dict_80M[key]["n_heads"] == 8
    assert data_dict_80M[key]["hidden_dim"] / data_dict_80M[key]["n_heads"] % 8 == 0


for key in data_dict_86M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_86M[key], json_file, indent=4)
    assert data_dict_86M[key]["hidden_dim"] % data_dict_86M[key]["n_heads"] == 0
    assert data_dict_86M[key]["n_heads"] == 8
    assert data_dict_86M[key]["hidden_dim"] / data_dict_86M[key]["n_heads"] % 8 == 0


for key in data_dict_116M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_116M[key], json_file, indent=4)
    assert data_dict_116M[key]["hidden_dim"] % data_dict_116M[key]["n_heads"] == 0
    assert data_dict_116M[key]["n_heads"] == 10
    assert data_dict_116M[key]["hidden_dim"] / data_dict_116M[key]["n_heads"] % 8 == 0


for key in data_dict_126M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_126M[key], json_file, indent=4)
    assert data_dict_126M[key]["hidden_dim"] % data_dict_126M[key]["n_heads"] == 0
    assert data_dict_126M[key]["n_heads"] == 10
    assert data_dict_126M[key]["hidden_dim"] / data_dict_126M[key]["n_heads"] % 8 == 0


for key in data_dict_164M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_164M[key], json_file, indent=4)
    assert data_dict_164M[key]["hidden_dim"] % data_dict_164M[key]["n_heads"] == 0
    assert data_dict_164M[key]["n_heads"] == 12
    assert data_dict_164M[key]["hidden_dim"] / data_dict_164M[key]["n_heads"] % 8 == 0


for key in data_dict_178M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_178M[key], json_file, indent=4)
    assert data_dict_178M[key]["hidden_dim"] % data_dict_178M[key]["n_heads"] == 0
    assert data_dict_178M[key]["n_heads"] == 12
    assert data_dict_178M[key]["hidden_dim"] / data_dict_178M[key]["n_heads"] % 8 == 0


for key in data_dict_237M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_237M[key], json_file, indent=4)
    assert data_dict_237M[key]["hidden_dim"] % data_dict_237M[key]["n_heads"] == 0
    assert data_dict_237M[key]["n_heads"] == 14
    assert data_dict_237M[key]["hidden_dim"] / data_dict_237M[key]["n_heads"] % 8 == 0


for key in data_dict_254M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_254M[key], json_file, indent=4)
    assert data_dict_254M[key]["hidden_dim"] % data_dict_254M[key]["n_heads"] == 0
    assert data_dict_254M[key]["n_heads"] == 14
    assert data_dict_254M[key]["hidden_dim"] / data_dict_254M[key]["n_heads"] % 8 == 0


for key in data_dict_313M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_313M[key], json_file, indent=4)
    assert data_dict_313M[key]["hidden_dim"] % data_dict_313M[key]["n_heads"] == 0
    assert data_dict_313M[key]["n_heads"] == 16
    assert data_dict_313M[key]["hidden_dim"] / data_dict_313M[key]["n_heads"] % 8 == 0


for key in data_dict_339M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_339M[key], json_file, indent=4)
    assert data_dict_339M[key]["hidden_dim"] % data_dict_339M[key]["n_heads"] == 0
    assert data_dict_339M[key]["n_heads"] == 16
    assert data_dict_339M[key]["hidden_dim"] / data_dict_339M[key]["n_heads"] % 8 == 0


for key in data_dict_469M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_469M[key], json_file, indent=4)
    assert data_dict_469M[key]["hidden_dim"] % data_dict_469M[key]["n_heads"] == 0
    assert data_dict_469M[key]["n_heads"] == 10
    assert data_dict_469M[key]["hidden_dim"] / data_dict_469M[key]["n_heads"] % 8 == 0


for key in data_dict_499M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_499M[key], json_file, indent=4)
    assert data_dict_499M[key]["hidden_dim"] % data_dict_499M[key]["n_heads"] == 0
    assert data_dict_499M[key]["n_heads"] == 10
    assert data_dict_499M[key]["hidden_dim"] / data_dict_499M[key]["n_heads"] % 8 == 0


for key in data_dict_712M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_712M[key], json_file, indent=4)
    assert data_dict_712M[key]["hidden_dim"] % data_dict_712M[key]["n_heads"] == 0
    assert data_dict_712M[key]["n_heads"] == 12
    assert data_dict_712M[key]["hidden_dim"] / data_dict_712M[key]["n_heads"] % 8 == 0

