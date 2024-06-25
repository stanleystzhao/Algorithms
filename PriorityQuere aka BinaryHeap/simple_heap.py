# Bruce A. Maxwell
# Heap class
# Summer 2024
# HW #4

import random

def compareup( a, b ):
    return a < b

def comparedown( a, b ):
    return a > b

# implements a priority queue using a heap
class PQ:

    # specify the size of the heap up front
    # specify the comparison function
    def __init__(self, size, compare):
        self.array = [-1 for i in range(size)]
        self.size = 0
        self.comp = compare

    # add something to the queue
    def add(self, thing):
        # if the array isn't big enough, double it and copy over the data.
        
        self.array[self.size] = thing
        self.size += 1
        
        self.reheap_up(self.size-1)

    # remove the top item from the queue
    def remove(self):
        retval = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.size -= 1

        self.reheap_down(0)
        
        return retval

    # move a node up the heap as long as its parent is lower priority
    def reheap_up(self, index):
        if index == 0:
            return

        parent = (index-1)//2
        if self.comp( self.array[parent], self.array[index] ):
            return

        tmp = self.array[index]
        self.array[index] = self.array[parent]
        self.array[parent] = tmp

        self.reheap_up( parent )
        return

    # move a node down the heap as long as it is lower priority
    def reheap_down(self, index):
        left_child = index*2 + 1
        right_child = index*2 + 2

        if left_child >= self.size:
            return

        max = left_child
        if right_child < self.size:
            if self.comp( self.array[right_child], self.array[left_child] ):
                max = right_child

        if self.comp( self.array[index], self.array[max] ):
            return

        tmp = self.array[index]
        self.array[index] = self.array[max]
        self.array[max] = tmp

        self.reheap_down(max)
        return

    # return true if the queue is empty
    def empty(self):
        return self.size == 0


# Main test function
def main():

    # make a PQ
    pqup = PQ(20, compareup)
    pqdown = PQ(20, comparedown)

    values = []
    for i in range(20):
        values.append( random.randint(0, 20) )

    print("\nBefore: ")
    print(values)
        
    for i in range(20):
        pqup.add( values[i] )
        pqdown.add( values[i] )

    upresult = []
    downresult = []
    for i in range(20):
        upresult.append( pqup.remove() )
        downresult.append( pqdown.remove() )

    print("\nAfter Up: ")
    print( upresult )
    print("\nAfter Down: ")
    print( downresult )
            

if __name__ == "__main__":
    main()
