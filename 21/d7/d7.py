import sys
import numpy as np


def find_best_spot(file_name):
    with open(file_name, 'r') as f:
        locations = f.readline().split(',')
        locations = [int(n) for n in locations]
    loc_dic = {}
    best = np.inf
    best_spot = None
    max_loc = 0
    for i in locations:
        if i > max_loc:
            max_loc = i
        try:
            loc_dic[i] += 1
        except KeyError:
            loc_dic[i] = 1

    for loc in range(max_loc):
        tot_dist = 0
        for i in loc_dic:
            tot_dist += abs(loc - i)*loc_dic[i]
        if tot_dist < best:
            best = tot_dist
            best_spot = loc

    return best


def find_best_spot_harder(file_name):
    with open(file_name, 'r') as f:
        locations = f.readline().split(',')
        locations = [int(n) for n in locations]
    loc_dic = {}
    best = np.inf
    best_spot = None
    max_loc = 0
    for i in locations:
        if i > max_loc:
            max_loc = i
        try:
            loc_dic[i] += 1
        except KeyError:
            loc_dic[i] = 1

    for loc in range(max_loc):
        tot_dist = 0
        for i in loc_dic:
            dis = abs(loc - i)
            tot_dist += dis*(dis + 1)/2*loc_dic[i]
        if tot_dist < best:
            best = tot_dist
            best_spot = loc
    return best


if __name__ == "__main__":
    best_crab_spot = find_best_spot(sys.argv[1])
    print(best_crab_spot)
    best_crab_spot2 = find_best_spot_harder(sys.argv[1])
    print(best_crab_spot2)
