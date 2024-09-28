# CSE-5311-Hands-On-6
CSE 5311 Assignment 6

1. Random Quicksort is implemented in random_quicksort.py
2. Non-Random Quicksort is implemented in non_quicksort.py
3. Benchmarks are written in non_quicksort.py for the following
4.   Best case, when the array is given such that it splits into two near equal subarrays
5.   Ive done this by having an ordered array and recursivly taking the middle element to the end
6.   This implementation is done in the unsort_array method
7.   Worst case, when the array is already sorted, though reverse sort and duplicative arrays also work
8.   Average case, random numbered array
9. The Benchmark is shown in Figure 10
10.   The worst case is exponential almost like O(n^2)
11.   The best and average case are near similar at O(nlogn)
12. The Time complexity calculations are shown at the end of non_quicksort.py
13.   T(n) is O(n^2) for worst case, and O(nlogn) for average case
