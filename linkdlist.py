class Node:
    def __init__(self, value):
        self.value=value
        self.nxt=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,number):
        mamba=Node(number)          #head=a1,mamba=a2       #head=a2
        mamba.nxt=self.head         #a2->a1                #a3->a2    //a3-a2-a1
        self.head=mamba               #head=address(a2)      #head=a3
    def pop(self):
        if(self.head!=None):
            x=self.head.value
            self.head=self.head.nxt
            return x
        else: return "empty"
    def pnt(self):
        temp=self.head
        while(temp!=None):
            print(temp.value)
            temp=temp.nxt


listt=LinkedList()
for i in range(0,100):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if x==0:
        listt.push(y)
        #listt.pnt()
    elif x==1:
        print(listt.pop())
        #list.pnt()
    elif x==2: listt.pnt()
    else: break