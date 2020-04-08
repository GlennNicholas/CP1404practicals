# https://github.com/GlennNicholas/CP1404practicals


def main():

    score = float(input("Enter score: "))
    print(score_status(score))


def score_status(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


main()

