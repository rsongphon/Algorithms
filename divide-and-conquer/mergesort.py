import unittest
import numpy as np
import time
import math

'''
helper fuction to make python look more like functional programming
'''
def cons(elem,array):
	return [elem] + array


'''
ListofInteger is one of
- []
- cons( Integer , ListofInteger)
interp. list of integer for recursive problem
'''

LOS1 = []
LOS2 = cons(1,cons(2,cons(3,[])))
'''
def fn_for_loi(loi):
    if len(loi) == 0:
        .... # empy case
    else:
        ....(fn_for_integer(loi[0]) , fn_for_loi(loi[1:]))
'''

'''
Mergesort
ListofIntger -> ListofInteger
Sort element in the list in increasing order using merge sort.
IMPROVEMENT1 : Function can handle redundant element.
IMPROVEMENT2 : Function can be used with both even and odd array.

'''


class TestMergeSort(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mergesort([]), [], "empty array return []")
    def test_case_2(self):
        self.assertEqual(mergesort([1]), [1], "one element array return itself")
    def test_case_3(self):
        self.assertEqual(mergesort([2,1]), [1,2])
    def test_case_4(self):
        self.assertEqual(mergesort([1,2]), [1,2], "Return itself")
    def test_case_5(self):
        self.assertEqual(mergesort([4,3,2,1]), [1,2,3,4])
    def test_case_6(self):
        self.assertEqual(mergesort([3,2,1]), [1,2,3])
    def test_case_7(self):
        self.assertEqual(mergesort([1,2,3]), [1,2,3])
    def test_case_8(self):
        self.assertEqual(mergesort([8,6,7,4,5]), [4,5,6,7,8])
    def test_case_9(self):
        self.assertEqual(mergesort([1,1,2,2,2]), [1,1,2,2,2])
    def test_case_10(self):
        self.assertEqual(mergesort([2,1,1,2,2]), [1,1,2,2,2])
    def test_case_11(self):
        self.assertEqual(mergesort([3,1,1,2,2]), [1,1,2,2,3])

           
def mergesort(loi):
    
    # find array length
    arraylen = len(loi)
    middlepoint = math.floor(arraylen/2) # use floor function 3 element array always split into split to [A] , [B,C]
    
    
    if (arraylen == 0) or (arraylen == 1):
        return loi # empy case
    else:
        c = mergesort(loi[:middlepoint]) # recursively sort first half of loi
        d = mergesort(loi[middlepoint:]) # recursively sort second half of loi
        
        return merge(c , d)
    
def merge(loi1,loi2):
    i = 0
    j = 0
    
    C = loi1
    D = loi2
    
    # output
    B = []
    
    output_len = len(C)+len(D)
    
    for k in range(output_len):
        
        # if C is exhausted
        if i == len(C):
            # append rest of D to B
            return B + D[j:]
        elif j == len(D):
            return B + C[i:]
        
        # normal operation
        if C[i] < D[j]:
            B.append(C[i])
            i = i+1
        else:
            B.append(D[j])
            j = j+1
    
    return B       
        
if __name__ == '__main__':
    
    #unittest.main()
    
    # Define the desired length (must be even)
    length = 1000000

    # Define the range for unique numbers
    low = 0
    high = 10000000

    # Ensure the length is not larger than the range of unique values
    if length > (high - low):
        raise ValueError("Length is larger than the range of unique values")

    # Generate a list of unique random integers
    random_integers = np.random.choice(np.arange(low, high), size=length, replace=False).tolist()
    
    #print(random_integers)

    # Start time
    start_time = time.time()

    sort = mergesort(random_integers)
    
    # End time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time_merge = end_time - start_time
    
    print(f"The mergesort function took {elapsed_time_merge} seconds to run.")
    
    # Start time
    start_time = time.time()
    
    random_integers.sort()
    
    # End time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time_sort = end_time - start_time
    
    print(f"The normal sort function took {elapsed_time_sort} seconds to run.")
    

    
