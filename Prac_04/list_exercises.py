"""https://github.com/GlennNicholas/CP1404practicals"""

def main():
    numbers = []
    for x in range(5):
        enter_numbers = int(input("Enter number: "))
        numbers.append(enter_numbers)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[4]))
    print("The smallest number is {}".format(min(numbers)))
    print("The smallest number is {}".format(max(numbers)))
    total = sum(numbers)
    average = total/len(numbers)
    print('The average number is {}'.format(average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    name_input = input("Enter your name: ")

    if name_input not in usernames:
        print("Access denied")
    else:
        print("Access granted")


if __name__ == '__main__':
    main()

