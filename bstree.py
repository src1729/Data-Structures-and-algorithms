class BST:
    def __init__(self,initval= None):
        self.value = initval
        self.left = None
        self.right = None

    def isEmpty(self):
        return (self.value == None)

    def maxval(self):
        if self.right == None:
            return self.value
        else:
            return (self.right.maxval())
    
    
    def INSERT(self,x):
        if self.isEmpty():
            self.value = x
            return
        elif x == self.value:
            return
        elif x < self.value :
            if self.left:
                self.left.INSERT(x)
            else:
                self.left = BST(x)
                return
        elif x > self.value:
            if self.right:
                self.right.INSERT(x)
            else:
                self.right = BST(x)
                return

    def find(self,x):
        if self.isEmpty():
            return False
        if x == self.value:
            return True
        if x < self.value:
            if self.left:
                return self.left.find(x)
            else:
                return False
        if x > self.value:
            if self.right:
                return self.right.find(x)
            else:
                return False              
    
    def REMOVE(self,x):
        if self.find(x) == False:
            return
        if x == self.value:
            if (self.left == None) and (self.right == None): #When it is a leaf
                self.value = None
            else:
                if self.left == None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                    return
                else:
                    self.value = self.left.maxval()
                    self.left.REMOVE(self.value)
                    return

        elif x < self.value:
    
                return self.left.REMOVE(x)
        elif x > self.value:
                return self.right.REMOVE(x)


    def sizetree(self):
        l = 0
        r = 0
        if self.isEmpty():
            return 0
        else:
            if self.left == None:
                l = 0
            elif self.right == None:
                r = 0
            if self.left:
                l += self.left.sizetree()
            if self.right:
                r += self.right.sizetree()
            return (1+ l + r)

    def SIZE(self,x):
        if self.find(x) == False:
            return None
        else:
            if x == self.value:
                return self.sizetree()
            elif x < self.value:
                return self.left.SIZE(x)
            elif x > self.value:
                return self.right.SIZE(x)
        
    def MAX(self,x):
        if self.find(x) == False:
            return None
        else:
            if x == self.value:
                return self.maxval()
            elif x < self.value:
                return self.left.MAX(x)
            elif x > self.value:
                return self.right.MAX(x)

 
n = int(input())
p = []
for i in range(n):
    a = list(map(str,input().split()))
    p = p + [a]

b = BST()
for i in range(n):
    if p[i][0] == "INSERT":
        b.INSERT(int(p[i][1]))
    if p[i][0] == "REMOVE":
        b.REMOVE(int(p[i][1]))
    if p[i][0] == "MAX" :
        print(b.MAX(int(p[i][1])))
    if p[i][0] == "SIZE" :
        print(b.SIZE(int(p[i][1])))
         #if self.left.value is None and self.right.value is None:
               # self.value=None