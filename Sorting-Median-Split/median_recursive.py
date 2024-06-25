# Stanley Zhao
# May 30 2024
# CS 5800 Algorithms

# A recursive version of unionkth


# important notes:
# 4 basic cases to consider, two in one group, two in the other
# returning a truncated array, the cut-off should be mid1+1 and mid2+1
# because the number at mid is guaranteed to be less than the median
# otherwise, the recursive call never ends

def unionkth(array1, array2, k: int) -> int:

    # base case(s)
    # if array1 is empty, return the kth element of array 2
    if len(array1) == 0:
        return array2[k]
    # if array2 is empty, return the kth element of array 1
    if len(array2) == 0:
        return array1[k]

    # compute the two midpoint indexes of the arrays
    mid1 = len(array1) // 2
    mid2 = len(array2) // 2

    # if the sum of the two midpoints is greater than k
    # the median is guaranteed not to be in the largest second half
    if mid1 + mid2 > k:
        # the largest second half is the one with the larger median
        if array1[mid1] <= array2[mid2]:
            # Discard array2[mid2+1:], because median is not there
            return unionkth(array1, array2[:mid2], k)
        else:
            # same thing, discard array1[mid1+1:]
            return unionkth(array1[:mid1], array2, k)
    else:
        # the median is guaranteed not to be in the smallest first half
        if array1[mid1] <= array2[mid2]:
            # Discard array1[:mid1] becasue it'sthe smallest first half
            # the +1 is important, because the new array starts at mid1+1
            return unionkth(array1[mid1+1:], array2, k - (mid1+1))  
        else:
            # same thing, discard array2[:mid2] and adjust k
            return unionkth(array1, array2[mid2+1:], k - (mid2+1))


def main():
    print("HW#3: Unionkth Recursive")
    print("Comparing this algorithm with joing two arrays, sorting them,\
and then taking the median.")

    array1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    array2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    # k is the median, k-1 is the index
    k = (len(array1) + len(array2)) // 2
    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Median:", unionkth(array1, array2, k))
    # 0-based indexing, since we are looking for the kth element
    print("median by sorting:", (sorted(array1 + array2)[k-1]))


if __name__ == "__main__":
    main()
