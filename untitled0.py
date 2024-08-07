# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ib-IyS80E1tx1k6WFD8sOUb_6avciFTP
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# Bubble Sort function
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort function
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Measure execution time for sorting algorithms
def measureTime(sortFunction, arr):
    start_time = time.time()
    sortFunction(arr)
    end_time = time.time()
    return end_time - start_time

# Generate random arrays and measure sorting times
array_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
bubble_sort_times = []
selection_sort_times = []

for size in array_sizes:
    arr = np.random.randint(1, 1000, size).tolist()
    arr_copy = arr[:]

    bubble_sort_times.append(measureTime(bubbleSort, arr))
    selection_sort_times.append(measureTime(selectionSort, arr_copy))

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(array_sizes, bubble_sort_times, label='Bubble Sort', marker='o')
plt.plot(array_sizes, selection_sort_times, label='Selection Sort', marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Bubble Sort vs Selection Sort Time Complexity')
plt.legend()
plt.grid(True)
plt.show()