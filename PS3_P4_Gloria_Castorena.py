numMin = int(input("Enter the minimum number for the multiplication table: "))
numMax = int(input("Enter the maximum number for the multiplication table: "))

for i in range(numMin, numMax + 1):
    for j in range(numMin, numMax + 1):
        if j > i:
            print("*\t", end='')
        else:
            answer = i * j
            print(str(answer) + "\t", end='')
    print()