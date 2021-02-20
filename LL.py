class LL: 
    class Node: 
        def __init__(self, data): 
            self.data = data 
            self.next = None
    
    def __init__(self): 
        self.head = self.tail = None 
        self.size = 0 
    
    def add(self, data):
        node = self.Node(data)
        if self.tail == node: 
            self.tail = self.head = node 
        else: 
            self.tail.next = node 
            self.tail = node
            self.size +=1 

    def deque(self):
        x = self.head 
        self.head = x.next 
        if self.head is None: 
            self.tail = None
        self.size -=1 
        return x.data 

    def remove(self,data ):
        x = self.head 
        p = None 
        f = False 
        

        while x and f is False:
            if x.data == data: 
                f= True
            else: 
                p = x 
                x = x.next
        
        if p is None: 
            self.head = x.next
            if x.next is None: 
                self.tail = self.head
        else: 
            p.next = x.next 
            if p.next is None: 
                self.tail = p
        self.size -=1 
