import sys
import numpy as np


def simulate_fish(file_name, n_days):
    with open(file_name, 'r') as f:
        ages = f.readline().split(',')
        ages = [int(n) for n in ages]
    for i in range(n_days):
        new_fish = []
        for fish in ages:
            if fish == 0:
                new_fish.append(8)
                new_fish.append(6)
            else:
                new_fish.append(fish - 1)
        ages = new_fish
    return len(ages)


def better_count_fish(file_name, n_days):
    with open(file_name, 'r') as f:
        ages = f.readline().split(',')
        ages = [int(n) for n in ages]
    age_dic = {i: 0 for i in range(9)}
    for a in ages:
        age_dic[a] += 1
    for d in range(n_days):
        for a in range(9):
            if a == 0:
                new_fish = age_dic[a]
            else:
                age_dic[a - 1] = age_dic[a]
        age_dic[8] = new_fish
        age_dic[6] += new_fish
    return sum(age_dic.values())

if __name__ == "__main__":
    fish_in_80 = simulate_fish(sys.argv[1], 80)
    print(fish_in_80)
    fish_in_256 = better_count_fish(sys.argv[1], 256)
    print(fish_in_256)
