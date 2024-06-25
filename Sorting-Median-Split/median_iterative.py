# Stanley Zhao
# May 30 2024
# CS 5800 Algorithms


# iterative mversion of unionkth using a while loop
# the cut-off should be mid1+1 and mid2+1, same as the recursive version

def unionkth(array1, array2, k: int) -> int:

    # binary search, iterative using a while loop
    # the loop condition stays true since the base cases are handled
    while True:
        # base cases
        if len(array1) == 0:
            return array2[k]
        if len(array2) == 0:
            return array1[k]
        if k == 0:
            return min(array1[0], array2[0])
        
        mid1 = len(array1) // 2
        mid2 = len(array2) // 2

        # same logic as in the recursive version
        # except we don't make recursive calls
        # we just truncate the arrays and k
        # the median is guaranteed not to be in the larger second half
        if mid1 + mid2 > k:
            # the largest second half is the one with the larger median
            if array1[mid1] > array2[mid2]:
                # Discard the larger second half
                array1 = array1[:mid1]
            else:
                array2 = array2[:mid2]
        # the median is guaranteed not to be in the smallest first half
        else:
            # the smaller first half is the one with the smaller median
            if array2[mid2] < array1[mid1]:
                array2 = array2[mid2 + 1:]
                k = k - (mid2 + 1)
            else:
                array1 = array1[mid1 + 1:]
                k = k - (mid1 + 1)


def main():
    print("HW#3: Unionkth Iterative")
    print("Comparing this algorithm with joing two arrays, sorting them,\
and then taking the median.")

    array1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    array2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print("Array 1:", array1)
    print("Array 2:", array2)
    k = (len(array1) + len(array2)) // 2
    # we are looking for the kth element, not the index, so no need to minus 1
    print("Median:", unionkth(array1, array2, k))
    print("median by sorting:", (sorted(array1 + array2)[k-1]))  # 0-based indexing


if __name__ == "__main__":
    main()