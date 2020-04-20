"""https://github.com/GlennNicholas/CP1404practicals"""


def main():
    word_to_count = {}
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    for sentence in words:  # LBYL method
        if sentence in word_to_count:
            word_to_count[sentence] += 1
        else:
            word_to_count[sentence] = 1

    max_length = max((len(sentence) for sentence in words))
    for sentence in words:
        print("{:{}} : {}".format(sentence, max_length, word_to_count[sentence]))


if __name__ == '__main__':
    main()

