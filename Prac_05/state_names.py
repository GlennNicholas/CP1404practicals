"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
"""https://github.com/GlennNicholas/CP1404practicals"""

CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)


def main():
    for state in CODE_TO_NAME:  # loop that prints all the states
        print("{} is {}".format(state, CODE_TO_NAME[state]))

    state_code = input("Enter short state: ").upper()  # input can be in both lower and uppercase
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()  # input can be in both lower and uppercase


if __name__ == '__main__':
    main()