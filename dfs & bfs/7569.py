from collections import deque

def bfs(n,m,h,graph):
  dx=[-1,1,0,0,0,0]
  dy=[0,0,-1,1,0,0]
  dz=[0,0,0,0,-1,1]
  queue=deque()
  days=-1
  for k in range(h):
    for i in range(n):
      for j in range(m):
        if graph[k][i][j]==1:
          queue.append((i,j,k))
  while queue:
    days+=1
    for _ in range(len(queue)):
      x,y,z=queue.popleft()
      for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny]==0:
          graph[nz][nx][ny]=1
          queue.append((nx,ny,nz))
  for k in range(h):
    for i in range(n):
      for j in range(m):
        if graph[k][i][j]==0:
          return -1
  return days

m,n,h=map(int, input().split())
graph = [[[int(x) for x in input().split()] for _ in range(n)] for _ in range(h)]
print(bfs(n,m,h,graph))
