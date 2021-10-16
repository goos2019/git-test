import sys

get_num = int(sys.stdin.readline().rstrip())

if get_num >= 1 and get_num <= 100000:

    input_stack = []
    output_stack = []
    temp_stack = []
    next_idx = 1

    for idx in range(get_num):

        input_stack.append(int(sys.stdin.readline().rstrip()))

        

        