from scipy.stats import spearmanr

chinchilla_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
chinchilla_predicted_80M = [
    5.0069, 4.9921, 5.0211, 4.992,  4.9866,
    3.4101, 3.3954, 3.4243, 3.3952, 3.3898,
    1.4949, 1.4801, 1.5091,
]
chinchilla_correlation_80M, _ = spearmanr(chinchilla_actual_80M, chinchilla_predicted_80M)
print(f"chinchilla_correlation_80M: {chinchilla_correlation_80M}")

chinchilla_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
chinchilla_predicted_116M = [
    4.5438, 4.5086, 4.5224, 4.5705, 4.5315, 4.5386,
    3.2151, 3.18,   3.1937, 3.2419, 3.2028,
    1.6215, 1.5863, 1.6001,
]
chinchilla_correlation_116M, _ = spearmanr(chinchilla_actual_116M, chinchilla_predicted_116M)
print(f"chinchilla_correlation_116M: {chinchilla_correlation_116M}")

chinchilla_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
chinchilla_predicted_164M = [
    4.1451, 4.1251, 4.1494, 4.132,  4.1536,
    3.0328, 3.0128, 3.037,  3.0197, 3.0413,
    1.6986, 1.6786, 1.7029,
]
chinchilla_correlation_164M, _ = spearmanr(chinchilla_actual_164M, chinchilla_predicted_164M)
print(f"chinchilla_correlation_164M: {chinchilla_correlation_164M}")

chinchilla_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
chinchilla_predicted_237M = [
    3.8018, 3.7882, 3.8145, 3.8108,
    2.8767, 2.863,  2.8893, 2.8856,
]
chinchilla_correlation_237M, _ = spearmanr(chinchilla_actual_237M, chinchilla_predicted_237M)
print(f"chinchilla_correlation_237M: {chinchilla_correlation_237M}")

chinchilla_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
chinchilla_predicted_313M = [
    3.6063, 3.6031, 3.6127, 3.6109,
    2.7978, 2.7946, 2.8043, 2.8024,
    1.8281, 1.8249,
]
chinchilla_correlation_313M, _ = spearmanr(chinchilla_actual_313M, chinchilla_predicted_313M)
print(f"chinchilla_correlation_313M: {chinchilla_correlation_313M}")

chinchilla_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
chinchilla_predicted_1B = [
    2.8092, 2.8263, 2.8099, 2.8511,
]
chinchilla_correlation_1B, _ = spearmanr(chinchilla_actual_1B, chinchilla_predicted_1B)
print(f"chinchilla_correlation_1B: {chinchilla_correlation_1B}")


inference_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
inference_predicted_80M = [
    4.9996, 5.0248, 5.0701, 4.9774, 4.9618,
    4.0272, 4.0471, 4.0844, 4.0089, 3.9962,
    2.9632, 2.9773, 3.0058,
]
inference_correlation_80M, _ = spearmanr(inference_actual_80M, inference_predicted_80M)
print(f"inference_correlation_80M: {inference_correlation_80M}")

inference_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
inference_predicted_116M = [
    4.5007, 4.5227, 4.5549, 4.5913, 4.483,  4.4708,
    3.7188, 3.7361, 3.7631, 3.7943, 3.7039,
    2.8633, 2.8755, 2.8967,
]
inference_correlation_116M, _ = spearmanr(inference_actual_116M, inference_predicted_116M)
print(f"inference_correlation_116M: {inference_correlation_116M}")

inference_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
inference_predicted_164M = [
    4.1083, 4.1252, 4.1478, 4.1778, 4.212,
    3.475,  3.4889, 3.5085, 3.5335, 3.5629,
    2.7821, 2.7927, 2.809,
]
inference_correlation_164M, _ = spearmanr(inference_actual_164M, inference_predicted_164M)
print(f"inference_correlation_164M: {inference_correlation_164M}")

inference_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
inference_predicted_237M = [
    3.7801, 3.7937, 3.8111, 3.8308,
    3.2712, 3.2827, 3.2982, 3.3152,
]
inference_correlation_237M, _ = spearmanr(inference_actual_237M, inference_predicted_237M)
print(f"inference_correlation_237M: {inference_correlation_237M}")

inference_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
inference_predicted_313M = [
    3.5839, 3.5963, 3.6132, 3.6303,
    3.1502, 3.161,  3.176,  3.191,
    2.6756, 2.6848,
]
inference_correlation_313M, _ = spearmanr(inference_actual_313M, inference_predicted_313M)
print(f"inference_correlation_313M: {inference_correlation_313M}")

inference_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
inference_predicted_1B = [
    2.8992, 2.9213, 2.9364, 2.9451,
]
inference_correlation_1B, _ = spearmanr(inference_actual_1B, inference_predicted_1B)
print(f"inference_correlation_1B: {inference_correlation_1B}")

