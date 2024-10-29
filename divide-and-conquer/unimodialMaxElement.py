
'''

UnimodialMaxElem
ListofInterger -> Integer
given a unimodal array of n distinct elements, compute the maximum element of 
a unimodal array thatruns in O(log n) time
Assumtion: distinct element in array



'''
import math
import unittest

class UnimodialMaxElem(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(unimodialmaxelem([2, 3, 4, 21, 43, 52, 51, 18, 11, 9, 6, 1]), 52)
    def test_case_2(self):
        self.assertEqual(unimodialmaxelem([2, 3, 4, 21, 43, 52, 67, 101, 211]), 211)
    def test_case_3(self):
        self.assertEqual(unimodialmaxelem([73, 52, 51, 18, 11, 9, 6, 1]), 73)
    def test_case_4(self):
        self.assertEqual(unimodialmaxelem([10,50,1]), 50)
    def test_case_5(self):
        self.assertEqual(unimodialmaxelem([50,1]), 50)
    def test_case_6(self):
        self.assertEqual(unimodialmaxelem([500,50,1]), 500)
    def test_case_7(self):
        self.assertEqual(unimodialmaxelem([1,2,3]), 3) 
        

        
#def unimodialmaxelem(loi):
#    return 0

def unimodialmaxelem(loi):
    arraylen = len(loi)
    middlepoint = math.floor(arraylen/2) # use floor function 3 element array always split into split to [A] , [B,C]

    C = loi[:middlepoint]
    D = loi[middlepoint:]

    
    if (len(C) == 1) and (len(D) == 1):
        if C[0] > D[0]:
            return C[0] # base case
        else:
            return D[0] # base case
    elif (len(C) == 1):
        if C[0] > D[0]:  # since array is unimodal, we cannot have element in D that have more value than C if C is one element and larger 
            return C[0]
        else:
            return unimodialmaxelem(D) # if C is smaller -> biggest element is in right array
    elif  C[-1] > D[0]:
        return unimodialmaxelem(C) # Recursive case
    else:
        return unimodialmaxelem(D) # Recursive case


if __name__ == "__main__":
    unittest.main()
