import sys
print("Song")
get_num = int(sys.stdin.readline().rstrip())

for value in range(get_num):

    get_sentence = sys.stdin.readline().rstrip()
    get_word = get_sentence.split(" ")

    print_str = []

    for data in get_word:

        str_temp = ''

        data_len = len(data)

        if data_len <= 20:

            for idx in range(data_len):

                now_idx = -(idx) - 1

                str_temp += data[now_idx]

            print_str.append(str_temp)

    if len(get_sentence) <= 1000 : print(" ".join(print_str))
