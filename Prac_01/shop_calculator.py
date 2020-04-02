def main():
    total_price = 0

    number_item = int(input("Enter No. of items: "))

    while number_item <= 0:

        print("Invalid Input")
        
        number_item = int(input("Enter No. of items: "))

        for i in range(number_item):

            item_price = float(input("Price of item: "))

            total_price += item_price

        if total_price > 100:

            discount = 0.9 * total_price

            print('Total Price is : $' + str(discount))

        if total_price < 100:
            print("Total price is:${:.2f}".format(total_price))


main()
