


class Stack:
    
    def __init__(self):
        
        self.data = []
        
    def __repr__(self) -> str:
        return f"{self.data}"
        
    def push(self, item):
        self.data.append(item)
    
    @property
    def pop(self):
        return self.data.pop()
        
    @property   
    def read(self):
        try:
            return self.data[-1]
        except: pass
    
    
def reverse(string):
    
    s = Stack()
    newstring = ""
    
    for char in string:
        s.push(char)
        
    while s.read: # while items exist in the stack
        newstring += s.pop
        
    return newstring


print(reverse("abcdef"))
        
    
    
    
    
    
    
    
    
def linter(string):
    
    s = Stack()
    
    for char in string:
        if char in ["[", "]", "{", "}", "(", ")"]:
            
            if char in ["[", "{", "("]: # push onto stack if char is an open brace
                s.push(char)
                
            elif char in ["]", "}", ")"]:
                
                try:
                    p = s.pop
                except IndexError:
                    raise IndexError(f"Closing brace '{char}' does not have a corresponding open brace")
                
                if char == "]" and p != "[":
                    raise SyntaxError(f"Closing brace '{char}' does not match opening brace '{p}'")
                
                if char == "}" and p != "{":
                    raise SyntaxError(f"Closing brace '{char}' does not match opening brace '{p}'")
                
                if char == ")" and p != "(":
                    raise SyntaxError(f"Closing brace '{char}' does not match opening brace '{p}'")
                
    if s.read:
        raise SyntaxError(f"Unmatched opening brace found: '{s.pop}'")
    else:
        print("All good!")
       

                
                
                
                

