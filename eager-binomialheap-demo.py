class node:    # each binomial trees
    def __init__(self,val=None):
        self.val=val
        self.deg=0
        self.parent=self.left=self.bro=None       #bro is just fancy way to say sibling lol

class beap:   #bheap= array of root nodes
    def link(self,b1,b2):  #link 2 trees
        if b1.val<=b2.val:   # minheap property
            temp=b1.left
            b1.left=b2
            b2.bro=temp
            b1.deg+=1
            b2.parent=b1
            return b1
        else: return self.link(b2,b1)   
    def adjust(self,bheap):    #adjust by merging trees of same degrees
        x=0
        next=1
        nexx=2
        bp=[]
        n=len(bheap)
        if n==0:return bp
        while x<n:
            if x==n-1:    #reched the end of the array
                bp.append(bheap[x])
                x+=1
                next+=1
                nexx+=1
            elif bheap[x].deg!=bheap[next].deg :     #current and next have different degree
                bp.append(bheap[x])
                x+=1
                next+=1
                nexx+=1
            else:   #current and next have same degree
                if nexx<n and bheap[x].deg==bheap[nexx].deg:    # next.next also has same degree
                    bp.append(bheap[x])
                    x+=1
                    nexx+=1
                    next+=1
                else:
                    bheap[next]=self.link(bheap[x],bheap[next])   #next.next is different degree
                    x=next
                    next=x+1
                    nexx=next+1
        
        for j in range(len(bp)-1):
                bp[j].bro=bp[j+1]
        bp[len(bp)-1].bro=None
                
        return bp
    def union(self,bheap1,bheap2):   #union of 2 bheaps
        n1=len(bheap1)
        n2=len(bheap2)
        i,j=0,0
        bheap=[]
        while i<n1 and j<n2:
            if bheap1[i].deg<=bheap2[j].deg:
                bheap.append(bheap1[i])
                i+=1
            else:
                bheap.append(bheap2[j])
                j+=1
        while i<n1:
            bheap.append(bheap1[i])
            i+=1
        while j<n2:
            bheap.append(bheap2[j])
            j+=1
        return self.adjust(bheap)

    def insert(self,bheap,val):
        temp=[node(val)]
        if bheap==None: return temp
        if bheap==[]:return temp
        return self.union(bheap,temp)

    def findmin(self,bheap):
        return min([x.val for x in bheap])   #find minimum of values of the roots in array

    def extractmin(self,bheap):
        bp1=[]
        bp2=[]
        m=self.findmin(bheap)
        c=0    #flag for first occurance of minimum
        for i in range (len(bheap)):
            if m==bheap[i].val and c==0:    
                c+=1
                x=bheap[i].left
                while x:     #pull up all siblings of leftchild of min
                    x.parent=None
                    bp1.append(x)
                    x=x.bro
            elif c==1 or m!=bheap[i].val:
                bp2.append(bheap[i])
        return (m,self.union(bp1,bp2))    #returns minimum and final bheap after deletion of min.

    def find(self,bheap,val):        #search function: O(n) recursive heavy.used in decrease(amortised-logn(loglogn)) and delete
        if bheap==None: 
            return None
        if bheap.val==None:return None
        if bheap.val==val:
            return bheap
        x=node()
        x=self.find(bheap.left,val)
        if x: return x
        return self.find(bheap.bro,val)

    def decrease(self,bheap,k,nk):    #decrease value of x to k
        x=node()
        c=0
        for i in range (len(bheap)):
           if bheap[i]:
               if bheap[i].val==k:
                   c=i
                   break
           x=self.find(bheap[i].left,k)
           if x:
               c=i
               break
        if not x: return bheap
        x.val=nk
        while x.parent:
            if x.val<x.parent.val:
                x.val,x.parent.val=x.parent.val,x.val
                x=x.parent
            else: break
        while x.parent:
            x=x.parent
        bheap[c]=x      #update the tree where decrease operation took place
        return bheap

    def delkey(self,rt,key,bheap):    #delete a key from the heap
        x=node()
        x=self.find(rt,key)
        if not x: return bheap
        m=self.findmin(bheap)
        bheap=self.decrease(bheap,key,m-1)
        m,bheap=self.extractmin(bheap)
        return bheap
    
    def display(self,head):           #display the heap
        while head:
            print(head.val,end=' ')
            self.display(head.left)
            head=head.bro

n=int(input())      #number of input
bhp=beap()
bh=[]
for i in range(n):
    x =input()
    if x=="-1":       #-1 to break
        break 
    if x=="a":         #next line should contain a single integer to be added to heap
       y=input()
       bh= bhp.insert(bh,int(y))
    if x=="em":          #extracts minimum
       if len(bh)==0:
           print("error")
           continue
       m,bh= bhp.extractmin(bh)
       print(m)
    if x=="m":      #prints minimum
        if len(bh)==0:
            print("error")
            continue
        print(bhp.findmin(bh))
    if x=="d":           #next line should contain 2 integers , first integer decreased to 2nd
        y,z=input().split()
        bh=bhp.decrease(bh,int(y),int(z))
    if x=="del":        #next line should contain key to be deleted
        y=input()
        if len(bh)>0:
            bh=bhp.delkey(bh[0],int(y),bh)
print("print the heap:")
if len(bh)>0:bhp.display(bh[0])
