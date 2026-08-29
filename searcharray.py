arr = [10, 20, 30, 40, 50]

search = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at position", i + 1)
        found = True
        break

if found == False:
    print("Element not found")