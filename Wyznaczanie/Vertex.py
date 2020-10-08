import sys;

class Vertex(object):
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adkacenciesList = []
        self.minDistance = sys.maxsize
        
    def __cmp__(self, otherVertex):
        return self.c,p(self.minDistance, otherVertex.minDistance)
    
        
        
    def __lt__(self):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority
        