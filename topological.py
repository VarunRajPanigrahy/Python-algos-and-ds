from graph_implementation import Graph,Vertex


def topological_sort_util(graph,vertex,visited,stack):
    visited[vertex]=True
    if(vertex in graph.getGraph() and graph.getGraph()[vertex]):
        for v in graph.getGraph()[vertex]:
            if( not visited[v]):
                topological_sort_util(graph,v,visited,stack)
    stack.insert(0,vertex)

def topological_sort(graph):
    visited=dict()
    for v in graph.getGraph():
        visited[v]=False
    stack=[]
    for i in graph.getGraph():
        if( not visited[i]):
            topological_sort_util(graph,i,visited,stack)
    return stack


'''   
g=Graph(1)
for i in range(1,8):
    g.addVertex(i)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(2,7)

print(g.getGraph())
b=topological_sort(g)

print(b)
'''