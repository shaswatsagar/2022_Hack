## binary Tree
class node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    def insertData(self,data):
        if self.data==None:
            self.data=data
        else:
            if data>self.data:
                if self.right==None:
                    self.right=node(data)
                else:
                    self.right.insertData(data)
                
            else:
                if self.left==None:
                    self.left=node(data)
                else:
                    self.left.insertData(data)
    
    def printData(self):
        if self.left:
            self.left.printData()
            print(self.data)
        else:
            print(self.data)
        if self.right:
            self.right.printData()



def inorder(Root):
    if Root:
        inorder(Root.left)
        print(Root.data)
        inorder(Root.right)

def postorder(Root):
    if Root:
        postorder(Root.left)
        postorder(Root.right)
        print(Root.data)
    
def preorder(Root):
    if Root:
        print(Root.data)
        preorder(Root.left)
        preorder(Root.right)
        print(Root.data)
        

Root=node()
flag = True

while(flag):
    print("press 1 to view the list")
    print("Press 2 to insert ")
    n  = int(input("Enter"))

    if (n==1):
        Root.printData()
    elif(n==2):
        data=input("Enter the data")
        Root.insertData(data)
    elif(n==3):
        flag=False
    else:
        print("invalid input")




