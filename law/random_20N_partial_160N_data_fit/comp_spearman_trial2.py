from scipy.stats import spearmanr

chinchilla_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
chinchilla_predicted_80M = [
    4.9637, 4.9687, 4.959,  4.9687, 4.9705,
    4.4262, 4.4311, 4.4214, 4.4312, 4.433,
    3.7076, 3.7126, 3.7029,
]
chinchilla_correlation_80M, _ = spearmanr(chinchilla_actual_80M, chinchilla_predicted_80M)
print(f"chinchilla_correlation_80M: {chinchilla_correlation_80M}")

chinchilla_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
chinchilla_predicted_116M = [
    4.5126, 4.5248, 4.52,   4.5032, 4.5169, 4.5144,
    4.0471, 4.0593, 4.0545, 4.0377, 4.0514,
    3.4249, 3.4371, 3.4323,
]
chinchilla_correlation_116M, _ = spearmanr(chinchilla_actual_116M, chinchilla_predicted_116M)
print(f"chinchilla_correlation_116M: {chinchilla_correlation_116M}")

chinchilla_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
chinchilla_predicted_164M = [
    4.1428, 4.15,   4.1413, 4.1475, 4.1397,
    3.7378, 3.745,  3.7362, 3.7425, 3.7347,
    3.1964, 3.2036, 3.1948,
]
chinchilla_correlation_164M, _ = spearmanr(chinchilla_actual_164M, chinchilla_predicted_164M)
print(f"chinchilla_correlation_164M: {chinchilla_correlation_164M}")

chinchilla_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
chinchilla_predicted_237M = [
    3.8095, 3.8147, 3.8047, 3.8061,
    3.4589, 3.4641, 3.4541, 3.4555,
]
chinchilla_correlation_237M, _ = spearmanr(chinchilla_actual_237M, chinchilla_predicted_237M)
print(f"chinchilla_correlation_237M: {chinchilla_correlation_237M}")

chinchilla_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
chinchilla_predicted_313M = [
    3.5873, 3.5885, 3.5848, 3.5855,
    3.2718, 3.273,  3.2693, 3.27,
    2.8501, 2.8513,
]
chinchilla_correlation_313M, _ = spearmanr(chinchilla_actual_313M, chinchilla_predicted_313M)
print(f"chinchilla_correlation_313M: {chinchilla_correlation_313M}")

chinchilla_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
chinchilla_predicted_1B = [
    2.6975, 2.6896, 2.6971, 2.678,
]
chinchilla_correlation_1B, _ = spearmanr(chinchilla_actual_1B, chinchilla_predicted_1B)
print(f"chinchilla_correlation_1B: {chinchilla_correlation_1B}")


inference_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
inference_predicted_80M = [
    4.9922, 5.0243, 5.0536, 4.9771, 4.9633,
    4.3933, 4.4222, 4.4467, 4.3806, 4.3687,
    3.7074, 3.7325, 3.7517,
]
inference_correlation_80M, _ = spearmanr(inference_actual_80M, inference_predicted_80M)
print(f"inference_correlation_80M: {inference_correlation_80M}")

inference_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
inference_predicted_116M = [
    4.4979, 4.5362, 4.5607, 4.5721, 4.4858, 4.4697,
    4.008,  4.0435, 4.0648, 4.0731, 3.9977,
    3.447,  3.4792, 3.4969,
]
inference_correlation_116M, _ = spearmanr(inference_actual_116M, inference_predicted_116M)
print(f"inference_correlation_116M: {inference_correlation_116M}")

inference_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
inference_predicted_164M = [
    4.1142, 4.1403, 4.1509, 4.1874, 4.2092,
    3.7108, 3.7351, 3.7438, 3.7773, 3.7962,
    3.2489, 3.2709, 3.2775,
]
inference_correlation_164M, _ = spearmanr(inference_actual_164M, inference_predicted_164M)
print(f"inference_correlation_164M: {inference_correlation_164M}")

inference_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
inference_predicted_237M = [
    3.7872, 3.8069, 3.8118, 3.8323,
    3.4574, 3.4758, 3.4795, 3.4984,
]
inference_correlation_237M, _ = spearmanr(inference_actual_237M, inference_predicted_237M)
print(f"inference_correlation_237M: {inference_correlation_237M}")

inference_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
inference_predicted_313M = [
    3.5803, 3.594,  3.6061, 3.6232,
    3.2957, 3.3084, 3.3193, 3.3351,
    2.9698, 2.9813,
]
inference_correlation_313M, _ = spearmanr(inference_actual_313M, inference_predicted_313M)
print(f"inference_correlation_313M: {inference_correlation_313M}")

inference_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
inference_predicted_1B = [
    2.8572, 2.8715, 2.8922, 2.8836,
]
inference_correlation_1B, _ = spearmanr(inference_actual_1B, inference_predicted_1B)
print(f"inference_correlation_1B: {inference_correlation_1B}")

