import unittest

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
ListofIntger -> Integer
Sum element in List

'''

class TestSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sumloi([]), 0, "Should be 0")
    def test_case_2(self):
        self.assertEqual(sumloi([1]), 1, "Should be 1")
    def test_case_3(self):
        self.assertEqual(sumloi([1,1]), 2, "Should be 2")
    def test_case_4(self):
        self.assertEqual(sumloi([1,2]), 3, "Should be 3")
           
        
def sumloi(loi):
    if len(loi) == 0:
        return 0 # empy case
    else:
        return loi[0] + sumloi(loi[1:])
        
        
if __name__ == '__main__':
    unittest.main()
