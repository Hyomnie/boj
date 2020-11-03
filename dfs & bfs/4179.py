from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
  while que1:
    x,y=que1.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<r and 0<=ny<c:
        if dist1[nx][ny]<0 and graph[nx][ny]!='#':
          dist1[nx][ny]=dist1[x][y]+1
          que1.append((nx,ny))
 
  while que2:
    x,y=que2.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=r or ny<0 or ny>=c:
        print(dist2[x][y]+1)
        return
      if dist2[nx][ny]>=0 or graph[nx][ny]=='#':
        continue
      if dist1[nx][ny]!=-1 and dist1[nx][ny]<=dist2[x][y]+1:
        continue
      dist2[nx][ny]=dist2[x][y]+1
      que2.append((nx,ny))
  print('IMPOSSIBLE')

r,c=map(int,input().split())
graph=[]
dist1=[[-1]*c for _ in range(r)]
dist2=[[-1]*c for _ in range(r)]
que1=deque()
que2=deque()
for i in range(r):
  row=list(input().strip())
  graph.append(row)

for i in range(r):
  for j in range(c):
    if graph[i][j]=='F':
      que1.append((i,j))
      dist1[i][j]=0
    if graph[i][j]=='J':
      que2.append((i,j))
      dist2[i][j]=0
bfs()

#어려워,,,
