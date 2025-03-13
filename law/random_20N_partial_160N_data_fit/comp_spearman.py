from scipy.stats import spearmanr

chinchilla_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
chinchilla_predicted_80M = [
    5.0878, 5.0936, 5.0824, 5.0936, 5.0957,
    4.5372, 4.5429, 4.5317, 4.543,  4.5451,
    3.7646, 3.7703, 3.7591,
]
chinchilla_correlation_80M, _ = spearmanr(chinchilla_actual_80M, chinchilla_predicted_80M)
print(f"chinchilla_correlation_80M: {chinchilla_correlation_80M}")

chinchilla_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
chinchilla_predicted_116M = [
    4.607,  4.6214, 4.6158, 4.596,  4.6121, 4.6092,
    4.1217, 4.1361, 4.1305, 4.1107, 4.1267,
    3.4406, 3.455,  3.4494,
]
chinchilla_correlation_116M, _ = spearmanr(chinchilla_actual_116M, chinchilla_predicted_116M)
print(f"chinchilla_correlation_116M: {chinchilla_correlation_116M}")

chinchilla_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
chinchilla_predicted_164M = [
    4.2069, 4.2155, 4.205,  4.2125, 4.2032,
    3.7773, 3.7859, 3.7754, 3.783,  3.7736,
    3.1745, 3.1831, 3.1726,
]
chinchilla_correlation_164M, _ = spearmanr(chinchilla_actual_164M, chinchilla_predicted_164M)
print(f"chinchilla_correlation_164M: {chinchilla_correlation_164M}")

chinchilla_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
chinchilla_predicted_237M = [
    3.8399, 3.8461, 3.834,  3.8358,
    3.4613, 3.4676, 3.4555, 3.4572,
]
chinchilla_correlation_237M, _ = spearmanr(chinchilla_actual_237M, chinchilla_predicted_237M)
print(f"chinchilla_correlation_237M: {chinchilla_correlation_237M}")

chinchilla_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
chinchilla_predicted_313M = [
    3.5905, 3.5921, 3.5874, 3.5883,
    3.2455, 3.247,  3.2424, 3.2432,
    2.7612, 2.7628,
]
chinchilla_correlation_313M, _ = spearmanr(chinchilla_actual_313M, chinchilla_predicted_313M)
print(f"chinchilla_correlation_313M: {chinchilla_correlation_313M}")

chinchilla_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
chinchilla_predicted_1B = [
    2.5533, 2.5428, 2.5529, 2.5274,
]
chinchilla_correlation_1B, _ = spearmanr(chinchilla_actual_1B, chinchilla_predicted_1B)
print(f"chinchilla_correlation_1B: {chinchilla_correlation_1B}")


inference_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
inference_predicted_80M = [
    4.9923, 5.0347, 5.0786, 4.9706, 4.952,
    4.3987, 4.4368, 4.4741, 4.3803, 4.3641,
    3.7379, 3.7711, 3.8012,
]
inference_correlation_80M, _ = spearmanr(inference_actual_80M, inference_predicted_80M)
print(f"inference_correlation_80M: {inference_correlation_80M}")

inference_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
inference_predicted_116M = [
    4.4882, 4.537,  4.5725, 4.594,  4.4708, 4.4502,
    4.0078, 4.0528, 4.084,  4.1012, 3.9928,
    3.4731, 3.5137, 3.5401,
]
inference_correlation_116M, _ = spearmanr(inference_actual_116M, inference_predicted_116M)
print(f"inference_correlation_116M: {inference_correlation_116M}")

inference_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
inference_predicted_164M = [
    4.1015, 4.135,  4.1522, 4.2013, 4.2347,
    3.71,   3.741,  3.7557, 3.8007, 3.8302,
    3.2741, 3.3023, 3.3143,
]
inference_correlation_164M, _ = spearmanr(inference_actual_164M, inference_predicted_164M)
print(f"inference_correlation_164M: {inference_correlation_164M}")

inference_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
inference_predicted_237M = [
    3.7752, 3.8006, 3.8102, 3.8384,
    3.4585, 3.4822, 3.4902, 3.5161,
]
inference_correlation_237M, _ = spearmanr(inference_actual_237M, inference_predicted_237M)
print(f"inference_correlation_237M: {inference_correlation_237M}")

inference_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
inference_predicted_313M = [
    3.5704, 3.5887, 3.6064, 3.63,
    3.2993, 3.3162, 3.3324, 3.3542,
    2.9974, 3.0129,
]
inference_correlation_313M, _ = spearmanr(inference_actual_313M, inference_predicted_313M)
print(f"inference_correlation_313M: {inference_correlation_313M}")

inference_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
inference_predicted_1B = [
    2.875,  2.8968, 2.9239, 2.917,
]
inference_correlation_1B, _ = spearmanr(inference_actual_1B, inference_predicted_1B)
print(f"inference_correlation_1B: {inference_correlation_1B}")

