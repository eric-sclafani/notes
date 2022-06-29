


def binary_search(array, target):
    #! important to note: the array never actually gets split up. The guess index just gets shifted left or right
    
    min_ = 0
    max_ = len(array) 
    
    while max_ != min_:
        
        guess = int((max_ + min_) / 2) # guesses the middle element by adding the max and min length and divide by 2
        print(f"Guess: {guess}")

        if array[guess] == target:
            return guess

        elif array[guess] > target:
            max_ = guess - 1 # if middle element is larger than our target, go the the left half of the array 
            print(f"New max: {max_}")
            
        else:
            min_ = guess + 1# if middle element is smaller than our target, go the the right half of the array 
            print(f"New min: {min_}")

    return -1
    
    