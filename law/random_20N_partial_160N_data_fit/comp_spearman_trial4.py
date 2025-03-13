from scipy.stats import spearmanr

chinchilla_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
chinchilla_predicted_80M = [
    4.9697, 4.9746, 4.9651, 4.9747, 4.9764,
    4.4297, 4.4346, 4.4251, 4.4347, 4.4364,
    3.7072, 3.7121, 3.7025,
]
chinchilla_correlation_80M, _ = spearmanr(chinchilla_actual_80M, chinchilla_predicted_80M)
print(f"chinchilla_correlation_80M: {chinchilla_correlation_80M}")

chinchilla_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
chinchilla_predicted_116M = [
    4.5199, 4.5319, 4.5272, 4.5107, 4.5241, 4.5216,
    4.0521, 4.0641, 4.0594, 4.0429, 4.0563,
    3.4262, 3.4382, 3.4335,
]
chinchilla_correlation_116M, _ = spearmanr(chinchilla_actual_116M, chinchilla_predicted_116M)
print(f"chinchilla_correlation_116M: {chinchilla_correlation_116M}")

chinchilla_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
chinchilla_predicted_164M = [
    4.1509, 4.158,  4.1494, 4.1556, 4.1479,
    3.7437, 3.7509, 3.7422, 3.7484, 3.7407,
    3.199,  3.2061, 3.1974,
]
chinchilla_correlation_164M, _ = spearmanr(chinchilla_actual_164M, chinchilla_predicted_164M)
print(f"chinchilla_correlation_164M: {chinchilla_correlation_164M}")

chinchilla_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
chinchilla_predicted_237M = [
    3.8182, 3.8233, 3.8135, 3.8149,
    3.4656, 3.4707, 3.4609, 3.4623,
]
chinchilla_correlation_237M, _ = spearmanr(chinchilla_actual_237M, chinchilla_predicted_237M)
print(f"chinchilla_correlation_237M: {chinchilla_correlation_237M}")

chinchilla_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
chinchilla_predicted_313M = [
    3.5964, 3.5976, 3.5939, 3.5946,
    3.2791, 3.2803, 3.2766, 3.2773,
    2.8545, 2.8557,
]
chinchilla_correlation_313M, _ = spearmanr(chinchilla_actual_313M, chinchilla_predicted_313M)
print(f"chinchilla_correlation_313M: {chinchilla_correlation_313M}")

chinchilla_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
chinchilla_predicted_1B = [
    2.7073, 2.6995, 2.707,  2.6881,
]
chinchilla_correlation_1B, _ = spearmanr(chinchilla_actual_1B, chinchilla_predicted_1B)
print(f"chinchilla_correlation_1B: {chinchilla_correlation_1B}")


inference_actual_80M = [
    4.9619, 5.0119, 5.0774, 4.9761, 4.9908,
    4.3655, 4.4234, 4.4899, 4.353,  4.3594,
    3.7074, 3.7712, 3.8428,
]
inference_predicted_80M = [
    4.9908, 5.0258, 5.0613, 4.9742, 4.96,
    4.3721, 4.4035, 4.4333, 4.3582, 4.3461,
    3.7074, 3.7348, 3.7586,
]
inference_correlation_80M, _ = spearmanr(inference_actual_80M, inference_predicted_80M)
print(f"inference_correlation_80M: {inference_correlation_80M}")

inference_actual_116M = [
    4.4789, 4.519,  4.5593, 4.5975, 4.4881, 4.5089,
    3.989,  4.0445, 4.0931, 4.1233, 3.9859,
    3.4816, 3.5451, 3.5982,
]
inference_predicted_116M = [
    4.4843, 4.5252, 4.5543, 4.5713, 4.471,  4.4546,
    3.9902, 4.0279, 4.0533, 4.0667, 3.9788,
    3.4594, 3.4936, 3.5151,
]
inference_correlation_116M, _ = spearmanr(inference_actual_116M, inference_predicted_116M)
print(f"inference_correlation_116M: {inference_correlation_116M}")

inference_actual_164M = [
    4.096,  4.1163, 4.1342, 4.1873, 4.2323,
    3.7125, 3.7411, 3.763,  3.8249, 3.8662,
    3.3163, 3.3522, 3.3794,
]
inference_predicted_164M = [
    4.1,    4.1279, 4.1415, 4.183,  4.2112,
    3.7025, 3.7283, 3.7398, 3.7779, 3.8026,
    3.2754, 3.299,  3.3082,
]
inference_correlation_164M, _ = spearmanr(inference_actual_164M, inference_predicted_164M)
print(f"inference_correlation_164M: {inference_correlation_164M}")

inference_actual_237M = [
    3.7838, 3.7991, 3.7998, 3.8274,
    3.4827, 3.5047, 3.5099, 3.5437,
]
inference_predicted_237M = [
    3.7801, 3.8011, 3.8084, 3.832,
    3.4628, 3.4824, 3.4884, 3.5101,
]
inference_correlation_237M, _ = spearmanr(inference_actual_237M, inference_predicted_237M)
print(f"inference_correlation_237M: {inference_correlation_237M}")

inference_actual_313M = [
    3.5904, 3.5961, 3.6079, 3.6272,
    3.337,  3.3469, 3.361,  3.3885,
    3.0646, 3.0811,
]
inference_predicted_313M = [
    3.5822, 3.5971, 3.6116, 3.6313,
    3.3132, 3.327,  3.3402, 3.3585,
    3.0241, 3.0368,
]
inference_correlation_313M, _ = spearmanr(inference_actual_313M, inference_predicted_313M)
print(f"inference_correlation_313M: {inference_correlation_313M}")

inference_actual_1B = [
    2.896,  2.909,  2.9326, 2.9198,
]
inference_predicted_1B = [
    2.9266, 2.945,  2.9679, 2.9625,
]
inference_correlation_1B, _ = spearmanr(inference_actual_1B, inference_predicted_1B)
print(f"inference_correlation_1B: {inference_correlation_1B}")

