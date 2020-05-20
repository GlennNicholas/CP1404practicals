from Prac_08.car import Car
from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    bill = 0
    all_taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive \n >>>")
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxi's available:")
            taxi_display(all_taxis)
            taxi_choice = int(input("Choose taxi: "))
            final_taxi = all_taxis[taxi_choice]
            print(bill)
        elif menu_choice == "d":
            final_taxi.start_fare()
            distance = int(input("Drive how far? \n >>>"))
            final_taxi.drive(distance)
            cost = final_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(final_taxi.name, cost))
            bill += cost
            print("Bill to date: {}".format(bill))
        else:
            print("Total trip cost: {}".format(bill))


def taxi_display(all_taxis):
    for i, taxi in enumerate(all_taxis):
        print("{} - {}".format(i, taxi))


main()
