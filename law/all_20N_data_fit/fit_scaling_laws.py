import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


def compute_r_squared(y_true, y_pred):
    # Convert lists to numpy arrays if they aren't already
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # Calculate the mean of observed data
    mean_y_true = np.mean(y_true)
    # Calculate total sum of squares (SS_tot)
    ss_tot = np.sum((y_true - mean_y_true) ** 2)
    # Calculate residual sum of squares (SS_res)
    ss_res = np.sum((y_true - y_pred) ** 2)
    # Calculate R-squared
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


def func(X, A, B, E, alpha):
    N, D = X
    return E + A / np.power(N, alpha) + B / np.power(D, alpha)


model_size_fit_20N_list = ["80M", "116M", "164M", "237M", "313M"]
model_variants_fit_20N_list = {
    "80M": ["80M_v1", "80M_v4", "80M_v5", "80M_v6", "80M_v7"],
    "116M": ["116M_v1", "116M_v2", "116M_v3", "116M_v4", "116M_v5", "116M_v6"],
    "164M": ["164M_v1", "164M_v4", "164M_v5", "164M_v6", "164M_v7"],
    "237M": ["237M_v1", "237M_v2", "237M_v3", "237M_v4"],
    "313M": ["313M_v1", "313M_v2", "313M_v3", "313M_v4"],
}

model_size_fit_160N_list = []
model_variants_fit_160N_list = {
    "80M": ["80M_v1", "80M_v4", "80M_v5"],
    "116M": ["116M_v1", "116M_v2", "116M_v3"],
    "164M": ["164M_v1", "164M_v4", "164M_v5"],
    "313M": ["313M_v1", "313M_v2"],
}

parameters_fit_dict = {
    "80M_v1": 78914048,
    "80M_v4": 78010560,
    "80M_v5": 79794560,
    "80M_v6": 77999936,
    "80M_v7": 77677440,
    "116M_v1": 115356800,
    "116M_v2": 111615120,
    "116M_v3": 113056800,
    "116M_v4": 118334480,
    "116M_v5": 114024400,
    "116M_v6": 114793440,
    "164M_v1": 162417408,
    "164M_v4": 158824800,
    "164M_v5": 163197120,
    "164M_v6": 160048416,
    "164M_v7": 163979136,
    "164M_v8": 165347616,
    "237M_v1": 231695744,
    "237M_v2": 227490480,
    "237M_v3": 235702880,
    "237M_v4": 234509968,
    "313M_v1": 308839424,
    "313M_v2": 307327104,
    "313M_v3": 311975680,
    "313M_v4": 311087744,
}

loss_fit_20N_dict = {
    "80M_v1": 4.9619,
    "80M_v4": 5.0119,
    "80M_v5": 5.0774,
    "80M_v6": 4.9761,
    "80M_v7": 4.9908,
    "116M_v1": 4.4789,
    "116M_v2": 4.5190,
    "116M_v3": 4.5593,
    "116M_v4": 4.5975,
    "116M_v5": 4.4881,
    "116M_v6": 4.5089,
    "164M_v1": 4.0960,
    "164M_v4": 4.1163,
    "164M_v5": 4.1342,
    "164M_v6": 4.1873,
    "164M_v7": 4.2323,
    "237M_v1": 3.7838,
    "237M_v2": 3.7991,
    "237M_v3": 3.7998,
    "237M_v4": 3.8274,
    "313M_v1": 3.5904,
    "313M_v2": 3.5961,
    "313M_v3": 3.6079,
    "313M_v4": 3.6272,
}

loss_fit_160N_dict = {
    "80M_v1": 3.7074,
    "80M_v4": 3.7712,
    "80M_v5": 3.8428,
    "116M_v1": 3.4816,
    "116M_v2": 3.5451,
    "116M_v3": 3.5982,
    "164M_v1": 3.3163,
    "164M_v4": 3.3522,
    "164M_v5": 3.3794,
    "313M_v1": 3.0646,
    "313M_v2": 3.0811,
}

tokens_fit_20N_dict = {
    "80M": 1610612736,
    "116M": 2315255808,
    "164M": 3288334336,
    "237M": 4731174912,
    "313M": 6174015488
}

tokens_fit_160N_dict = {
    "80M": 12884901888,
    "116M": 18522046464,
    "164M": 26306674688,
    "313M": 49392123904
}

