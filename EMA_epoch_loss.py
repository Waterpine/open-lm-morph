def exponential_moving_average(losses, alpha):
    ema = [losses[0]]
    for loss in losses[1:]:
        ema.append(alpha * loss + (1 - alpha) * ema[-1])
    return ema


def average(lst):
    return sum(lst) / len(lst)


filename = "logs/open_lm_ex_26753/out.log"
train_loss_list = []
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        line_split = line.split(" | ")
        # print(line_split)
        if len(line_split) == 3 and line_split[2].startswith("FLAG start epoch"):
            epoch_train_loss_list = []
        if len(line_split) == 3 and line_split[2].startswith("FLAG end epoch"):
            assert len(epoch_train_loss_list) == 64
            train_loss_list.extend(epoch_train_loss_list)
        if len(line_split) == 3 and line_split[2].startswith("Train Loss (epoch)"):
            train_info = line_split[2].split(',')
            if len(train_info) == 4:
                train_loss = float(train_info[1].split(": ")[1])
                # print(f"train_loss: {train_loss}")
                epoch_train_loss_list.append(train_loss)

print(train_loss_list)
print(len(train_loss_list))
ema_list = exponential_moving_average(train_loss_list, 0.1)
print(average(ema_list))
