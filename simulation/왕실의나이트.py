n=input()
row=int(n[1])
col=int(ord(n[0]))-int(ord('a'))+1
count=0
dx=[1, -1, 1, -1, 2, 2, -2, -2]
dy=[2, 2, -2, -2, 1, -1, 1, -1]
x,y=row,col

for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]
  if nx>=1 and ny>=1 and nx<=8 and ny<=8:
    count+=1

print(count)