N_data_fit_list = []
D_data_fit_list = []
loss_data_fit_list = []
model_variants_fit_choice_list = []
for model_size in model_size_fit_20N_list:
    for model_variants in model_variants_fit_20N_list[model_size]:
        N_data_fit_list.append(parameters_fit_dict[model_variants])
        D_data_fit_list.append(tokens_fit_20N_dict[model_size])
        loss_data_fit_list.append(loss_fit_20N_dict[model_variants])
        model_variants_fit_choice_list.append(model_variants)

for model_size in model_size_fit_160N_list:
    for model_variants in model_variants_fit_160N_list[model_size]:
        N_data_fit_list.append(parameters_fit_dict[model_variants])
        D_data_fit_list.append(tokens_fit_160N_dict[model_size])
        loss_data_fit_list.append(loss_fit_160N_dict[model_variants])
        model_variants_fit_choice_list.append(model_variants)

N_data_fit = np.array(N_data_fit_list)
D_data_fit = np.array(D_data_fit_list)
loss_data_fit = np.array(loss_data_fit_list)
print(N_data_fit)
print(D_data_fit)
print(loss_data_fit)
popt, pcov = curve_fit(func, (N_data_fit, D_data_fit), loss_data_fit, maxfev=100000)
print(popt)
A = popt[0]
B = popt[1]
E = popt[2]
alpha = popt[3]
beta = popt[3]
sum_error = 0.0
for idx in range(len(N_data_fit)):
    model_variants = model_variants_fit_choice_list[idx]
    loss_predict = E + A / np.power(N_data_fit[idx], alpha) + B / np.power(D_data_fit[idx], beta)
    sum_error = sum_error + (loss_predict - loss_data_fit_list[idx]) ** 2
    # print(f"model_variants: {model_variants}, loss_predict: {loss_predict}")
print(f"sum_error: {sum_error}")
print(f"MSE: {sum_error / len(N_data_fit)}")

# 1B prediction
D_1b = 28991029248
N_v1_1b = 1439795200
N_v3_1b = 1527073280
N_v6_1b = 1443304192
N_v8_1b = 1668885504
loss_v1_1b = E + A / np.power(N_v1_1b, alpha) + B / np.power(D_1b, beta)
print(f"loss_v1_1b: {loss_v1_1b}, error: {abs(loss_v1_1b - 2.8960) / 2.8960}")
loss_v3_1b = E + A / np.power(N_v3_1b, alpha) + B / np.power(D_1b, beta)
print(f"loss_v3_1b: {loss_v3_1b}, error: {abs(loss_v3_1b - 2.9090) / 2.9090}")
loss_v6_1b = E + A / np.power(N_v6_1b, alpha) + B / np.power(D_1b, beta)
print(f"loss_v6_1b: {loss_v6_1b}, error: {abs(loss_v6_1b - 2.9326) / 2.9326}")
loss_v8_1b = E + A / np.power(N_v8_1b, alpha) + B / np.power(D_1b, beta)
print(f"loss_v8_1b: {loss_v8_1b}, error: {abs(loss_v8_1b - 2.9198) / 2.9198}")

# Testing, compute MSE and R^2

model_size_test_20N_list = ["80M", "86M", "116M", "126M", "164M", "178M", "237M", "313M", "339M", "1B"]
model_variants_test_20N_list = {
    "80M": ["80M_v1", "80M_v4", "80M_v5", "80M_v6", "80M_v7"],
    "86M": ["86M_v1", "86M_v2"],
    "116M": ["116M_v1", "116M_v2", "116M_v3", "116M_v4", "116M_v5", "116M_v6"],
    "126M": ["126M_v1", "126M_v2"],
    "164M": ["164M_v1", "164M_v4", "164M_v5", "164M_v6", "164M_v7"],
    "178M": ["178M_v1", "178M_v2"],
    "237M": ["237M_v1", "237M_v2", "237M_v3", "237M_v4"],
    "313M": ["313M_v1", "313M_v2", "313M_v3", "313M_v4"],
    "339M": ["339M_v1"],
    "1B": ["1B_v1", "1B_v3", "1B_v6", "1B_v8"],
}

model_size_test_40N_list = ["80M", "116M", "164M", "237M", "313M"]
model_variants_test_40N_list = {
    "80M": ["80M_v1", "80M_v4", "80M_v5", "80M_v6", "80M_v7"],
    "116M": ["116M_v1", "116M_v2", "116M_v3", "116M_v4", "116M_v5"],
    "164M": ["164M_v1", "164M_v4", "164M_v5", "164M_v6", "164M_v7"],
    "237M": ["237M_v1", "237M_v2", "237M_v3", "237M_v4"],
    "313M": ["313M_v1", "313M_v2", "313M_v3", "313M_v4"],
}

