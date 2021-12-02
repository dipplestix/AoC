import sys


def calc_wrapping(input_file):
    total = 0

    with open(input_file, 'r') as f:
        for dim in f:
            dims = [int(d) for d in dim.split('x')]
            sides = [dims[0]*dims[1], dims[0]*dims[2], dims[1]*dims[2]]
            total += 2*sum(sides) + min(sides)

    return total


def calc_ribbon(input_file):
    total = 0

    with open(input_file, 'r') as f:
        for dim in f:
            dims = [int(d) for d in dim.split('x')]
            sides = [dims[0]+dims[1], dims[0]+dims[2], dims[1]+dims[2]]
            vol = dims[0]*dims[1]*dims[2]
            total += 2*min(sides) + vol

    return total


if __name__ == "__main__":
    print(calc_wrapping(sys.argv[1]))
    print(calc_ribbon(sys.argv[1]))
