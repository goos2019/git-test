import sys

get_num = int(sys.stdin.readline().rstrip())

if (get_num <= 10000 and get_num >= 1):

    my_stack = []

    for value in range(get_num):

        get_cmd = sys.stdin.readline().rstrip().split(" ")

        cmd = get_cmd[0]

        if cmd == "push":
            my_stack.append(get_cmd[1])

        elif cmd == "pop":
            if(len(my_stack) <= 0):
                print(-1)
            else:
                print(my_stack[-1])
                my_stack.pop()

        elif cmd == "size":
            print(len(my_stack))

        elif cmd == "empty":
            if(len(my_stack) <= 0):
                print(1)
            else:
                print(0)
            
        elif cmd == "top":
            if(len(my_stack) <= 0):
                print(-1)
            else:
                print(my_stack[-1])