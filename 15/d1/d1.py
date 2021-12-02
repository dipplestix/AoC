import sys


def find_floor(file_name):
    cur_floor = 0
    with open(file_name, 'r') as f:
        directions = f.readline()
        directions = list(directions)
        for d in directions:
            if d == '(':
                cur_floor += 1
            elif d == ')':
                cur_floor -= 1

    return cur_floor



def find_threshold(file_name):
    cur_floor = 0
    basement = False
    with open(file_name, 'r') as f:
        directions = f.readline()
        directions = list(directions)
        for i, d in enumerate(directions):
            if d == '(':
                cur_floor += 1
            elif d == ')':
                cur_floor -= 1
            if not basement and cur_floor == -1:
                basement = True
                base_floor = i+1
            

    return base_floor


if __name__ == "__main__":
    print(find_floor(sys.argv[1]))
    print(find_threshold(sys.argv[1]))
