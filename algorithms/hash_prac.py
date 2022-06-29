# hash map exercises


def intersection(a1, a2):

    hash = {i: True for i in a1} # maps all values from first array to True    
    return [i for i in a2 if hash.get(i)]

    
def findfirstdupe(array):
    
    hash = {}
    
    for i in array:
        if i not in hash:
            hash[i] = True
        else:
            return i
        
    return None

def findmissingletter(string):
    hash = {i:True for i in string}
    
    for s in "abcdefghijklmnopqrstuvwxyz":
        if not hash.get(s):
            return s
    return None
 

def findfirstnondupe(string):
    hash = {}
    
    for s in string:
        if s not in hash:
            hash[s] = 1
        else:
            hash[s] += 1
            
    for s in string:
        if hash[s] == 1:
            return s
        
        
print(findfirstnondupe("minimum"))