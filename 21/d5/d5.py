import sys
import numpy as np


def count_vents(file_name):
    vent_dic = {}
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            line = [int(n) for n in val.replace(' -> ', ',').split(',')]
            if line[0] == line[2]:
                start = min(line[1], line[3])
                end = max(line[1], line[3])
                vent_locs = [(line[0], i) for i in range(start, end + 1)]
            elif line[1] == line[3]:
                start = min(line[0], line[2])
                end = max(line[0], line[2])
                vent_locs = [(i, line[1]) for i in range(start, end + 1)]
            else:
                vent_locs = []
            for v in vent_locs:
                try:
                    vent_dic[v] += 1
                except KeyError:
                    vent_dic[v] = 1
    return len([value for value in list(vent_dic.values()) if value >= 2])


def count_diag_vents(file_name):
    vent_dic = {}
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            line = [int(n) for n in val.replace(' -> ', ',').split(',')]
            if line[0] == line[2]:
                start = min(line[1], line[3])
                end = max(line[1], line[3])
                vent_locs = [(line[0], i) for i in range(start, end + 1)]
            elif line[1] == line[3]:
                start = min(line[0], line[2])
                end = max(line[0], line[2])
                vent_locs = [(i, line[1]) for i in range(start, end + 1)]
            elif abs(line[0] - line[2]) == abs(line[1] - line[3]):
                start_x = line[0]
                start_y = line[1]
                end_x = line[2]
                end_y = line[3]

                if start_x > end_x:
                    sep_x = -1
                else:
                    sep_x = 1
                if start_y > end_y:
                    sep_y = -1
                else:
                    sep_y = 1
                xs = list(range(start_x, end_x + sep_x, sep_x))
                ys = list(range(start_y, end_y + sep_y, sep_y))
                vent_locs = [(j, k) for j, k in zip(xs, ys)]

            else:
                vent_locs = []
            for v in vent_locs:
                try:
                    vent_dic[v] += 1
                except KeyError:
                    vent_dic[v] = 1
    return len([value for value in list(vent_dic.values()) if value >= 2])


if __name__ == "__main__":
    dangerous_count = count_vents(sys.argv[1])
    print(dangerous_count)
    with_diags = count_diag_vents(sys.argv[1])
    print(with_diags)
