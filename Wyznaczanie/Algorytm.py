import heapq


class Algorytm(object):
    def ObliczNajkrotszaTrase(self, vertexList, startVertex):
        
        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue, startVertex)
        
        while len(queue)>0:
            
            actualVertex = heapq.heappop(queue);
            
            for edge in actualVertex.adkacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue, v)
                    
    
    def NajkrotszaDroga(self, targetVertex):
        
        print("Najkrotsza cieżka do celu to: %d metrow" % (targetVertex.minDistance))
        s = (targetVertex.minDistance/11.111) +1
        godziny = s/3600
        minuty = (s%3600)/60
        sekundy = s%60
        print("Planowany czas dotarcia pojazdem (40 km/h):%d godzin %d minut %d sekundy" % (godziny, minuty, sekundy))
        
        node = targetVertex
        
        print("Najkrotsza droga prowadzi przez:")
        
        while node is not None:
            print("%s ->" % node.name)
            node = node.predecessor