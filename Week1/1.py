# Lower Triangle

rows = int(input("Enter Rows:"))

for i in range(1,rows+1):
    for _ in range(1,i+1):
        print("*", end=" ")
    print()

print("\n")

for i in range(1, rows + 1):
    for _ in range(rows - i):
        print(" ", end=" ")
    for _ in range(i):
        print("*", end=" ")
    print()