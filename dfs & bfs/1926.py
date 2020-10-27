from collections import deque

n,m=map(int, input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int, input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
  a=1
  queue=deque()
  queue.append((x,y))
  graph[x][y]=0
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny]:
          a+=1
          queue.append((nx,ny))
          graph[nx][ny]=0
  return a

num,area=0,0

for i in range(n):
  for j in range(m):
    if graph[i][j]:
      num+=1
      area=max(area, bfs(i,j))
print(num)
print(area)

#왜 visited[] 쓰면 틀릴까?
