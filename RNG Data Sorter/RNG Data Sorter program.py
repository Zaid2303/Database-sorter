import random # For random num Generator
import time # to calculate time taken
import pandas as pd # to get information to generate graph
import matplotlib.pyplot as plt # generated graph as a image

# Function to generate random arrays
def generateRandomArray(size):
    return [random.randint(100000, 999999) for _ in range(size)]

# ---------- Sorting algorithms ----------

# Selection Sort Algorithm
def selectionSort(arr):
    comparisons = 0 # set comparrison to 0 when function called
    n = len(arr) # array length being used
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            comparisons += 1 # everytime a comparrison is made comparrison counter increased by 1
            if arr[j] < arr[minIndex]: # calculating the time
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return comparisons # returns number of comparrisons

# Merge Sort Algorithm
def mergeSort(arr):
    comparisons = 0 # set comparrison to 0 when function called
    if len(arr) > 1: # array length being used
        mid = len(arr) // 2 # array split in middle
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        # comparisons for both halves
        comparisons += mergeSort(leftHalf) # array called for each half being split up so it is looped
        comparisons += mergeSort(rightHalf)

        i = j = k = 0
        # i = left half comparison
        # j = right half comparrison
        # k = amount of items in new sorted array

        while i < len(leftHalf) and j < len(rightHalf): # checking which half to check left side or right
            comparisons += 1
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

    return comparisons

# Quick Sort Algorithm
def quickSort(arr):
    comparisons = 0 # set comparrison to 0 when function called
    if len(arr) <= 1: # check to make sure array size is more than 1 because doesnt need sorting
        return comparisons
    pivot = arr[len(arr) // 2] # splitting array in half
    left = [x for x in arr if x < pivot] # check if pivot goes into left half of split array
    middle = [x for x in arr if x == pivot] # check if pivot goes into middle of split array
    right = [x for x in arr if x > pivot] # check if pivot goes into right half of split array
    comparisons += len(arr) - len(left) - len(right)
    comparisons += quickSort(left)
    comparisons += quickSort(right)
    return comparisons

# Function that calculates time and comparison amount
def measurePerformance(algorithm, array):
    startTime = time.time() # starting a timer
    comparisons = algorithm(array) # getting the amount of comparrisons for graph use
    endTime = time.time() # stopping timer
    executionTime = (endTime - startTime) * 1000  # calcuculating time taken. Convert to milliseconds
    return executionTime, comparisons

# Function to create a line chart comparing the performance of multiple sorting algorithms
def plotMultipleAlgorithms(dataSizes, executionTimes, comparisons, algorithmNames):
    # Set up a figure for the plot with a specific size
    plt.figure(figsize=(10, 5))

    # Plot execution times in the first subplot
    plt.subplot(1, 2, 1)
    for execTimes, algorithmName in zip(executionTimes, algorithmNames):
        # Plot a line chart with data sizes on the x-axis and execution times on the y-axis
        plt.plot(dataSizes, execTimes, marker='x', label=algorithmName)

    # Set title and labels for the first subplot
    plt.title('Algorithm Performance')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (ms)')
    plt.legend()  # Display legend to identify each algorithm

    # Plot comparisons in the second subplot
    plt.subplot(1, 2, 2)
    for comps, algorithmName in zip(comparisons, algorithmNames):
        # Plot a line chart with data sizes on the x-axis and the number of comparisons on the y-axis
        plt.plot(dataSizes, comps, marker='x', label=algorithmName)

    # Set title and labels for the second subplot
    plt.title('Algorithm Comparisons')
    plt.xlabel('Array Size')
    plt.ylabel('Number of Comparisons')
    plt.legend()  # Display legend to identify each algorithm

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

# Function to run a sorting algorithm, measure its performance, and plot the results
def runAndPlotSortingAlgorithm(algorithm, array, size):
    arrayCopy = array.copy()  # Create a copy of the input array to preserve the original
    time, comparisons = measurePerformance(algorithm, arrayCopy)  # Measure algorithm performance
    return time, comparisons  # Return the execution time and number of comparisons

# Array Setup
arrayName = ["HundredList", "ThousandList", "TenThousandList"]
arraySize = [100,1000,10000]

# Create arrays
arrays = {}  # Dictionary to store arrays
for name, size in zip(arrayName, arraySize): # zip is used so that the loop can use data from both arrays
    arrays[name] = generateRandomArray(size)

# Measure and analyse performance for each sorting algorithm and dataset size
# copying each List for each type of sort
selectionArrays = {name: array.copy() for name, array in arrays.items()}
mergeArrays = {name: array.copy() for name, array in arrays.items()}
quickArrays = {name: array.copy() for name, array in arrays.items()}

#----------Calculating the time taken for each sort----------

# Selection Sort
selectionExecutionTimesAll = []
selectionComparisonsAll = []

for name, array in selectionArrays.items(): # in both arrays
    timeSelection, comparisonsSelection = measurePerformance(selectionSort, array) # calls measurePerformance function
    print(f"Selection Sort ({name}): Execution Time: {timeSelection} ms, Comparisons: {comparisonsSelection}") # the f makes all the content in the {} into a string 
    # for plotting
    selectionExecutionTimesAll.append(timeSelection) # saves time taken into array for all 3 sorts
    selectionComparisonsAll.append(comparisonsSelection) # saves all number of comparrison 
print("\n")

# Merge Sort
mergeExecutionTimesAll = []
mergeComparisonsAll = []

for name, array in mergeArrays.items():
    timeMerge, comparisonsMerge = measurePerformance(mergeSort, array)
    print(f"Merge Sort ({name}): Execution Time: {timeMerge} ms, Comparisons: {comparisonsMerge}")
    # for plotting
    mergeExecutionTimesAll.append(timeMerge)
    mergeComparisonsAll.append(comparisonsMerge)
print("\n")

# Quick Sort
quickExecutionTimesAll = []
quickComparisonsAll = []

for name, array in quickArrays.items():
    timeQuick, comparisonsQuick = measurePerformance(quickSort, array)
    print(f"Quick Sort ({name}): Execution Time: {timeQuick} ms, Comparisons: {comparisonsQuick}")
    
    quickExecutionTimesAll.append(timeQuick)
    quickComparisonsAll.append(comparisonsQuick)
print("\n")

# Run and store results
executionTimesAll = []
comparisonsAll = []

# Plot a single graph for all array sizes using pervious information
plotMultipleAlgorithms(arraySize, [selectionExecutionTimesAll, mergeExecutionTimesAll, quickExecutionTimesAll], [selectionComparisonsAll, mergeComparisonsAll, quickComparisonsAll], arrayName)

"""
----------References----------

Used For Plotting

Matplotlib.org. (2023). Available at: https://matplotlib.org/cheatsheets/_images/handout-beginner.png.
Matplotlib.org. (2023). Available at: https://matplotlib.org/cheatsheets/_images/handout-intermediate.png.
www.w3schools.com. (n.d.). Matplotlib Pyplot. [online] Available at: https://www.w3schools.com/python/matplotlib_pyplot.asp.

"""

