import sys
import numpy as np


def find_mins(file_name):
    risk_level = 0
    rows = []
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            row = [int(n) for n in val if n!='\n']
            rows.append(row)
    rows = np.array(rows)
    num_rows = len(rows)
    num_cols = len(rows[0])
    for j, row in enumerate(rows):
        for k, val in enumerate(row):
            low_point = True
            if k != 0:
                if rows[j][k - 1] <= val:
                    low_point = False
            if (k + 1) != num_cols:
                if rows[j][k + 1] <= val:
                    low_point = False
            if j != 0:
                if rows[j - 1][k] <= val:
                    low_point = False
            if (j + 1) != num_rows:
                if rows[j + 1][k] <= val:
                    low_point = False
            if low_point:
                risk_level += 1 + val
    return risk_level


def find_basins(file_name):
    basins = [0, 0, 0]

    rows = []
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            row = [int(n) for n in val if n!='\n']
            rows.append(row)
    rows = np.array(rows)
    num_rows = len(rows)
    num_cols = len(rows[0])
    for j, row in enumerate(rows):
        for k, val in enumerate(row):
            low_point = True
            if k != 0:
                if rows[j][k - 1] <= val:
                    low_point = False
            if (k + 1) != num_cols:
                if rows[j][k + 1] <= val:
                    low_point = False
            if j != 0:
                if rows[j - 1][k] <= val:
                    low_point = False
            if (j + 1) != num_rows:
                if rows[j + 1][k] <= val:
                    low_point = False
            if low_point:
                search_directions = [(j - 1, k, val), (j + 1, k, val), (j, k - 1, val), (j, k + 1, val)]
                assigned = [(j, k)]
                size = 1
                while search_directions:
                    new_search = search_directions.pop()
                    r = new_search[0]
                    c = new_search[1]
                    if 0<=r<num_rows and 0<=c<num_cols and (r, c) not in assigned:
                        v = rows[r, c]
                        if v != 9:
                            if v > new_search[2]:
                                size += 1
                                search_directions.extend([(r - 1, c, v), (r + 1, c, v), (r, c - 1, v), (r, c + 1, v)])
                                assigned.append((r, c))
                if size > min(basins):
                    basins[basins.index(min(basins))] = size
    return basins[0]*basins[1]*basins[2]


if __name__ == "__main__":
    risk = find_mins(sys.argv[1])
    print(risk)
    basin_tot = find_basins(sys.argv[1])
    print(basin_tot)