model_size_test_160N_list = ["80M", "86M", "116M", "126M", "164M", "178M", "313M", "339M"]
model_variants_test_160N_list = {
    "80M": ["80M_v1", "80M_v4", "80M_v5"],
    "86M": ["86M_v1", "86M_v2"],
    "116M": ["116M_v1", "116M_v2", "116M_v3"],
    "126M": ["126M_v1", "126M_v2"],
    "164M": ["164M_v1", "164M_v4", "164M_v5"],
    "178M": ["178M_v1", "178M_v2"],
    "313M": ["313M_v1", "313M_v2"],
    "339M": ["339M_v1"],
}

parameters_test_dict = {
    "80M_v1": 78914048,
    "80M_v4": 78010560,
    "80M_v5": 79794560,
    "80M_v6": 77999936,
    "80M_v7": 77677440,
    "86M_v1": 85975488,
    "86M_v2": 84874880,
    "116M_v1": 115356800,
    "116M_v2": 111615120,
    "116M_v3": 113056800,
    "116M_v4": 118334480,
    "116M_v5": 114024400,
    "116M_v6": 114793440,
    "126M_v1": 124612560,
    "126M_v2": 121148000,
    "164M_v1": 162417408,
    "164M_v4": 158824800,
    "164M_v5": 163197120,
    "164M_v6": 160048416,
    "164M_v7": 163979136,
    "164M_v8": 165347616,
    "178M_v1": 176744160,
    "178M_v2": 174258240,
    "237M_v1": 231695744,
    "237M_v2": 227490480,
    "237M_v3": 235702880,
    "237M_v4": 234509968,
    "313M_v1": 308839424,
    "313M_v2": 307327104,
    "313M_v3": 311975680,
    "313M_v4": 311087744,
    "339M_v1": 339182208,
    "1B_v1": 1439795200,
    "1B_v3": 1527073280,
    "1B_v6": 1443304192,
    "1B_v8": 1668885504,
}

loss_test_20N_dict = {
    "80M_v1": 4.9619,
    "80M_v4": 5.0119,
    "80M_v5": 5.0774,
    "80M_v6": 4.9761,
    "80M_v7": 4.9908,
    "86M_v1": 4.9371,
    "86M_v2": 4.9887,
    "116M_v1": 4.4789,
    "116M_v2": 4.5190,
    "116M_v3": 4.5593,
    "116M_v4": 4.5975,
    "116M_v5": 4.4881,
    "116M_v6": 4.5089,
    "126M_v1": 4.4568,
    "126M_v2": 4.5043,
    "164M_v1": 4.0960,
    "164M_v4": 4.1163,
    "164M_v5": 4.1342,
    "164M_v6": 4.1873,
    "164M_v7": 4.2323,
    "178M_v1": 4.0763,
    "178M_v2": 4.0934,
    "237M_v1": 3.7838,
    "237M_v2": 3.7991,
    "237M_v3": 3.7998,
    "237M_v4": 3.8274,
    "313M_v1": 3.5904,
    "313M_v2": 3.5961,
    "313M_v3": 3.6079,
    "313M_v4": 3.6272,
    "339M_v1": 3.5719,
    "1B_v1": 2.8960,
    "1B_v3": 2.9090,
    "1B_v6": 2.9326,
    "1B_v8": 2.9198,
}

loss_test_40N_dict = {
    "80M_v1": 4.3655,
    "80M_v4": 4.4234,
    "80M_v5": 4.4899,
    "80M_v6": 4.3530,
    "80M_v7": 4.3594,
    "116M_v1": 3.9890,
    "116M_v2": 4.0445,
    "116M_v3": 4.0931,
    "116M_v4": 4.1233,
    "116M_v5": 3.9859,
    "164M_v1": 3.7125,
    "164M_v4": 3.7411,
    "164M_v5": 3.7630,
    "164M_v6": 3.8249,
    "164M_v7": 3.8662,
    "237M_v1": 3.4827,
    "237M_v2": 3.5047,
    "237M_v3": 3.5099,
    "237M_v4": 3.5437,
    "313M_v1": 3.3370,
    "313M_v2": 3.3469,
    "313M_v3": 3.3610,
    "313M_v4": 3.3885,
}

