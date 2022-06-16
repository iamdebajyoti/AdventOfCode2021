with open(r"C:\DEB_CloudData\my_git_repos\Python\AdventOfCode\Day 7 input.txt", 'r') as crab_pos:
    crab_pos_list = crab_pos.read()
    crab_pos_list = crab_pos_list.strip('\n')
    crab_pos_list = crab_pos_list.split(',')
    # print(crab_pos_list, type(crab_pos_list))

crab_pos_list = [int(i) for i in crab_pos_list]

# [print(type(i)) for i in crab_pos_list]
    

num_of_crabs = len(crab_pos_list)
print(num_of_crabs)
max_horz_pos_of_crab = max(crab_pos_list)
print(max_horz_pos_of_crab)

fuel_cost_per_move = 0
fuel_cost_tot = 0
pos_cumm_cost_dict = dict()

for h in range(0, max_horz_pos_of_crab, 1):
    for xx in crab_pos_list:
        fuel_cost_per_move = abs(xx - h)
        fuel_cost_tot = fuel_cost_tot+ fuel_cost_per_move
    pos_cumm_cost_dict[h] = fuel_cost_tot

min_cost = min(pos_cumm_cost_dict.values())
for items in pos_cumm_cost_dict.items():
    if items[1] == min_cost:
        print(items)
