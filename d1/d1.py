import sys
import numpy as np


def count_inc(file_name):
    past_val = None
    inc_count = 0

    with open(file_name, 'r') as f:
        for val in f:
            if past_val is not None:
                if val > past_val:
                    inc_count += 1
            past_val = val

    return inc_count


def count_inc_3(file_name):
    counts = np.array([0, 0, 0])
    inc_count = 0
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
                            inc_count += 1
                comp_val = sum_val
                counts[j] = 0

    return inc_count 







if __name__ == "__main__":
    incs = count_inc(sys.argv[1])
    print(incs)
    inc_count = count_inc_3(sys.argv[1])
    print(inc_count)


