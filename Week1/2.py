# Upper Triangle

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for _ in range(i):
        print(" ", end=" ")
    for _ in range(rows-i):
        print("*", end=" ")
    print()

print("\n")

for i in range(rows,0,-1):
    for _ in range(1,i+1):
        print("*", end=" ")
    print()
