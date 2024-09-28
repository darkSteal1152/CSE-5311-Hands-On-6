import random

def random_quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        random_quicksort(arr, p, q - 1)
        random_quicksort(arr, q + 1, r)

def partition(arr, p, r):
    pivot_index = random.randint(p, r)
    pivot = arr[pivot_index]

    temp = arr[pivot_index]
    arr[pivot_index] = arr[r]
    arr[r] = temp

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

n = 10
arr = [random.randint(0, 100) for _ in range(n)]
print(arr)
random_quicksort(arr, 0, len(arr) - 1)
print(arr)
