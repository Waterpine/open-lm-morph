filename = "results/world_knowledge/open_lm_ex_1.5b_v8_epoch_16.txt"

mmlu_list = []
mmlu_expand_list = []
jeopardy_list = []
jeopardy_small_list = []
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line_split = line.split(" ")
        if line_split[0].split('/')[1] == "mmlu":
            mmlu_list.append(float(line_split[2]))
        if line_split[0].split('/')[1] == "mmlu_expand":
            mmlu_expand_list.append(float(line_split[2]))
        if line_split[0].split('/')[1] == "jeopardy":
            jeopardy_list.append(float(line_split[2]))
        if line_split[0].split('/')[1] == "jeopardy_small":
            jeopardy_small_list.append(float(line_split[2]))

mmlu_average = sum(mmlu_list) / len(mmlu_list)
mmlu_expand_average = sum(mmlu_expand_list) / len(mmlu_expand_list)
jeopardy_average = sum(jeopardy_list) / len(jeopardy_list)
jeopardy_small_average = sum(jeopardy_small_list) / len(jeopardy_small_list)
print(f"mmlu_average: {mmlu_average}, number of subtasks: {len(mmlu_list)}")
print(f"mmlu_expand_average: {mmlu_expand_average}, number of subtasks: {len(mmlu_expand_list)}")
print(f"jeopardy_average: {jeopardy_average}, number of subtasks: {len(jeopardy_list)}")
print(f"jeopardy_small_average: {jeopardy_small_average}, number of subtasks: {len(jeopardy_small_list)}")

filename = "results/safety/open_lm_ex_1.5b_v8_epoch_16.txt"

bbq_list = []
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line_split = line.split(" ")
        if line_split[0].split('/')[1] == "bbq":
            bbq_list.append(float(line_split[2]))
bbq_average = sum(bbq_list) / len(bbq_list)
print(f"bbq_average: {bbq_average}, number of subtasks: {len(bbq_list)}")

