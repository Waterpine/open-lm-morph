filename = "results/world_knowledge/open_lm_ex_80m_v7_40N_epoch_2.txt"

task_list = []
acc_list = []
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line_split = line.split(" ")
        if line_split[0].split('/')[1] == "mmlu":
            pass
        elif line_split[0].split('/')[1] == "mmlu_expand":
            pass
        elif line_split[0].split('/')[1] == "jeopardy":
            pass
        elif line_split[0].split('/')[1] == "jeopardy_small":
            pass
        elif line_split[0].split('/')[1] == "bbq":
            pass
        else:
            task_list.append(line_split[0].split('/')[1])
            acc_list.append(float(line_split[2]))
print(task_list)
print(acc_list)

