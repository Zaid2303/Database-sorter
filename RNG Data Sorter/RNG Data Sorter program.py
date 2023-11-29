import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate random arrays
def generate_random_array(size):
    return [random.randint(100000, 999999) for _ in range(size)]

# Sorting algorithms

# Selection Sort Algorithm
def selection_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comparisons

# Merge Sort Algorithm
def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        comparisons += merge_sort(left_half)
        comparisons += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparisons += 1
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

    return comparisons

# Quick Sort Algorithm
def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return comparisons
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    comparisons += len(arr) - len(left) - len(right)
    comparisons += quick_sort(left)
    comparisons += quick_sort(right)
    return comparisons

# Function that calculates time and comparison amount
def measure_performance(algorithm, array):
    start_time = time.time()
    comparisons = algorithm(array)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return execution_time, comparisons

# Create arrays
HundredList = generate_random_array(100)
ThousandList = generate_random_array(1000)
TenThousandList = generate_random_array(10000)

# Measure and analyze performance for each sorting algorithm and dataset size
HundredList_selection = HundredList.copy()
ThousandList_selection = ThousandList.copy()
TenThousandList_selection = TenThousandList.copy()

HundredList_merge = HundredList.copy()
ThousandList_merge = ThousandList.copy()
TenThousandList_merge = TenThousandList.copy()

HundredList_quick = HundredList.copy()
ThousandList_quick = ThousandList.copy()
TenThousandList_quick = TenThousandList.copy()

# Selection Sort
time_selection, comparisons_selection = measure_performance(selection_sort, HundredList_selection)
print(f"Selection Sort (HundredList): Execution Time: {time_selection} ms, Comparisons: {comparisons_selection}")

time_selection, comparisons_selection = measure_performance(selection_sort, ThousandList_selection)
print(f"Selection Sort (ThousandList): Execution Time: {time_selection} ms, Comparisons: {comparisons_selection}")

time_selection, comparisons_selection = measure_performance(selection_sort, TenThousandList_selection)
print(f"Selection Sort (TenThousandList): Execution Time: {time_selection} ms, Comparisons: {comparisons_selection}")

print ("")

# Merge Sort
time_merge, comparisons_merge = measure_performance(merge_sort, HundredList_merge)
print(f"Merge Sort (HundredList): Execution Time: {time_merge} ms, Comparisons: {comparisons_merge}")

time_merge, comparisons_merge = measure_performance(merge_sort, ThousandList_merge)
print(f"Merge Sort (ThousandList): Execution Time: {time_merge} ms, Comparisons: {comparisons_merge}")

time_merge, comparisons_merge = measure_performance(merge_sort, TenThousandList_merge)
print(f"Merge Sort (TenThousandList): Execution Time: {time_merge} ms, Comparisons: {comparisons_merge}")

print ("")

# Quick Sort
time_quick, comparisons_quick = measure_performance(quick_sort, HundredList_quick)
print(f"Quick Sort (HundredList): Execution Time: {time_quick} ms, Comparisons: {comparisons_quick}")

time_quick, comparisons_quick = measure_performance(quick_sort, ThousandList_quick)
print(f"Quick Sort (ThousandList): Execution Time: {time_quick} ms, Comparisons: {comparisons_quick}")

time_quick, comparisons_quick = measure_performance(quick_sort, TenThousandList_quick)
print(f"Quick Sort (TenThousandList): Execution Time: {time_quick} ms, Comparisons: {comparisons_quick}")

print ("")
print ("")

# Function to create line chart for multiple algorithms
def plot_multiple_algorithms(data_sizes, execution_times, comparisons, algorithm_names):
    plt.figure(figsize=(10, 5))

    # Plot execution times
    plt.subplot(1, 2, 1)
    for exec_times, algorithm_name in zip(execution_times, algorithm_names):
        plt.plot(data_sizes, exec_times, marker='x', label=algorithm_name)
    plt.title('Algorithm Performance')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (ms)')
    plt.legend()

    # Plot comparisons
    plt.subplot(1, 2, 2)
    for comps, algorithm_name in zip(comparisons, algorithm_names):
        plt.plot(data_sizes, comps, marker='x', label=algorithm_name)
    plt.title('Algorithm Comparisons')
    plt.xlabel('Array Size')
    plt.ylabel('Number of Comparisons')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Function to run and plot sorting algorithm
def run_and_plot_sorting_algorithm(algorithm, array, size):
    array_copy = array.copy()
    time, comparisons = measure_performance(algorithm, array_copy)
    return time, comparisons

# Run and store results
execution_times_all = []
comparisons_all = []
for size in data_sizes:
    execution_times = []
    comparisons = []
    for algorithm, algorithm_name in zip(algorithms, algorithm_names):
        array = generate_random_array(size)
        exec_time, comparison = run_and_plot_sorting_algorithm(algorithm, array, size)
        execution_times.append(exec_time)
        comparisons.append(comparison)

        # Print results for the current algorithm and array size
        print(f"{algorithm_name} ({size} elements): Execution Time: {exec_time} ms, Comparisons: {comparison}")

    # Append results for the current array size
    execution_times_all.append(execution_times)
    comparisons_all.append(comparisons)

# Plot a single graph for all array sizes
plot_multiple_algorithms(data_sizes, execution_times_all, comparisons_all, algorithm_names)
