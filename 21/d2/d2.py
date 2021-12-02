import sys


def count_inc(file_name):
    location = [0, 0]
    with open(file_name, 'r') as f:
        for val in f:
            directions = val.split()
            directions[1] = int(directions[1])
            if directions[0] == 'up':
                location[0] -= directions[1]
            elif directions[0] == 'down':
                location[0] += directions[1]
            elif directions[0] == 'forward':
                location[1] += directions[1]
    return location[0]*location[1]


def find_loc(file_name):
    location = [0, 0, 0]
    with open(file_name, 'r') as f:
        for val in f:
            directions = val.split()
            directions[1] = int(directions[1])
            if directions[0] == 'up':
                location[2] -= directions[1]
            elif directions[0] == 'down':
                location[2] += directions[1]
            elif directions[0] == 'forward':
                location[1] += directions[1]
                location[0] += directions[1]*location[2]
    return location[0]*location[1]


if __name__ == "__main__":
    location = count_inc(sys.argv[1])
    print(location)
    location_2 = find_loc(sys.argv[1])
    print(location_2)
