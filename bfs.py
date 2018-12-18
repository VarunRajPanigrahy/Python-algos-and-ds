from graph_implementation import Graph,Vertex

def bfs(graph,key):
    #vertex=graph.getVertex(key)
    vertices_list=graph.getVertices()
    queue=[vertices_list[0]]
    visited=[queue[0]]
    i=0
    
    while len(queue)>0:
      
        vertex_key=queue[0]
        
        vertex=graph.getVertex(vertex_key)
        #print(queue)
        #print(vertex.getNeighbours(),i)
        for child in vertex.getNeighbours():
            if(child not in visited):
                queue.append(child)
                visited.append(child)
        #print(visited,"v")
        #print(queue,"q")
        a=queue.pop(0)
        if(key in visited):return visited
    return visited
    
    
'''
g=Graph(0)
g.addVertex(3)
g.addVertex(7)
g.addVertex(9)
g.addVertex(25)
g.addVertex(37)
g.addVertex(43)
g.addVertex(52)


g.addEdge(3,7)
g.addEdge(3,9)
g.addEdge(7,25)
g.addEdge(7,37)
g.addEdge(9,43)
g.addEdge(9,52)
b=bfs(g,52)
#print(g.getGraph())
print(b)
'''
