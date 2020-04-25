"""https://github.com/GlennNicholas/CP1404practicals"""


def main():
    email_to_name = {}
    email = input("Enter your email:")
    while email != "":
        name = name_from_email(email)
        confirm = input("is your name " + name + "(Y/N)?")
        if confirm.upper() == "Y":
            for email in email_to_name.items():
                print("{} ({})".format(name, email))
        elif confirm.upper() == "N":
            name = input("Enter your name: ")
            email_to_name[email] = name
            email = input("Enter your email:")


def name_from_email(email):
    at_sign = email.split('@')[0]
    split_at = at_sign.split('.')
    name = ' '.join(split_at).title()
    return name


if __name__ == '__main__':
    main()
