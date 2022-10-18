
from heapq import heapify


class node:
    def __init__(self,data) -> None:
        self.data=data
        self.adres=None
class linkedList:
    def __init__(self) -> None:
        self.adres=None
    
    def PrintData(self):
        if self.adres==None:
            print("LINKED LIST IS EMPTY")
        else:
            temp=self.adres
            while(temp!=None):
                print(temp.data)
                temp=temp.adres

    def InsertAtEnd(self,data):
        if self.adres==None:
            self.adres=node(data)
        else:
            temp=self.adres
            while(temp.adres!=None):
                temp=temp.adres
            temp.adres=node(data)
    def atStart(self,data):
        temp=head.adres
        newNode = node(data)
        head.adres=newNode
        newNode.adres=temp
        


head=linkedList()
flag = True

while(flag):
    print("press 1 to view the list")
    print("Press 2 to insert at the end")
    n  = int(input("Enter"))

    if (n==1):
        head.PrintData()
        pass
    elif(n==2):
        data=input("Enter the data")
        head.InsertAtEnd(data)
    elif(n==3):
        flag=False
    else:
        print("invalid input")




