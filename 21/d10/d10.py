import sys


def find_cor(file_name):
    score = 0
    points = {'>': 25137, ')': 3, '}': 1197, ']': 57}
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            expected = []
            for char in val[:-1]:
                if char == '(':
                    expected.append(')')
                elif char == '[':
                    expected.append(']')
                elif char == '{':
                    expected.append('}')
                elif char == '<':
                    expected.append('>')
                elif char == expected[-1]:
                    expected.pop(-1)
                else:
                    score += points[char]
                    break
    return score


def find_inc(file_name):
    scores = []
    points = {'>': 4, ')': 1, '}': 3, ']': 2}
    with open(file_name, 'r') as f:
        for i, val in enumerate(f):
            cor = False
            loop_score = 0
            expected = []
            for char in val[:-1]:
                if char == '(':
                    expected.append(')')
                elif char == '[':
                    expected.append(']')
                elif char == '{':
                    expected.append('}')
                elif char == '<':
                    expected.append('>')
                elif char == expected[-1]:
                    expected.pop(-1)
                elif char != expected[-1]:
                    cor = True
                    break
            if expected and not cor:
                expected.reverse()
                for char in expected:
                    loop_score = loop_score*5
                    loop_score += points[char]
                scores.append(loop_score)
    scores.sort()
    return scores[int((len(scores) - 1)/2)]


if __name__ == "__main__":
    cor_score = find_cor(sys.argv[1])
    print(cor_score)
    inc_score = find_inc(sys.argv[1])
    print(inc_score)
