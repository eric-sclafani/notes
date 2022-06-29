class Queue:
    
    def __init__(self):
        
        self.data = []
        
    def __repr__(self) -> str:
        return f"{self.data}"
        
    def push(self, item):
        self.data.append(item)
    
    @property
    def pop(self):
        return self.data.pop(0)
        
    @property   
    def read(self):
        try:
            return self.data[0]
        except: pass
        
        
q  = Queue()

