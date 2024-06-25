# Stanley Zhao
# May 30 2024
# CS 5800 Algorithms

# Median finding algorithm that uses the selection algorithm
# to find the median of an array
# The selection algorithm is a divide and conquer algorithm

import random
import time


def swap( a, i, j ):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return


# Given a list of numbers a
# Given an index containing the value on which to split the array
# Modifies the array in place so that it contains, in order
#   p values < a[index]
#   q values == a[index]
#   r values > a[index]
# The function returns (p, q, r)
def split(a, index):
   # special case arrays of length 0 and 1 (shouldn't occur, but...)
    if len(a) == 0:
        return (0, 0, 0)
    
    if len(a) == 1:
        return (0, 1, 0)
    
    p = 0
    q = 1
    r = 0

    # swap a[index] with a[0]
    swap( a, index, 0)

    value = a[0]
    left = 1 # pointer to unchecked values <= v
    right = len(a)-1 # pointer to uncheck values > v

    # special case for an array of length 2
    if len(a) == 2:
        if a[left] < value:
            swap( a, 0, left )
            return (1, 1, 0)
        elif a[left] == value:
            return (0, 2, 0)
        else:
            return (0, 1, 1)

    # O(n) time
    while left < right:

        # move the left pointer right until we find a value > v or it meets right
        while left <= right:
            if a[left] <= value:
                left += 1 # move to the next location
                p += 1    # increase the number of items < v
            else: # a[left] > value
                break

        # move the right pointer left until we find a value < v or it meets left
        while left < right:
            if a[right] > value:
                right -= 1 # move pointer left
                r += 1     # increase the number of items > v
            else: # the value is <= v
                break

        if left < right: # do a swap
            swap( a, left, right )


    # value in position 0
    # p values from index 1 to index p <= v
    # q values from index p+1 to end > v

    swap( a, 0, p ) # put the value v in between left right groups

    # get any other values in the left group that are = v
    left = 0
    # O(n) time, at most searches n-1 items
    while left < p:
        if a[left] == value:
            swap( a, left, p-1 )
            p -= 1 # subtract from group < v
            q += 1 # add to group == v
            left -= 1 # keep left where it is incase the value swapped in is = v
        left += 1

    # return the number of things in the three groups <, =, >
    return (p, q, r)


def selection_random(a, k):
    if len(a) == 1:
        return a[0]

    index = random.randint(0, len(a) - 1)
    p, q, r = split(a, index)

    if k < p:
        return selection_random(a[:p], k)
    elif k < p + q:
        return a[p]
    else:
        return selection_random(a[p+q:], k - (p + q))


def selection_alternative(a, k):
    if len(a) == 1:
        return a[0]

    point1 = random.randint(0, len(a) - 1)
    point2 = random.randint(0, len(a) - 1)
    point3 = random.randint(0, len(a) - 1)
    median_of_three = sorted([point1, point2, point3])[1]
    p, q, r = split(a, median_of_three)

    if k < p:
        return selection_alternative(a[:p], k)
    elif k < p + q:
        return a[p]
    else:
        return selection_alternative(a[p+q:], k - (p + q))


def main():
    a = [random.randint(1, 100) for _ in range(7)]
    print("HW#3: Median Split")
    print("array:", a)
    print("median using random split point:", selection_random(a[:], len(a) // 2))
    print("median using alternative split point:", selection_alternative(a[:], len(a) // 2))
    print("The median obtained by sorting the array:", sorted(a)[len(a) // 2])

    print("Timing the three methods for different magnitudes of input:")
    print("N = 10000:")
    a = [random.randint(1, 100) for i in range(10000)]
    start = time.time()
    selection_random(a, len(a) // 2)
    print("Time for random split:", time.time() - start)
    
    start = time.time()
    selection_alternative(a, len(a) // 2)
    print("Time for alternative split:", time.time() - start)

    start = time.time()
    sorted(a)[len(a) // 2]
    print("Time for sorting:", time.time() - start)

    print("N = 100000:")
    a = [random.randint(1, 100) for i in range(100000)]
    start = time.time()
    selection_random(a, len(a) // 2)
    print("Time for random split:", time.time() - start)

    start = time.time()
    selection_alternative(a, len(a) // 2)
    print("Time for alternative split:", time.time() - start)

    start = time.time()
    sorted(a)[len(a) // 2]
    print("Time for sorting:", time.time() - start)

    print("N = 1000000:")
    a = [random.randint(1, 100) for i in range(1000000)]
    start = time.time()
    selection_random(a, len(a) // 2)
    print("Time for random split:", time.time() - start)

    start = time.time()
    selection_alternative(a, len(a) // 2)
    print("Time for alternative split:", time.time() - start)

    start = time.time()
    sorted(a)[len(a) // 2]
    print("Time for sorting:", time.time() - start)


if __name__ == "__main__":
    main()
