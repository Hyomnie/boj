from collections import deque

def bfs(n,m,graph):
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  queue=deque()
  days=-1
  for i in range(n):
    for j in range(m):
      if graph[i][j]==1:
        queue.append((i,j))
  while queue:
    days+=1
    for _ in range(len(queue)):
      x,y=queue.popleft()
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
          graph[nx][ny]=1
          queue.append((nx,ny))
  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        return -1
  return days

m,n=map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(n)]
print(bfs(n,m,graph))
