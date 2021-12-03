import sys
import numpy as np


def count_inc(file_name):
    past_val = None

    with open(file_name, 'r') as f:
        counter = 0
        for val in f:
            if past_val is not None:
                if val > past_val:
                    counter += 1
            past_val = val

    return counter


def count_inc_3(file_name):
    counts = np.array([0, 0, 0])
    counter = 0
    comp_val = None

    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            val = int(val)
            if i == 0:
                counts[0] = val
            elif i == 1:
                counts[0] = counts[0] + val
                counts[1] = val
            else:
                counts = counts + val
                j = (i+1) % 3
                sum_val = counts[j]
                if comp_val is not None:
                    if sum_val > comp_val:
                        counter += 1
                comp_val = sum_val
                counts[j] = 0

    return counter


if __name__ == "__main__":
    incs = count_inc(sys.argv[1])
    print(incs)
    inc_count = count_inc_3(sys.argv[1])
    print(inc_count)
