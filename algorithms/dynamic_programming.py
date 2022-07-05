

def max1(array):
    """This implementation of max is extremely inefficient because of the two recursive calls
       When this function operates over [1,2,3,4,5], it gets called 15 total times. That's 3 times larger than the len(array)! 
       
       time complexity = O(2^n)
       """
    if len(array) == 1:
        return array[0]
      
    if array[0] > max1(array[1:]):
        return array[0]
    else:
        return max1(array[1:])
    
def max2(array):
    """This implementation of max is way more efficient because we are storing the result of our recursive call, 
       and thus not performing two recursive calls, severely increasing the efficiency
       
       time complexity = O(n)
       """
       
    if len(array) == 1:
        return array[0]
    
    # saving the recursive call to a variable to avoid unnecessary function calls
    max_of_remainder = max2(array[1:])
    
    if array[0] > max_of_remainder:
        return array[0]
    else:
        return max_of_remainder
 
 
#! When it comes to memoization, it can be done natively, or by using a myriad of packages as well
from functools import lru_cache
 
 
    
def fib_without_memo(n):
    """This implementation is inefficient because the two calls of fib both execute the same calculations, 
       leading to a massive amount of function iterations (way more than needed"""
    
    if n in [0,1]:
        return n
    
    return fib_without_memo(n-2) + fib_without_memo(n-1)


def fib_memo1(n, memo={}):
    """To address the problem of the previous function, one can add memoization, 
       which means we store the result of each sub calculation instead of constantly recalculating things"""
    
    # base case
    if n < 2:
        return n
    
    # check memo dict to see if fib(n) has already been calculated
    if not memo.get(n):
        
        # if not, add it to memo
        memo[n] = fib_memo1(n-2, memo) + fib_memo1(n-1, memo)
        
    return memo[n]

@lru_cache(maxsize=None)
def fib_with_memo2(n):
    
    if n < 2:
        return n
    else:
        return fib_with_memo2(n-2) + fib_with_memo2(n-1)
    
# bottom up fibonacci sequence (non-recursive)
def fib_bu(n):
    
    if not n:
        return 0
    
    # first 2 fib numbers
    n1,n2 = 0,1
    
    for _ in range(1,n):
        temp = n1
        n1 = n2
        n2 = temp + n1
    
    return n2



def add_until_100(array):
    
    if not len(array):
        return 0
    
    current_result = add_until_100(array[1:])
    
    if array[0] + current_result > 100:
        return current_result
        
    else:
        return array[0] + current_result



def golomb(n, memo={}):
    
    if n == 1:
        return 1
    
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n-1,memo),memo),memo)
    
    return memo[n]



def unique_paths(rows, cols, memo={}):
    
    if rows == 1 or cols == 1:
        return 1
    
    if not memo.get((rows,cols)):
        
        memo[(rows,cols)] = unique_paths(rows-1, cols, memo) + unique_paths(rows, cols-1, memo)
        
    return memo[(rows, cols)]


