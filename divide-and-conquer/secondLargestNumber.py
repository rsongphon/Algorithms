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
secondLargestnumber
ListofInteger -> Integer
Compute second largest number by using simple linear scan
INVARIANT : n is a  power of 2 (at least 2 elements)
INVARIANT : input is unsorted array of n distinct numbers

'''

#def secondlargest(loi):
#    return  0

class TestSecondLargest(unittest.TestCase):
    def test_case_3(self):
        self.assertEqual(find_second_largest([2,1]), 1)
    def test_case_5(self):
        self.assertEqual(find_second_largest([4,3,2,1]), 3)
    def test_case_6(self):
        self.assertEqual(find_second_largest([4,3,2,1,5,99,1359,44,52,63,666,13457,99999]), 13457)
        
        
    
def find_second_largest(arr):
    # Helper function to perform tournament and track comparisons
    def tournament(arr):
        winners = -999
        comparisons = -999
        
        for i in range(len(arr) - 1):
            if (arr[i] > arr[i+1]) and (arr[i] > winners) :
                winners = arr[i]
                second_runner = arr[i+1]
            elif (arr[i+1] > arr[i]) and (arr[i+1] > winners):
                winners = arr[i+1] 
                second_runner = arr[i]

        return winners, second_runner
    
    # Find the largest number and track comparisons
    winners, second_runner = tournament(arr)
    
    return second_runner
    
                
if __name__ == "__main__":
    unittest.main()
