# Diamond Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for _ in range(rows - i):
        print(" ", end=" ")
    for _ in range(2 * i - 1):
        print("*", end=" ")
    print()  

print("\n")

for i in range(rows):
    for _ in range(i):
        print(" ",end=" ")
    for _ in range(2 *(rows-i) -1):
        print("*",end=" ")
    print()