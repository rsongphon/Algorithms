
'''

BinarySearch
ListofInteger,Integer -> Boolean
Given a sorted array smallest to largest (distinct)
Return True if A[i] = i False otherwise
Assumption: distinct element in array
'''
import math
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarysearch([],999), False)
    def test_case_2(self):
        self.assertEqual(binarysearch([1],1), True)
    def test_case_4(self):
        self.assertEqual(binarysearch([1],2), False)
    def test_case_5(self):
        self.assertEqual(binarysearch([1,2],2), True)
    def test_case_6(self):
        self.assertEqual(binarysearch([1,2],3), False)
    def test_case_7(self):
        self.assertEqual(binarysearch([1,2,3],3), True)
    def test_case_8(self):
        self.assertEqual(binarysearch([1,2,3],1), True)
    def test_case_9(self):
        self.assertEqual(binarysearch([1,2,3],4), False)
    def test_case_10(self):
        self.assertEqual(binarysearch([1,2,3,4],2), True)
    def test_case_11(self):
        self.assertEqual(binarysearch([1,2,3,4],3), True)
    def test_case_12(self):
        # Generate a list of 100000 elements in increasing order
        increasing_list = list(range(0, 1000001))
        self.assertEqual(binarysearch(increasing_list,999999), True)


        

        
#def binarysearch(loi,i):
#    return False

def binarysearch(loi,i):
    if len(loi) == 0:
        return False
    
    arraylen = len(loi)
    middlepoint  = math.floor(arraylen/2)   # use floor function 3 element array always split into split to [A] , [B,C]
    
    if arraylen % 2 == 0:
        middlepoint = middlepoint -1
    
    middle_element = loi[middlepoint]
    

    
    if middle_element == i:
        return True
    elif middle_element > i: # target in the left array
        return binarysearch(loi[:middlepoint],i)
    else: # target in the right array
        return binarysearch(loi[middlepoint+1:],i)


if __name__ == "__main__":
    unittest.main()
