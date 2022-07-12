from dataclasses import dataclass




# partition class
@dataclass
class SortableArray:
    
    array:list
    
    def __len__(self):
        return len(self.array)
    
    def __repr__(self):
        return f"{self.array}"
     
    def partition(self,left_pointer, right_pointer):
        
        pivot_index = right_pointer # we always want to choose the right-most element as the pivot and store pivot index for later use
        
        pivot = self.array[pivot_index] # grab pivot value
        
        right_pointer -= 1  # start the right pointer immediately to the left of pivot
        
        while True:
            while self.array[left_pointer] < pivot: # move the left pointer to the right as long as it points to a value < pivot
                left_pointer += 1
            
            while self.array[right_pointer] > pivot: # move the right pointer to the left as long as it points to a value > pivot
                right_pointer -= 1
                
            # We've now reached the point where we've stopped moving both pointers. 
            # Now, we check whether the left pointer has reached or gone beyond the right. 
            # if yes, we break the loop so we can swap the pivot later in the code
            if left_pointer >= right_pointer:
                break
            
            else:
                # if the left pointer is still to the left of the right pointer,
                # then we swap the values of the left and right pointers
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                
                # we move the left pointer to the right, gearing up 
                # for the next round of left and right pointer movements
                left_pointer += 1 
               
        # at the final step of the partition, we swap the value 
        # of the left pointer with the pivot
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
         
        # we return the left pointer for usage in the quicksort method
        return left_pointer
    
    def quicksort(self, left_index, right_index):
        """Quick sort has O(N*log N) AVERAGE CASE time complexity, O(N^2) worse case"""
        
        # base case: subarray has 0 or 1 elements
        if right_index - left_index <= 0:
            return
        
        # partition the range of elements and grab the index of the pivot
        pivot_index = self.partition(left_index, right_index)
        
        # recursively call quicksort method
        # on whatever is to the left of the pivot:
        self.quicksort(left_index, pivot_index - 1)
        
        # recursively call quicksort method
        # on whatever is to the right of the pivot:
        self.quicksort(pivot_index+1, right_index)
        
    def quickselect(self, kth_lowest_value, left_index, right_index):
        """Quickselect has O(N) average case because after partioning, 
           can ignore the side of the array that doesnt contain what we want"""
        
        # if we reach the base case: that is, that the subarray has one cell,
        # we know we've found the value we're looking for
        if right_index - left_index <= 0:
            return self.array[left_index]
        
        # partition the array and grab index of pivot
        pivot_index = self.partition(left_index, right_index)
        
        # if what we're looking for is to the left of pivot:
        if kth_lowest_value < pivot_index:
            
            # recursively perform quickselect on subarray to the left of pivot
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
            
        # if what we're looking for is to the right of pivot:
        elif kth_lowest_value > pivot_index:
            
            # recursively perform quickselect on subarray to the right of pivot
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
            
        else: # if kth_lowest_value == pivot_index
            
            # if after the parition, the pivot position is in the same spot
            # as the kth lowest value, we've found the value we're looking for
            return self.array[pivot_index]
              
           
def find_largest_product(array):
    """After sorting, the three largest numbers will be to the right"""
    array = sorted(array)
    return array[-1] * array[-2] * array[-3]





def find_missing_num(array):
    array = sorted(array)
    
    for i, num in enumerate(array):
        if i != num:
            return i
      
        
def maxnum1(array):
    greatest = 0
    
    for n in array:
        for i in array:
            if n > i and n > greatest:
                greatest = n
    return greatest
            

def maxnum2(array):
    greatest = 0
    for n in array:
        if n > greatest:
            greatest = n
    return greatest

def maxnum3(array):
    array = sorted(array)
    return array[-1]
    