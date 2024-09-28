import random
import time
import matplotlib.pyplot as plt

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)

def partition(arr, p, r):
    pivot_index = r
    pivot = arr[pivot_index]

    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp

    return i + 1

def unsort_array(arr):
    # Base case: if the array has 0 or 1 element, return it as-is
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid_index = len(arr) // 2
    # Get the middle element
    middle = arr[mid_index]
    # Remove the middle element from the array
    arr = arr[:mid_index] + arr[mid_index+1:]

    # Split into two subarrays
    min_subarray = arr[:len(arr) // 2]  # First half
    max_subarray = arr[len(arr) // 2:]  # Second half

    # Recursively apply the process to the min and max subarrays
    min_result = unsort_array(min_subarray)
    max_result = unsort_array(max_subarray)

    # Return the result by placing the middle element at the end
    return min_result + max_result + [middle]

def generate_best_case(n):
    arr = [i for i in range(1, n + 1)]

    unsorted_arr = unsort_array(arr)

    return unsorted_arr

def generate_worst_case(n):
    return list(range(n))

def generate_average_case(n):
    return [random.randint(0, 10000) for i in range(n)]

def measure_runtime(quicksort_func, generate_input_func, n_values):
    runtimes = []
    for n in n_values:
        arr = generate_input_func(n)
        start_time = time.time()
        quicksort_func(arr, 0, len(arr) - 1)
        end_time = time.time()
        runtimes.append(end_time - start_time)
    return runtimes

n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900]

best_case_runtimes = measure_runtime(quicksort, generate_best_case, n_values)
worst_case_runtimes = measure_runtime(quicksort, generate_worst_case, n_values)
average_case_runtimes = measure_runtime(quicksort, generate_average_case, n_values)

plt.figure(figsize=(10, 6))
plt.plot(n_values, best_case_runtimes, label="Best Case (Sorted Input)", marker='o')
plt.plot(n_values, worst_case_runtimes, label="Worst Case (Reverse Sorted Input)", marker='o')
plt.plot(n_values, average_case_runtimes, label="Average Case (Random Input)", marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Quicksort Runtime Analysis')
plt.legend()
plt.grid(True)
plt.show()
