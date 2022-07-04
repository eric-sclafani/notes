


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
    
    
    
def fib1(n):
    """This implementation is inefficient because of the two calls of fib"""
    
    if n in [0,1]:
        return n
    
    return fib1(n-2) + fib1(n-1)



def fib2(n):
    pass
    


    
