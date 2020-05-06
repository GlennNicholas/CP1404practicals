from Prac_06.guitar import Guitar


def main():

    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name == "":
        name = input("Name: ")
    year = input("Year: ")
    while year == "":
        year = input("Year: ")
    Cost = input("Cost: ")
    while Cost == "":
        Cost = input("Cost: ")

    add_guitars = Guitar(name, year, Cost)
    guitars.append(add_guitars)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                 {2}".format(i + 1, guitar, vintage_string))


main()
