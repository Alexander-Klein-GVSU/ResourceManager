class Process:
    def __init__(self, n):
        self.requests = [0] * n
        self.has = [0] * n
        self.finished = False
    
    def request(self, r, n):
        self.finished = False
        self.requests[r] += n

    def take(self, r, n):
        self.requests[r] -= n
        self.has[r] += n

    def release(self, r, n):
        self.has[r] -= n
        self.setFinished()

    def setFinished(self):
        f = True
        for i in range(len(self.requests)):
            if ((self.requests[i] != 0) or (self.has[i] != 0)):
                f = False
        self.finished = f

    def isFinished(self):
        return self.finished

    def getRequests(self, n):
        return self.requests[n]

    def getHas(self, n):
        return self.has[n]