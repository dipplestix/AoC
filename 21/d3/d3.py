import sys
import numpy as np


def count_inc(file_name):
    counts = None
    counter = 0
    with open(file_name, 'r') as f:
        for val in f:
            vals = list(val)
            vals = vals[:-1]
            if counts is None:
                counts = np.zeros(len(vals))
            for i, v in enumerate(vals):
                if int(v) == 0:
                    counts[i] += 1
            counter += 1
    counts = counts/counter

    zeros = np.zeros(len(counts))
    ones = np.zeros(len(counts))
    for i, dig in enumerate(counts):
        if dig > .5:
            zeros[i] = 1
        else:
            ones[i] = 1
    zeros = zeros.dot(2**np.arange(zeros.size)[::-1])
    ones = ones.dot(2**np.arange(ones.size)[::-1])

    return zeros*ones


def life_support(file_name):
    oxygen = []
    co2 = []
    i_o = 0
    i_c = 0

    with open(file_name, 'r') as f:
        for val in f:
            vals = list(val)
            vals = vals[:-1]
            oxygen.append(vals)
            co2.append(vals)

    while len(oxygen) >1:
        count = 0
        div = len(oxygen)
        zero_keep = []
        one_keep = []
        for num in oxygen:
            cur_val = int(num[i_o])
            if cur_val == 0:
                count += 1
                zero_keep.append(num)
            else:
                one_keep.append(num)
        if count/div > .5:
            oxygen = zero_keep
        else:
            oxygen = one_keep
        i_o = (i_o + 1) % 13

    while len(co2) > 1:
        count = 0
        div = len(co2)
        zero_keep = []
        one_keep = []
        for num in co2:
            cur_val = int(num[i_c])
            if cur_val == 0:
                count += 1
                zero_keep.append(num)
            else:
                one_keep.append(num)
        if count/div > .5:
            co2 = one_keep
        else:
            co2 = zero_keep
        i_c = (i_c + 1) % 13

    oxygen = [int(c) for c in oxygen[0]]
    co2 = [int(c) for c in co2[0]]

    oxygen = np.array(oxygen)
    co2 = np.array(co2)

    o = oxygen.dot(2**np.arange(oxygen.size)[::-1])
    c = co2.dot(2**np.arange(co2.size)[::-1])

    return o*c


if __name__ == "__main__":
    gamma_delta = count_inc(sys.argv[1])
    print(gamma_delta)
    o_c = life_support(sys.argv[1])
    print(o_c)
