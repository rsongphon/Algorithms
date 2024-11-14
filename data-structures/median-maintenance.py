import heapq

# The median maintenance problem.
# You are presented with a sequence of numbers, one by one 
# Assume for simplicity that they are distinct. 
# Each time you receive a new number, your responsibility is to reply with the median element of all the numbers you’ve seen thus far.

# H1 MaxHeap
# H2 MinHeap


# The first invariant is that H1 and H2 are balanced, meaning they each contain the same number of elements (after an even round)  or that one contains exactly one more element than the other (after an odd round). 
# The second invariant is that H1 and H2 are ordered, meaning every element in H1 is smaller than every element in H2.

# To figure out where to insert a new element x so that the heaps remain ordered, it’s enough to compute the maximum element y in H1 and the minimum element z in H2.

# If x is less than y, it has to go in H1; if it’s more than z, it has to go in H2; if it’s in between, it can go in either one.

'''
how to get the median from 2 heaps, always get the value from the heap which 
collects smaller values and return the high of those smaller values because of the way it is described in the programming assignment. 
(Note- do not let the length of max_heap go above length of min heap)
'''



def return_median(H1,H2,num,r):
    if (len(H1) == 0) and (len(H2) == 0):
        # Number goes to H1(MaxHeap, lowerheap)
        heapq.heappush(H1, (num*-1))
    
    elif (num < (H1[0]*(-1))): #extractMax from H1
        heapq.heappush(H1, (num*-1)) # goes to H1 (lowerheap)
    elif (len(H2) != 0) and (num > H2[0]): # Extractmin from H2
        heapq.heappush(H2, num)
    else:
        heapq.heappush(H2, (num))
        
    if (r % 2) == 0: # even round
        if abs(len(H1) - len(H2)) == 2: # unbalance case
            if (len(H1) - len(H2)) == 2: # H1 has more element
                element = -heapq.heappop(H1) # multiply negative value to return to original value
                heapq.heappush(H2, element) # add to H2
            else: # H2 has more element
                element = heapq.heappop(H2)
                heapq.heappush(H1, (element*-1)) # add to H1, don't forget to multiply by -1

    # Extract median
    # ExtractMax from smaller value, multiple by -1 to return to original value
    if len(H1) == len(H2):
        return (H1[0] * -1)  # extracmin to get median
    # Other case -> median in the larger heap
    elif len(H1) > len(H2):
        return (H1[0] * -1) 
    else:
        return H2[0]
        

    
if __name__ == "__main__":
    H1 = []
    H2 = []
    summed = 0
    test = [1,2,3,4,5,6,7]
    test1 = [1,666,10,667,100,2,3]
    test2 = [6331, 2793, 1640,9290,225,625,6195,2303,5685,1354]
    test3 = []
    
    with open('Median.txt', 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace characters (like newlines)
            line = line.strip()
            test3.append(int(line))

    
    for r, num in enumerate(test3):
        median = return_median(H1,H2,num,r+1)
        
        #print(H1)
        #print(H2)
        #print(median)
        summed = summed + median
        
        if r == 10000:
            break
    
    print(summed)
    summod = summed % 10000 #
    print(summod)
