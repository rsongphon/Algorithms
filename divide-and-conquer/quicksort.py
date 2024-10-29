


'''
QuickSort
ListofInteger length(ListofInteger)-> ListofInteger
Recieving unsorted array, returns sorted array from smallest to largest. 

INVARIANT : for left, right variable in this code
            left = exact positon in the array eg 0 mean position 0 in array
            right = exclusive positon in array (for the purpose of using for loop)
                    eg: right = 5 mean element 0 to 4 in array
'''

import math
import random
import unittest
from utils import read_txt_return_arraynum
import math


class TestQuicksort1(unittest.TestCase):

    def test_quicksort(self):
        test_cases = [
            ([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10]),
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([5, 5, 5, 5], [5, 5, 5, 5]),
            ([9, 3, 7, 6, 2, 8], [2, 3, 6, 7, 8, 9])
        ]

        for arr, expected in test_cases:
            quicksort(arr)
            self.assertEqual(arr, expected, f"Test failed for input {arr}. Expected {expected}, got {arr}")

class TestQuicksort(unittest.TestCase):

    def generate_test_cases(self):
        test_cases = []

        # Add specific test cases
        test_cases.append(([], []))
        test_cases.append(([1], [1]))
        test_cases.append(([2, 1], [1, 2]))
        test_cases.append(([5, 5, 5, 5], [5, 5, 5, 5]))
        test_cases.append(([9, 3, 7, 6, 2, 8], [2, 3, 6, 7, 8, 9]))
        test_cases.append((list(range(10)), list(range(10))))  # Already sorted
        test_cases.append((list(range(10, 0, -1)), list(range(1, 11))))  # Reverse sorted
        test_cases.append(([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]))  # Duplicates

        # Generate random test cases
        for _ in range(92):  # We already added 8 test cases
            arr = [random.randint(0, 100) for _ in range(random.randint(0, 20))]
            expected = sorted(arr)
            test_cases.append((arr, expected))

        return test_cases

    def test_quicksort(self):
        test_cases = self.generate_test_cases()
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                print('Pass')
                quicksort(arr)
                self.assertEqual(arr, expected, f"Test failed for input {arr}. Expected {expected}, got {arr}")
            
            
def quicksort(loi0):
    total_length = len(loi0)
    def quicksort_sub(loi,left,right):
        #n = len(loi[left:right+1])
        n = len(loi[left:right]) # total element
        if (n==0) or (n==1) or (left == total_length) or (right == 0):
            return # No further recursive stack, array already sorted
        else:
            pivot_index = choose_pivot(loi,left , right,mode='median')
            new_pivot_pos = partition_around_pivot(loi, pivot_index , left ,right)
            quicksort_sub(loi,left,new_pivot_pos) # Recursively sort left side of array, pivot in the last position is exclu\sive
            quicksort_sub(loi,new_pivot_pos+1,right) # Recursively sort right side of array, pivout in the the first position is inclusiove so increment bv one        
    return quicksort_sub(loi0,0,total_length)

def choose_pivot(loi,left,right,mode,):
    '''
    Select pivot point of the array
    Mode : 'first' first element of the array
            'last' last element of the array
            'median' 25-75 random position in median range
    '''
    
    if mode =='first':
        return left
    elif mode == 'last':
        return right-1
    elif mode == 'median':
        
        if (right - left) == 1:
            return left
        
        first = loi[left]
        last = loi[right-1]
        mid_point = math.ceil(len(loi[left:right])/2) - 1 # array start at 0 so we need to minus 1 
        pivot_mid_index = left + mid_point 
        mid = loi[pivot_mid_index]
        
        set_candidates = [(first,left) , (last,right) , (mid,pivot_mid_index)]
        #print(set_candidates)
        
        def median_of_three(a, b, c):
            if (a - b) * (c - a) >= 0:
                return a
            elif (b - a) * (c - b) >= 0:
                return b
            else:
                return c
        
        
        median_val = median_of_three(first, last, mid)
        #print(median_val)
        
        for val,index in set_candidates:
            if median_val == val:
                #print(index)
                return index
        
    
def partition_around_pivot(loi,pivot_index , left , right):
    
    if pivot_index == right:
        pivot_index = pivot_index - 1 # right element is outofbound
    
    p = loi[pivot_index]
    # swap pivot with first element
    if pivot_index == 0:
        pass
    else:
        swap_elements(loi,left,pivot_index)
    
    i = left + 1 # first position after the pivot (all number > pivot)
    for j in range(left + 1 ,right):
        
        if (loi[j] < p): # do nothing
            swap_elements(loi,j,i)
            i = i+1
        else:
            continue
    swap_elements(loi,left,i-1) # plce pivot in the correct position
    #print(i-1)
    return i-1 # because i is the first number after pivot

def swap_elements(lst, index1, index2):
    # Perform the swap using tuple unpacking
    lst[index1], lst[index2] = lst[index2], lst[index1]

if __name__ == "__main__":
    unittest.main()
    #A = [14, 24, 40, 72, 88, 91, 37, 98]
    #quicksort(A)
    #print(A)
    # Define the file path
    
    #array_nums = read_txt_return_arraynum('QuickSort.txt')
    #quicksort(array_nums)
    #print(array_nums)
