n=int(input())
x=[]
for i in range(n):
  a,b=map(int, input().split())
  x.append((a,b))
x=sorted(x)
for i in range(n):
 print(x[i][0], x[i][1])
