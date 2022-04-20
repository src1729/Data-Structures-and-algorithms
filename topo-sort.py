from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  
   
    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def topo(self, u, vi, stack):
        vi[u] = True 
        for i in self.graph[u]:
            if vi[i] is False:
                self.topo(i, vi, stack)    
        stack.append(u)  

    def topoooot(self,n):
        
        vi = [False for x in range(0,n)]
        stack = []
        for i in range(n):
            if vi[i] is False:
                self.topo(i, vi, stack)
        for i in range(n):
           print(stack[n-i-1],end=' ')

g = Graph()
n,m=input().split()
n=int(n)
m=int(m)
for i in range (m):
    u,v=input().split()
    u=int(u)
    v=int(v)
    g.add_Edge(u,v)
g.topoooot(n)