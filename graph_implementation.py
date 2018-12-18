class Vertex:

    def __init__(self,key):
        self.id=key
        self.connected={}
    
    def addNeighbour(self,key,weight=0):
        self.connected[key]=weight

    def countNeighbours(self):
        return len(list(self.connected))
    
    def getNeighbours(self):
        return list(self.connected)

    def getWeight(self,key):
        return self.connected[key]

    def getId(self):
        return self.id


class Graph:

    def __init__(self,direct=0):
        self.vertList={}
        self.vertCount=0
        self.directed=direct

    def addVertex(self,key):
        self.vertCount+=1
        vertex = Vertex(key)
        self.vertList[key]=vertex
        return vertex

    def getVertex(self,n):
        if(n in self.vertList):
            return self.vertList[n]
        return None
    
    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbour(t,cost)
        if(self.directed==0):
            self.vertList[t].addNeighbour(f,cost)

    def getVertices(self):
        return self.vertList.keys()

    def countVertices(self):
        return self.vertCount
    
    def getGraph(self):
        return self.vertList

'''  

usage of code
graph object has a dictionary vertList in which integer keys map to vertex objects.
Vertex object has a dictionary in which integer key(to vertex is mapped to weight of edge (default value=0))

0 is passed in constructor to show graph is undirected. Pass 1 for a directed graph. 

g=Graph(0)
for i in range(10):
    g.addVertex(i)
g.addEdge(0,1,1)
g.addEdge(1,2,3)
g.addEdge(2,3,3)
g.addEdge(9,8,3)
g.addEdge(3,6,3)
g.addEdge(3,7,3)

for v in g.getVertices():
    ver=g.vertList[v]
    print(v,ver.getNeighbours())
'''


       
        
