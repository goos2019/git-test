import sys

get_num = int(sys.stdin.readline().rstrip())

for value in range(get_num):

    get_line = sys.stdin.readline().rstrip()

    count = 0

    line_len = len(get_line)

    if line_len >= 2 and line_len <= 50:

        for idx in range(line_len):

            if count < 0:

                break

            elif get_line[idx] == '(':

                count += 1

            else:

                count -= 1

        print('YES' if count == 0 else 'NO')

