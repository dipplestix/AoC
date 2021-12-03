import sys


def count_inc(file_name):
    with open(file_name, 'r') as f:
        loc = [0, 0]
        for val in f:
            directions = val.split()
            directions[1] = int(directions[1])
            if directions[0] == 'up':
                loc[0] -= directions[1]
            elif directions[0] == 'down':
                loc[0] += directions[1]
            elif directions[0] == 'forward':
                loc[1] += directions[1]
    return loc[0]*loc[1]


def find_loc(file_name):
    loc = [0, 0, 0]
    with open(file_name, 'r') as f:
        for val in f:
            directions = val.split()
            directions[1] = int(directions[1])
            if directions[0] == 'up':
                loc[2] -= directions[1]
            elif directions[0] == 'down':
                loc[2] += directions[1]
            elif directions[0] == 'forward':
                loc[1] += directions[1]
                loc[0] += directions[1]*loc[2]
    return loc[0]*loc[1]


if __name__ == "__main__":
    location = count_inc(sys.argv[1])
    print(location)
    location_2 = find_loc(sys.argv[1])
    print(location_2)
