import random

# Function to generate random arrays
def generate_random_array(size):
    return [random.randint(100000, 999999) for _ in range(size)]

# Create arrays 
HundredList = generate_random_array(100) # 100 paces
ThousandList = generate_random_array(1000) # 1000 spaces
TenThousandList = generate_random_array(10000) # 10000 spaces

# Sorting algorithms
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

#merge sort 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



# creates copy of Original list with .copy for selection sort and sorts it.
HundredList_selection = HundredList.copy()
ThousandList_selection = ThousandList.copy()
TenThousandList_selection = TenThousandList.copy()

selection_sort(HundredList_selection)
selection_sort(ThousandList_selection)
selection_sort(TenThousandList_selection)

# creates copy of Original list with .copy for merge sort and sorts it.
HundredList_merge = HundredList.copy()
ThousandList_merge = ThousandList.copy()
TenThousandList_merge = TenThousandList.copy()

merge_sort(HundredList_merge)
merge_sort(ThousandList_merge)
merge_sort(TenThousandList_merge)

# creates copy of Original list with .copy for quick sort and sorts it.
HundredList_quick = HundredList.copy()
ThousandList_quick = ThousandList.copy()
TenThousandList_quick = TenThousandList.copy()

quick_sort(HundredList_quick)
quick_sort(ThousandList_quick)
quick_sort(TenThousandList_quick)

# Debug use
print (len(HundredList))
print (len(ThousandList))
print (len(TenThousandList))

print("Selection Sort:")
print(HundredList_selection[:10])  # Print the first 10 elements of the sorted array for verification
print(ThousandList_selection[:10])
print(TenThousandList_selection[:10])

print("\nMerge Sort:")
print(HundredList_merge[:10])
print(ThousandList_merge[:10])
print(TenThousandList_merge[:10])

print("\nQuick Sort:")
print(HundredList_quick[:10])
print(ThousandList_quick[:10])
print(TenThousandList_quick[:10])




