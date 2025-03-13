from scipy.stats import spearmanr

chinchilla_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
chinchilla_predicted_80M = [
    5.0014, 5.0069, 4.9961, 5.0069, 5.0089,
    4.446,  4.4515, 4.4408, 4.4516, 4.4536,
    3.7722, 3.7776, 3.7669,
]
chinchilla_correlation_80M, _ = spearmanr(chinchilla_actual_80M, chinchilla_predicted_80M)
print(f"chinchilla_correlation_80M: {chinchilla_correlation_80M}")

chinchilla_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
chinchilla_predicted_116M = [
    4.523,  4.5361, 4.531,  4.5131, 4.5276, 4.525,
    4.0589, 4.072,  4.0669, 4.049,  4.0635,
    3.4958, 3.5089, 3.5038,
]
chinchilla_correlation_116M, _ = spearmanr(chinchilla_actual_116M, chinchilla_predicted_116M)
print(f"chinchilla_correlation_116M: {chinchilla_correlation_116M}")

chinchilla_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
chinchilla_predicted_164M = [
    4.1447, 4.1522, 4.1431, 4.1496, 4.1416,
    3.7546, 3.762,  3.753,  3.7595, 3.7514,
    3.2812, 3.2886, 3.2796,
]
chinchilla_correlation_164M, _ = spearmanr(chinchilla_actual_164M, chinchilla_predicted_164M)
print(f"chinchilla_correlation_164M: {chinchilla_correlation_164M}")

chinchilla_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
chinchilla_predicted_237M = [
    3.8154, 3.8205, 3.8106, 3.812,
    3.4895, 3.4946, 3.4847, 3.4861,
]
chinchilla_correlation_237M, _ = spearmanr(chinchilla_actual_237M, chinchilla_predicted_237M)
print(f"chinchilla_correlation_237M: {chinchilla_correlation_237M}")

chinchilla_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
]
chinchilla_predicted_313M = [
    3.6024, 3.6036, 3.6,    3.6006,
    3.3167, 3.3179, 3.3143, 3.315,
]
chinchilla_correlation_313M, _ = spearmanr(chinchilla_actual_313M, chinchilla_predicted_313M)
print(f"chinchilla_correlation_313M: {chinchilla_correlation_313M}")

chinchilla_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
chinchilla_predicted_1B = [
    2.8162, 2.8097, 2.816,  2.8002,
]
chinchilla_correlation_1B, _ = spearmanr(chinchilla_actual_1B, chinchilla_predicted_1B)
print(f"chinchilla_correlation_1B: {chinchilla_correlation_1B}")


inference_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
inference_predicted_80M = [
    4.9969, 5.0341, 5.0712, 4.9794, 4.9644,
    4.3952, 4.4286, 4.4599, 4.3806, 4.3676,
    3.7456, 3.7749, 3.8,
]
inference_correlation_80M, _ = spearmanr(inference_actual_80M, inference_predicted_80M)
print(f"inference_correlation_80M: {inference_correlation_80M}")

inference_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
inference_predicted_116M = [
    4.4881, 4.5316, 4.5621, 4.5794, 4.474,  4.4566,
    4.0067, 4.0469, 4.0736, 4.0872, 3.9947,
    3.487,  3.5236, 3.5462,
]
inference_correlation_116M, _ = spearmanr(inference_actual_116M, inference_predicted_116M)
print(f"inference_correlation_116M: {inference_correlation_116M}")

inference_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
inference_predicted_164M = [
    4.1019, 4.1315, 4.1456, 4.1895, 4.2188,
    3.7139, 3.7414, 3.7533, 3.7936, 3.8194,
    3.295,  3.3202, 3.3298,
]
inference_correlation_164M, _ = spearmanr(inference_actual_164M, inference_predicted_164M)
print(f"inference_correlation_164M: {inference_correlation_164M}")

inference_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
inference_predicted_237M = [
    3.7798, 3.8021, 3.8096, 3.8344,
    3.4696, 3.4904, 3.4965, 3.5194,
]
inference_correlation_237M, _ = spearmanr(inference_actual_237M, inference_predicted_237M)
print(f"inference_correlation_237M: {inference_correlation_237M}")

inference_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
inference_predicted_313M = [
    3.5798, 3.5956, 3.6107, 3.6315,
    3.3164, 3.331,  3.3448, 3.3641,
    3.0319, 3.0454,
]
inference_correlation_313M, _ = spearmanr(inference_actual_313M, inference_predicted_313M)
print(f"inference_correlation_313M: {inference_correlation_313M}")

inference_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
inference_predicted_1B = [
    2.9161, 2.9352, 2.9595, 2.9533,
]
inference_correlation_1B, _ = spearmanr(inference_actual_1B, inference_predicted_1B)
print(f"inference_correlation_1B: {inference_correlation_1B}")

