n=int(input())
l=[]

for i in range(n):
  age,name=input().split()
  l.append((int(age),i,name))
l=sorted(l)
for i in range(len(l)):
  print(l[i][0],l[i][2])
