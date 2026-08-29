arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Array in ascending order:")
print(arr)