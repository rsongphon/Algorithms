import math
import unittest


'''

CountInversion
ListofInteger -> ListofInteger Integer
Given a sorted array of n distinct elements, compute the number of inversions in the array. Using at most O(nlog n ) time complexity. Piggyback merge sorted so return sorted array as an output along with number of inversions.
Assumtion: distinct element in array

'''


class TestCountInv(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sort_and_countinv([1,2,3,4]), ([1,2,3,4],0))
    def test_case_2(self):
        self.assertEqual(sort_and_countinv([8,7,6,5,4,3,2,1]), ([1,2,3,4,5,6,7,8],28))
    def test_case_3(self):
        self.assertEqual(sort_and_countinv([54044 ,14108 ,79294 ,29649, 25260,60660, 2995, 53777, 49689, 9083]), ([2995, 9083, 14108, 25260, 29649, 49689, 53777, 54044, 60660, 79294],28))
    def test_case_4(self):
        self.assertEqual(sort_and_countinv([1]), ([1],0))
    def test_case_5(self):
        self.assertEqual(sort_and_countinv([1,2]), ([1,2],0))
    def test_case_6(self):
        self.assertEqual(sort_and_countinv([2,1]), ([1,2],1))
    def test_case_7(self):
        self.assertEqual(sort_and_countinv([2,1,3]), ([1,2,3],1))
    def test_case_8(self):
        self.assertEqual(sort_and_countinv([3,1,2]), ([1,2,3],2))
    





def sort_and_countinv(loi):
    
    # find array length
    arraylen = len(loi)
    middlepoint = math.floor(arraylen/2) # use floor function 3 element array always split into split to [A] , [B,C]
    
    if (arraylen == 0) or (arraylen == 1):
        return (loi,0) # base case
    else:
        (C , leftinv) = sort_and_countinv(loi[:middlepoint]) # recursively sort and count inverson first half of loi
        (D , rightinv) = sort_and_countinv(loi[middlepoint:]) # recursively sort and count inverson second half of loi
        
        (B , splitinv) = merge_and_countsplitinv(C,D)
        return (B , leftinv + rightinv + splitinv)


def merge_and_countsplitinv(loi1,loi2):
    i = 0
    j = 0
    
    C = loi1
    D = loi2
    
    length_C = len(C)
    length_D = len(D)
    output_len = length_C+length_D
    # output initilize
    B = []
    splitInv = 0
    
    
    for k in range(output_len):
        if i == len(C):
            # append rest of D to B
            return (B + D[j:] , splitInv ) 
        elif j == len(D):  # no need to count split inversion, we already did when element of D is copied.
            return (B + C[i:] , splitInv )
        
        # normal operation
        if C[i] < D[j]:
            B.append(C[i])
            i = i+1
        else:
            B.append(D[j])
            j = j+1
            splitInv = splitInv + (length_C - i) # number left i C that out of order = number of split inversions
    
    return (B , splitInv)
    
    
    
if __name__ == '__main__':
    
    #unittest.main()
    
    # Define the file path
    file_path = 'inversiontestsample.txt'

    # Initialize an empty list to store the numbers
    numbers_list = []

    # Open the file and read the contents
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any extra whitespace and convert the line to an integer
            number = int(line.strip())
            # Append the number to the list
            numbers_list.append(number)

    # Output the list
    print(sort_and_countinv(numbers_list))
