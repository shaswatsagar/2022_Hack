n=int(input("enter number of node"))
node=[]
for _ in range(n):
    node.append(int(input()))
e=int(input("enter the no of edges"))
edge=[]
for _ in range(e):
    edge.append( list(map(int,input().split(" "))))
print(edge)
adjM=[[] for _ in range(n+1)]
for i in edge:
    adjM[i[0]][i[1]]=1
    adjM[i[1]][i[0]]=1
print(adjM)
flag=True
while(True):
    print("ENTER 1 TO CHECK WHETHER NODES ARE CONNECTED OR NOT \n ENTER 0 TO EXIT ")
    value=int(input())
    if value==1:
        print("ENTER PAIR YOU WANT TO CHECK")
        print(adjM[int(input())][int(input())])
    else:
        flag=False