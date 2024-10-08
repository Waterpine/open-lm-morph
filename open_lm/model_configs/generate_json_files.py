import json


data_dict_14M = {
    '14m_v1': {
        "hidden_dim": 128,
        "n_layers": 3,
        "n_heads": 4,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '14m_v2': {
        "hidden_dim": 128,
        "n_layers": 4,
        "n_heads": 4,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '14m_v3': {
        "hidden_dim": 120,
        "n_layers": 7,
        "n_heads": 4,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '14m_v4': {
        "hidden_dim": 116,
        "n_layers": 9,
        "n_heads": 4,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '14m_v5': {
        "hidden_dim": 132,
        "n_layers": 2,
        "n_heads": 4,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_79M = {
    '79m_v1': {
        "hidden_dim": 512,
        "n_layers": 8,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v2': {
        "hidden_dim": 528,
        "n_layers": 7,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v3': {
        "hidden_dim": 488,
        "n_layers": 9,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v4': {
        "hidden_dim": 472,
        "n_layers": 11,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v5': {
        "hidden_dim": 544,
        "n_layers": 6,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v6': {
        "hidden_dim": 576,
        "n_layers": 5,
        "n_heads": 8,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '79m_v7': {
        "hidden_dim": 592,
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
        "hidden_dim": 660,
        "n_layers": 9,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v3': {
        "hidden_dim": 700,
        "n_layers": 7,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v4': {
        "hidden_dim": 740,
        "n_layers": 6,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v5': {
        "hidden_dim": 590,
        "n_layers": 12,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '116m_v6': {
        "hidden_dim": 560,
        "n_layers": 15,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_163M = {
    '163m_v1': {
        "hidden_dim": 768,
        "n_layers": 12,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '163m_v2': {
        "hidden_dim": 660,
        "n_layers": 18,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '163m_v3': {
        "hidden_dim": 840,
        "n_layers": 9,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '163m_v4': {
        "hidden_dim": 864,
        "n_layers": 8,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '163m_v5': {
        "hidden_dim": 900,
        "n_layers": 7,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '163m_v6': {
        "hidden_dim": 948,
        "n_layers": 6,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_232M = {
    '232m_v1': {
        "hidden_dim": 896,
        "n_layers": 14,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '232m_v2': {
        "hidden_dim": 1022,
        "n_layers": 10,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '232m_v3': {
        "hidden_dim": 1218,
        "n_layers": 6,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '232m_v4': {
        "hidden_dim": 1092,
        "n_layers": 8,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '232m_v5': {
        "hidden_dim": 770,
        "n_layers": 20,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '232m_v6': {
        "hidden_dim": 812,
        "n_layers": 18,
        "n_heads": 14,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_309M = {
    '309m_v1': {
        "hidden_dim": 1024,
        "n_layers": 16,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '309m_v2': {
        "hidden_dim": 1152,
        "n_layers": 12,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '309m_v3': {
        "hidden_dim": 1344,
        "n_layers": 8,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '309m_v4': {
        "hidden_dim": 1232,
        "n_layers": 10,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '309m_v5': {
        "hidden_dim": 960,
        "n_layers": 19,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '309m_v6': {
        "hidden_dim": 880,
        "n_layers": 22,
        "n_heads": 16,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_455M = {
    '455m_v1': {
        "hidden_dim": 1280,
        "n_layers": 16,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '455m_v2': {
        "hidden_dim": 1400,
        "n_layers": 13,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '455m_v3': {
        "hidden_dim": 1440,
        "n_layers": 12,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '455m_v4': {
        "hidden_dim": 1540,
        "n_layers": 10,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '455m_v5': {
        "hidden_dim": 1220,
        "n_layers": 18,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '455m_v6': {
        "hidden_dim": 1150,
        "n_layers": 21,
        "n_heads": 10,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


data_dict_695M = {
    '695m_v1': {
        "hidden_dim": 1536,
        "n_layers": 19,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '695m_v2': {
        "hidden_dim": 1608,
        "n_layers": 17,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '695m_v3': {
        "hidden_dim": 1692,
        "n_layers": 15,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '695m_v4': {
        "hidden_dim": 1800,
        "n_layers": 13,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '695m_v5': {
        "hidden_dim": 1440,
        "n_layers": 22,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
    '695m_v6': {
        "hidden_dim": 1332,
        "n_layers": 26,
        "n_heads": 12,
        "seq_len": 2048,
        "vocab_size": 50432,
        "post_embed_norm": False,
        "weight_tying": False
    },
}


for key in data_dict_14M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_14M[key], json_file, indent=4)
    assert data_dict_14M[key]["hidden_dim"] % data_dict_14M[key]["n_heads"] == 0


for key in data_dict_79M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_79M[key], json_file, indent=4)
    assert data_dict_79M[key]["hidden_dim"] % data_dict_79M[key]["n_heads"] == 0


for key in data_dict_116M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_116M[key], json_file, indent=4)
    assert data_dict_116M[key]["hidden_dim"] % data_dict_116M[key]["n_heads"] == 0


for key in data_dict_232M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_232M[key], json_file, indent=4)
    assert data_dict_232M[key]["hidden_dim"] % data_dict_232M[key]["n_heads"] == 0


for key in data_dict_309M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_309M[key], json_file, indent=4)
    assert data_dict_309M[key]["hidden_dim"] % data_dict_309M[key]["n_heads"] == 0


for key in data_dict_455M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_455M[key], json_file, indent=4)
    assert data_dict_455M[key]["hidden_dim"] % data_dict_455M[key]["n_heads"] == 0


for key in data_dict_695M.keys():
    filename = f"scale_open_lm_{key}.json"
    with open(filename, 'w') as json_file:
        json.dump(data_dict_695M[key], json_file, indent=4)
    assert data_dict_695M[key]["hidden_dim"] % data_dict_695M[key]["n_heads"] == 0

