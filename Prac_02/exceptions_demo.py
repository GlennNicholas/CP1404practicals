try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# Ans - ValueError will occur only when the input is a string or a float.
# When will a ZeroDivisionError occur?
# Ans - ZeroDivisionError will occur when the input for denominator is 0
# Could you change the code to avoid the possibility of a ZeroDivisionError?
