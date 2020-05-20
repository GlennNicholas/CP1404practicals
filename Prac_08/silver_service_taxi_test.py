from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("test", 100, 2)
    taxi.drive(18)
    print(taxi.get_fare())


main()
