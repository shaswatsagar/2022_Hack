n=int(input("enter number of node"))
node=[]
for _ in range(n):
    node.append(int(input()))
e=int(input("enter the no of edges"))
edge=[]
for _ in range(e):
    edge.append(list(map(int,input().split(" "))))

adjL=[[] for _ in range(n+1)]
print(adjL)
for i in edge:
    adjL[i[0]].append(i[1])
    adjL[i[1]].append(i[0])
print(adjL)