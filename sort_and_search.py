list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return arr

print("Original list:")
print(list)

target = 9
found_index = linear_search(list, target)
print(f"\nLinear Search: Number {target} found at index {found_index} (in unsorted list)")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

sorted_list = list.copy()
insertion_sort(sorted_list)

print("\nList after Insertion Sort:")
print(sorted_list)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

binary_search_index = binary_search(sorted_list, target)
print(f"\nBinary Search: Number {target} found at index {binary_search_index} (in sorted list)")


