class Resource:
    def __init__(self, n):
        self.total = n
        self.available = n

    def provideRes(self, n):
        if (self.available - n >= 0):
            self.available -= n
            return 0
        else:
            print("Error: Resource Shortage")
            return 1
        
    def returnRes(self, n):
        if (self.available + n <= self.total):
            self.available += n
            return 0
        else:
            print("Error: Resource Overflow")
            return 1

    def getAvailable(self):
        return self.available

    def getTotal(self):
        return self.total