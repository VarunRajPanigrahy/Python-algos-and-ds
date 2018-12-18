from graph_implementation import Graph,Vertex

def dfs(graph,key):
    visited=[]
    start=graph.getVertices()[0]
    stack=[start]
    graph_dict=graph.getGraph()
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for child in graph.getVertex(vertex).getNeighbours():
                if(child not in visited):
                    stack.append(child)
        if(key in visited):break
    return visited

'''
g=Graph(0)
for i in range(1,10):
    g.addVertex(i)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(7,8)
g.addEdge(5,9)

b=dfs(g,9)
#print(g.getGraph())
print(b)
'''