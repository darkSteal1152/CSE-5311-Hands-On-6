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
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    middle = arr[mid_index]
    arr = arr[:mid_index] + arr[mid_index+1:]

    min_subarray = arr[:len(arr) // 2]  # First half
    max_subarray = arr[len(arr) // 2:]  # Second half

    min_result = unsort_array(min_subarray)
    max_result = unsort_array(max_subarray)

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

#def quicksort(arr, p, r):          // Expressed as 2T(n / 2) + O(partition)
#    if p < r:                      // O(1) per call
#        q = partition(arr, p, r)   //
#        quicksort(arr, p, q - 1)   // average case results in T(n / 2)
#        quicksort(arr, q + 1, r)   // average case results in T(n / 2)

#def partition(arr, p, r):          // Dominated by O(n)
#    pivot_index = r                // O(1)
#    pivot = arr[pivot_index]       // O(1)

#    i = p - 1                      // O(1)
#   for j in range(p, r):           // worst case is O(n -1)
#        if arr[j] <= pivot:        // O(1)
#            i += 1                 // O(1)
#            temp = arr[i]          // swap is O(1)
#            arr[i] = arr[j]
#            arr[j] = temp

#    temp = arr[i + 1]              // swap is O(1)
#    arr[i + 1] = arr[r]
#    arr[r] = temp

#    return i + 1                   // O(1)

# Complete Complexity is 2T(n / 2) + O(n)
# relation corresponds to   O(nlogn) at average case
#                           O(n^2) at worst case
