from dataclasses import dataclass




# partition class
@dataclass
class SortableArray:
    
    array:list
     
    def partition(self,left_pointer, right_pointer):
        
        # we always want to choose the right-most element as the pivot
        # store pivot index for later use
        pivot_index = right_pointer
        
        # grab pivot value
        pivot = self.array[pivot_index]
        
        # start the right pointer immediately to the left of pivot
        right_pointer -= 1
        
        while True:
            
            # move the left pointer to the right as long as it points to a value < pivot
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            
            # move the right pointer to the left as long as it points to a value > pivot
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
                
                
            # We've now reached the point where we've stopped moving both pointers. 
            # Now, we check whether the left pointer has reached or gone beyond the right. 
            # if yes, we break the loop so we can swap the pivot later in the code
            print("Left:", left_pointer)
            print("Right:", right_pointer)
            
            # if the left pointer is still to the left of the right pointer,
            # then we swap the values of the left and right pointers
            self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
            
            # we move the left pointer to the right, gearing up 
            # for the next round of left and right pointer movements
            left_pointer += 1
            
            
            if left_pointer >= right_pointer:
                break
            
            
          #! not working  
               
        
        # at the final step of the partition, we swap the value 
        # of the left pointer with the pivot
        
        #self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
         
        
        # we return the left pointer for usage in the quicksort method
        return left_pointer
    
    
d = SortableArray([0,5,2,1,6,3])
d.partition(0, -1)
print(d.array)
     
    