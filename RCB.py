from LL import LL

class RCB():
    class Resource():
        def __init__(self, state=1):          
            self.state = state
            self.wait_list = LL()
    def __init__(self, size=4):
        self.array = [self.Resource() for i in range(size)]
