def exponential_moving_average(losses, alpha):
    ema = [losses[0]]
    for loss in losses[1:]:
        ema.append(alpha * loss + (1 - alpha) * ema[-1])
    return ema


def average(lst):
    return sum(lst) / len(lst)

length = 5888
filename = "logs/open_lm_ex_313m_v4_40N/out.log"
train_loss_list = []
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        line_split = line.split(" | ")
        # print(line_split)
        if len(line_split) == 3 and line_split[2].startswith("FLAG start epoch"):
            epoch_train_loss_list = []
            last_sum_train_loss = 0.0
        if len(line_split) == 3 and line_split[2].startswith("FLAG end epoch"):
            assert len(epoch_train_loss_list) == length
            train_loss_list.extend(epoch_train_loss_list)
        if len(line_split) == 3 and line_split[2].startswith("Train Loss (epoch)"):
            train_info = line_split[2].split(',')
            if len(train_info) == 5:
                train_loss = float(train_info[1].split(": ")[1])
                # print(f"train_loss: {train_loss}")
                epoch_train_loss_list.append(train_loss)
                curr_sum_train_loss = float(train_info[3].split(": ")[1])
                # print(f"train_loss: {train_loss}")
                # print(f"curr_sum_train_loss: {curr_sum_train_loss}")
                # print(f"last_sum_train_loss: {last_sum_train_loss}")
                # assert abs(train_loss - (curr_sum_train_loss - last_sum_train_loss) / 64) < 0.01
                last_sum_train_loss = curr_sum_train_loss

print(train_loss_list)
print(len(train_loss_list))
ema_list = exponential_moving_average(train_loss_list, 0.9)
print(average(ema_list))
for i in range(2):
    # print(len(ema_list[: (i + 1) * length]))
    # print(length)
    assert len(ema_list[: (i + 1) * length]) == length * (i + 1)
    print(i, round(average(ema_list[: (i + 1) * length]), 4))