loss_test_160N_dict = {
    "80M_v1": 3.7074,
    "80M_v4": 3.7712,
    "80M_v5": 3.8428,
    "86M_v1": 3.6964,
    "86M_v2": 3.7745,
    "116M_v1": 3.4816,
    "116M_v2": 3.5451,
    "116M_v3": 3.5982,
    "126M_v1": 3.4816,
    "126M_v2": 3.5448,
    "164M_v1": 3.3163,
    "164M_v4": 3.3522,
    "164M_v5": 3.3794,
    "178M_v1": 3.3063,
    "178M_v2": 3.3430,
    "313M_v1": 3.0646,
    "313M_v2": 3.0811,
    "339M_v1": 3.0522,
}

tokens_test_20N_dict = {
    "80M": 1610612736,
    "86M": 1610612736,
    "116M": 2315255808,
    "126M": 2315255808,
    "164M": 3288334336,
    "178M": 3288334336,
    "237M": 4731174912,
    "313M": 6174015488,
    "339M": 6174015488,
    "1B": 28991029248,
}

tokens_test_40N_dict = {
    "80M": 3221225472,
    "116M": 4630511616,
    "164M": 6576668672,
    "237M": 9462349824,
    "313M": 12348030976,
}

tokens_test_160N_dict = {
    "80M": 12884901888,
    "86M": 12884901888,
    "116M": 18522046464,
    "126M": 18522046464,
    "164M": 26306674688,
    "178M": 26306674688,
    "313M": 49392123904,
    "339M": 49392123904
}

count_20N = 0
count_40N = 0
count_160N = 0
N_data_test_list = []
D_data_test_list = []
loss_data_test_list = []
loss_predict_test_list = []
model_variants_choice_test_list = []
for model_size in model_size_test_20N_list:
    for model_variants in model_variants_test_20N_list[model_size]:
        N_data_test_list.append(parameters_test_dict[model_variants])
        D_data_test_list.append(tokens_test_20N_dict[model_size])
        loss_data_test_list.append(loss_test_20N_dict[model_variants])
        model_variants_choice_test_list.append(model_variants)
        count_20N = count_20N + 1

for model_size in model_size_test_40N_list:
    for model_variants in model_variants_test_40N_list[model_size]:
        N_data_test_list.append(parameters_test_dict[model_variants])
        D_data_test_list.append(tokens_test_40N_dict[model_size])
        loss_data_test_list.append(loss_test_40N_dict[model_variants])
        model_variants_choice_test_list.append(model_variants)
        count_40N = count_40N + 1

for model_size in model_size_test_160N_list:
    for model_variants in model_variants_test_160N_list[model_size]:
        N_data_test_list.append(parameters_test_dict[model_variants])
        D_data_test_list.append(tokens_test_160N_dict[model_size])
        loss_data_test_list.append(loss_test_160N_dict[model_variants])
        model_variants_choice_test_list.append(model_variants)
        count_160N = count_160N + 1

N_data_test = np.array(N_data_test_list)
D_data_test = np.array(D_data_test_list)
loss_data_test = np.array(loss_data_test_list)
sum_error_test = 0.0
for idx in range(len(N_data_test)):
    model_variants = model_variants_choice_test_list[idx]
    loss_predict = E + A / np.power(N_data_test[idx], alpha) + B / np.power(D_data_test[idx], beta)
    sum_error_test = sum_error_test + (loss_predict - loss_data_test_list[idx]) ** 2
    loss_predict_test_list.append(round(loss_predict, 4))

print(f"sum_error: {sum_error_test}")
print(f"MSE: {sum_error_test / len(N_data_test)}")
# print(len(N_data_test))
print(f"sklearn MSE: {np.mean((np.array(loss_data_test_list) - np.array(loss_predict_test_list))**2)}")
# print(len(loss_data_test_list), loss_data_test_list)
# print(len(loss_predict_test_list), loss_predict_test_list)
print(f"R^2 Score: {compute_r_squared(loss_data_test_list, loss_predict_test_list)}")
mse = mean_squared_error(loss_data_test_list, loss_predict_test_list)
print(f"mse: {mse}")
r2 = r2_score(loss_data_test_list, loss_predict_test_list)
print(f"R^2 Score: {r2}")
print(loss_data_test_list)
print(loss_predict_test_list)

print(loss_data_test_list[:count_20N])
print(loss_data_test_list[count_20N: count_20N + count_40N])
print(loss_data_test_list[count_20N + count_40N: count_20N + count_40N + count_160N])
print(loss_predict_test_list[:count_20N])
print(loss_predict_test_list[count_20N: count_20N + count_40N])
print(loss_predict_test_list[count_20N + count_40N: count_20N + count_40N + count_160N])


# Plot





