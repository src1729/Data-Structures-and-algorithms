def dfs(dist,graph,stack,l):
    while len(stack):
      u=stack.pop()
      
      if(dist[u]==-1):
          dist[u]=0
          l.append(u)
      for v in graph[u]:
          if (dist[v]==-1):
              stack.append(v)
              
              #print(v)
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
stack=[]
u=int(input())
stack.append(u)
l=dfs(dist,graph,stack,[])
print(l)
print (dist)