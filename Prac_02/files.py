# Files ques 1
name_file = "name.txt"

file_name = open(name_file, "w")

name = str(input("Enter your name: "))

print(name, file=file_name)

file_name.close()

# Files ques 2
name_in_file = open(name_file, "r")

name = name_in_file.read()

print("Your name is", name)

name_in_file.close()

# Files ques 3
number_file = "numbers.txt"

number_file = open(number_file, "r")

number = int(number_file.readline())  # calling twice will return the first and second
number2 = int(number_file.readline())

number_file.close()
print(number + number2)

# Files ques 3
number_file = "numbers.txt"

number_file = open(number_file, "r")

number = int(number_file.readline())
number2 = int(number_file.readline())
number3 = int(number_file.readline())

number_file.close()
print(number + number2 + number3)








