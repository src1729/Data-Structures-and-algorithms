def bfs(dist,graph,qu,l):
    while qu:
     u=qu.pop(0)
     #dist[u]=1
     #print(u,end=' ')
     l.append(u)
     for v in graph[u]:
       if(dist[v]==-1):
           qu.append(v)
           dist[v]=1+dist[u]
    return l
     
n,m=input().split()
n=int(n)
m=int(m)
graph=[[] for x in range(n)]
for i in range(m):
    u,v=input().split()
    u=int(u)
    v=int(v)
    graph[u].append(v)
    graph[v].append(u)
dist=[-1 for x in range(n)]
qu=[]
u=int(input())
qu.append(u)
dist[u]=0
l=bfs(dist,graph,qu,[])
print(l)
print (dist)