



def bubble_sort(array):
    
    flag = 0
    for _ in range(len(array)):
        for i in range(len(array)-1):
            
            if array[i] > array[i+1]:
                temp = array[i] # store first element in a temporary variable
                array[i] = array[i+1] # assigns the first element as the second
                array[i+1] = temp # assigns the second element as the first
                flag = 1
                
        # monitors whether elements are getting swapped inside the inner for loop
        # will cut the loop short to save time complexity if array is finished sorting early
        # basically, we expect sorting to happen on each iteration. But no sorting == elements are already sorted
        if not flag:
            break
     
    return array
    