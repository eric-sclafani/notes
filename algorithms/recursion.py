




printarray = [1,2,3,[4,5,6],7,[8,[9,10,11,[12,13,14]]],[15,16,17,18,19,[20,21,22,[23,24,25,[26,27,29]],30,31],32], 33]

def printnums(arrays):
    """This function recurses through nested arrays and prints any number it finds"""
    for element in arrays:
      
        if isinstance(element, int):# if current element is an integer, print it out
            print(element)
        else:                       # else, plug the element back into the printnums function
            printnums(element)

def factorial_v1(n):
    return 1 if n == 1 else n * factorial_v1(n-1) 

def factorial_v2(n, i=1, product=1):
    """
    n = number for which we are finding the factorial
    i = increments by 1 for each successive function call
    product = stores the calculations
    
    """
    return product if i > n else factorial_v2(n, i+1, product*i)


def sum(array):
    return array[0] if len(array) == 1 else array[0] + sum(array[1:])


def reverse(string):
    return string[0] if len(string) == 1 else reverse(string[1:]) + string[0]

def count(string, x):
    
    # return 0 if empty string
    if not string: return 0
    
    # +1 for each time string[0] == x
    return 1 + count(string[1:], x) if string[0] == x else count(string[1:],x)
    
def num_of_paths(n):
    """I think we're assuming the max amount of steps at one time is three?"""
    
    # two base cases
    if n < 0: return 0
    if n in [0,1]: return 1
    
    # number of paths to the top is the sum of previous three numbers of paths
    return num_of_paths(n-1) + num_of_paths(n-2) + num_of_paths(n-3) 


a = ["ab", "c", "def", "ghij"]

def count_chars_reg(array):
    return sum([len(x) for x in array])

def count_chars_resursive(array):
    
    if len(array) == 1: return array[0]
    return len(array[0]) + count_chars_resursive(array[1:])

def only_even(array):
    
    if not array: return []
    
    return [array[0]] + only_even(array[1:]) if array[0] % 2 == 0 else only_even(array[1:])



def triangular_nums(n, i=1, result=0):
    
    if i > n:
        return result

    return triangular_nums(n, i+1, result+i)


def x_first_index(string,i=1):
    
    if string[0] == "x":
        return i
    
    return x_first_index(string[1:], i+1)


def find_shortest_paths(rows, cols):
    
    if rows == 1 or cols == 1:
        return 1
    
    return find_shortest_paths(rows-1, cols) + find_shortest_paths(rows, cols-1) 

print(find_shortest_paths(3,7))