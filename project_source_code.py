import time
import random
import math
import copy

# FUNCTIONS
# all algorithms with starting index 0


def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def parent(i):
    return math.floor(i/2)

# for starting index 0


def left(i):
    return 2*i + 1


def right(i):
    return (2*i) + 2


def max_heapify(A, i, n, heap_size):
    n = heap_size
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n, heap_size)


def build_max_heap(A, n, heap_size):
    # downto 0 included
    for i in range(math.floor(n/2), -1, -1):
        max_heapify(A, i, n, heap_size)


def heapsort(A):
    n = heap_size = len(A)
    build_max_heap(A, n, heap_size)
    # down to 2, 1 is not included
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, n, heap_size)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p-1, r-1)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:  # i > k
        return randomized_select(A, q+1, r, i-k)


# returns an array of 5 different arrays each of length n
def fill_arrays(n):
    lists_holder = []
    for j in range(5):
        array = []
        for i in range(n):
            array.append(random.randint(0, 30000))
        lists_holder.append(array)
    return lists_holder


def main():
    # # used for testing with smaller arrays
    # A = [19, 6, 2, 1, 15, 12, 17, 8, 25, 16, 40]
    # B = [19, 6, 2, 1, 15, 12, 17, 8, 25, 16, 40]
    # C = [19, 6, 2, 1, 15, 12, 17, 8, 25, 16, 40]
    # # if we want 6 order statistic, then we substract 1 because of starting index 0
    # i = 6
    # answer = insertion_sort(A, i-1)
    # print(f"\nInsertion Sort Array: {A}, {i}th order statistic is {answer}")
    # answer2 = heapsort(B, i-1)
    # print(f"\nHeapSort Array: {B}, {i}th order statistic is {answer2}")
    # answer3 = randomized_select(A, 1, len(C), i-1)
    # print(f"\nRandomized Select: The {i}th order statistic is {answer3}")

    # array that contains 1000 to 10000 size of each array
    numbers = [(m * (10**3)) for m in range(1, 11)]
    # print(numbers)

    # this dictionary will hold all arrays, the key of dictionary is the length of arrays, 1000 to 10000
    arrays_holder_dict = {}
    # just to test, running time of filling the dictionary with arrays
    start = time.perf_counter()
    for j in numbers:
        arrays_holder_dict[j] = fill_arrays(j)
    end = time.perf_counter()
    print(f"\nThe time to fill arrays is {(end-start):0.2f} seconds\n")

    # deep copy is needed, since we want the 3 of them to be equal for comparison
    A1 = copy.deepcopy(arrays_holder_dict)
    A2 = copy.deepcopy(arrays_holder_dict)
    A3 = copy.deepcopy(arrays_holder_dict)

    print("Insertion Sort Algorithm:")
    for key in A1:
        # we substract 1, since arrays here start at 0. 5th order statistic for example in this array A[1,2,3,4,5,6] is at index A[5-1] = A[4]
        i = math.floor((2*key)/3) - 1
        sum_seconds = 0
        for m in range(len(A1[key])):
            # starts counter
            timer_start = time.perf_counter()
            insertion_sort(A1[key][m])
            # print(A1[key][m][i])
            # ends counter
            timer_end = time.perf_counter()
            sum_seconds += (timer_end - timer_start)
        avg = (sum_seconds / 5)
        print(
            f"for n = {key}, avg time is {avg:.4f} seconds, or {(avg*1000):.2f} miliseconds")

    print("\nHeap-Sort Select Algorithm:")
    for key in A2:
        i = math.floor((2*key)/3) - 1
        sum_seconds = 0
        for m in range(len(A2[key])):
            timer_start = time.perf_counter()
            heapsort(A2[key][m])
            # print(A2[key][m][i])
            timer_end = time.perf_counter()
            sum_seconds += (timer_end - timer_start)
        avg = (sum_seconds / 5)
        print(
            f"for n = {key}, avg time is {avg:.4f} seconds, or {(avg*1000):.2f} miliseconds")

    print("\nRandomized Select Algorithm:")
    for key in A3:
        i = math.floor((2*key)/3) - 1
        sum_seconds = 0
        for m in range(len(A1[key])):
            timer_start = time.perf_counter()
            answer = randomized_select(
                A3[key][m], 1, key, i - 1)
            # print(answer)
            timer_end = time.perf_counter()
            sum_seconds += (timer_end - timer_start)
        avg = (sum_seconds / 5)
        print(
            f"for n = {key}, avg time is {avg:.4f} seconds, or {(avg*1000):.2f} miliseconds")

    # this is to check if arrays are sorted
    # choice = input(
    #     "\nWould you like to see if Insertion and Heapsort arrays are sorted and equal? Will show first 15 values for each array (Y or N): ")
    # if(choice == 'y' or choice == 'Y'):
    #     print("\nInsertion Array:\n")
    #     for key in A1:
    #         print(f"\nArrays with {key} values")
    #         for n in range(5):
    #             print(A1[key][n][:15])
    #     print("\nHeap-Sort Array:\n")
    #     for key in A2:
    #         print(f"\nArrays with {key} values")
    #         for n in range(5):
    #             print(A1[key][n][:15])


main()
