import sys


def num_segments(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            nums = val.split('|')[1].split()
            for len_segments in [len(x) for x in nums]:
                if len_segments == 2 or len_segments == 4 or len_segments == 3 or len_segments == 7:
                    count += 1
    return count


def translate_segments(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for i, line in enumerate(f):
            seq_dic = {}
            five_len = []
            six_len = []
            sequences = line.split('|')[0].split()
            outputs = line.split('|')[1].split()

            for val in sequences:
                val = ''.join(sorted(val))
                if len(val) == 2:
                    seq_dic[1] = val
                if len(val) == 3:
                    seq_dic[7] = val
                if len(val) == 4:
                    seq_dic[4] = val
                if len(val) == 7:
                    seq_dic[8] = val
                if len(val) == 5:
                    five_len.append(val)
                if len(val) == 6:
                    six_len.append(val)
            for sixl in six_len:
                in_four = 0
                in_one = 0
                for letter in sixl:
                    if letter in seq_dic[4]:
                        in_four += 1
                    if letter in seq_dic[1]:
                        in_one += 1
                if in_four == 4:
                    seq_dic[9] = sixl
                elif in_one == 2:
                    seq_dic[0] = sixl
                else:
                    seq_dic[6] = sixl

            for fivel in five_len:
                in_one = 0
                in_nine = 0
                for letter in fivel:
                    if letter in seq_dic[1]:
                        in_one += 1
                    if letter in seq_dic[9]:
                        in_nine += 1
                if in_one == 2:
                    seq_dic[3] = fivel
                elif in_nine == 5:
                    seq_dic[5] = fivel
                else:
                    seq_dic[2] = fivel
            inv_map = {v: k for k, v in seq_dic.items()}

            for k, o in enumerate(outputs):
                o = ''.join(sorted(o))
                count += inv_map[o]*10**(3-k)
    return count


if __name__ == "__main__":
    segment_count = num_segments(sys.argv[1])
    print(segment_count)
    total_val = translate_segments(sys.argv[1])
    print(total_val)
