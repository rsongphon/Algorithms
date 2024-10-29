
'''
Karatsuba Multiplication

Integer -> Integer
multiple 2 integers using Karasuba algorithm
Assumption: n is a power of 2

'''
import math
import unittest

class TestKarasuba(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(karasuba(24,24), 576)
    def test_case_2(self):
        self.assertEqual(karasuba(1234,5678), 7006652)

        
#def karasuba(int1, int2):
#    return 0

def is_single_digit(num):
    if isinstance(num, int):
        return -9 <= num <= 9
    return False

def split_into_pairs(num,middlepoint):
    first , second = divmod(num,10**middlepoint)
    return int(first) , int(second)

def size_base10(num):
    return int(len(str(num)))


def karasuba(int1, int2):
    
    
    if is_single_digit(int1) or is_single_digit(int2):
        return int1 * int2
    
    
    else:
        
        # /* Calculates the size of the numbers. */
        m = max(size_base10(int1) , size_base10(int2))
        middle = math.floor(m/2)
    

        # break input into first and second half
        a , b = split_into_pairs(int1,middle)
        c , d = split_into_pairs(int2,middle)
        
        # compute p and c
        p = a + b
        q = c + d
        # recursively compute ac , bd , pq
        
        ac = karasuba(a,c)
        bd = karasuba(b,d)
        pq = karasuba(p,q)
        
        # compute adbc
        abcd = pq - ac - bd
        
        # compute the result in sophisticated way
        # assumtion n int1 = n int 2  
        
        zeroes_n_str = '0'*(middle*2)
        half_zeroes_n_str = '0'*middle
        
        ac_padding = str(ac) + zeroes_n_str
        adbc_padding = str(abcd) + half_zeroes_n_str
        result = int(ac_padding) + int(adbc_padding) + bd
        
        return result


if __name__ == "__main__":
    unittest.main()
    
    result = karasuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
    
    print(result)
