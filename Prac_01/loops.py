for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("No. of stars: "))
for x in range(stars + 1):
    for y in range(x):
          print("*", end="")
    print("\n")




