"""https://github.com/GlennNicholas/CP1404practicals"""

import random


def main():
    smallest_number = 1
    highest_number = 45
    quick_picks = int(input('How many quick picks?'))

    for i in range(quick_picks):
        quick_picks_list = []
        for j in range(6):
            random_number = random.randint(smallest_number, highest_number)
            while random_number in quick_picks_list:
                random_number = random.randint(smallest_number, highest_number)
            quick_picks_list.append(random_number)
        quick_picks_list.sort()
        print(" ".join("{:2}".format(random_number) for random_number in quick_picks_list))


main()
