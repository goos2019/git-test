import sys

get_num = int(sys.stdin.readline().rstrip())

for value in range(get_num):

    get_sentence = sys.stdin.readline().rstrip()

    get_word = get_sentence.split(" ")

    max_word_len = 0

    sentence_len = len(get_sentence)

    for word in get_word:

        word_len = len(word)

        if word_len > max_word_len: max_word_len = word_len

    if sentence_len and  max_word_len <= 20:

        print_str = []

        for data in get_word:

            print_str.append(data[::-1])

        print(" ".join(print_str))
