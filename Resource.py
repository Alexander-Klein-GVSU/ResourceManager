class Resource:
    def __init__(self, n):
        self.total = n
        self.available = n

    def provideRes(self):
        if (self.available > 0):
            self.available -= 1
            return 0
        else:
            print("Error: Resource Shortage")
            return 1
        
    def returnRes(self):
        if (self.available < self.total):
            self.available += 1
            return 0
        else:
            print("Error: Resource Overflow")
            return 1

    def getAvailable(self):
        return self.available

    def getTotal(self):
        return self.total