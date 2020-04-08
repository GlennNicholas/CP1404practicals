# https://github.com/GlennNicholas/CP1404practicals

MIN_LENGTH = 2


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(MIN_LENGTH):
    password = input("Enter password of at least 8 characters")
    while len(password) < MIN_LENGTH:
        print("Password is too short")
        password = input("Enter password of at least 8 characters")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
