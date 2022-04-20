def hpfy(h,p,sz):
    if p*2<=sz:
        if h[p]>h[2*p] or h[p]>2*p+1:
            if h[2*p]<h[2*p+1]:
                h[p],h[2*p]=h[2*p],h[p]
                hpfy(h,2*p,sz)
            else:
                h[p],h[2*p+1]=h[2*p+1],h[p]
                hpfy(h,2*p+1,sz)
def push(h,y,sz):
    sz+=1
    h[sz]=y
    curr=sz
    while h[curr]<h[curr//2]:
        h[curr],h[curr//2]=h[curr//2],h[curr]
        curr=curr//2
    return sz
def rem(h,sz):
    if sz==0: return "error",sz
    pop=h[1]
    h[1]=h[sz]
    sz-=1
    hpfy(h,1,sz)
    return pop,sz
def heapsort(h,sz):
    a=[]
    while sz>0:
       x,sz=rem(h,sz)
       a.append(x)
    return a
n=int(input())
sz=0
heap=[0 for x in range(n+1)]
heap[0]=-99999999999
for qq in range(0,n):
    x,y=input().split()
    y=int(y)
    if x=="ADD":
        heap[0]=min(heap[0],y-1)
        sz=push(heap,y,sz)
    elif y==-1:
        a,sz=rem(heap,sz)
        print(a)
    else:
        if sz>0:print(heap[1])
print(heapsort(heap,sz))
#print(heap)