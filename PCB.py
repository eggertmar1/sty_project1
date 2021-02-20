from LL import LL
from RCB import RCB 
from RL import RL 

class Error(Exception): pass

class PCB:
    class Process:
        def __init__(self, parent):
            self.state = 1
            self.parent = parent
            self.children = LL()
            self.resources = LL()

    def __init__(self, size=16):
        self.size = size
        self.PCB = [None] * self.size
        self.PCB[0] = self.Process(None)
        self.running = 0
        self.RL = RL()
        self.RCB = RCB()


    def create(self,priority):
        if priority == 0: 
            raise Error() # process 0 is the only one to have priority 0 , print something for explaining 


    def destroy(self):  ## mogulega delete fallid ? 
        pass

    def scheduler(self):
        pass

    def _delete(self): #helper function
        pass 

    def delete(self, idx): 
        pass 

    def request(self, idx):
        pass 

    def release(self, resource):
        pass
    
    def timeout(self):
        pass


        

    














