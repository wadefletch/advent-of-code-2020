def solution(input, dx, dy):
    # minus 1 to remove newline character at the end
    line_length = len(input[0]) - 1

    trees = 0

    for i, line in enumerate(input):
        if i % dy != 0:
            continue
        
        y = i // dy 
        x = (y * dx) % line_length
       
        if line[x] == '#':
            trees += 1

    return trees

if __name__ in '__main__':
    input = open('input.txt').readlines()

    print(solution(input, 3, 1))
    print(solution(input, 1, 1) * solution(input, 3, 1) * solution(input, 5, 1) * solution(input, 7, 1) * solution(input, 1, 2))

