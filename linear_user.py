numbers = []
for i in range(15):
    value = int(input("Enter a number: "))
    numbers.append(value)
search = int(input("Enter the number to search: "))
found = False
for i in range(15):
    if numbers[i] == search:
        print("Number found at position", i + 1)
        found = True
        break
if found == False:
    print("Number not found")