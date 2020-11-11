from collections import deque
import sys

def dfs(v):
  visited[v]=1
  print(v, end=' ')
  for i in range(1,n+1):
    if visited[i]==0 and graph[v][i]==1:
      dfs(i)

def bfs(v):
  queue=deque()
  queue.append(v)
  visited[v]=0
  while queue:
    x=queue.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
      if visited[i]==1 and graph[x][i]==1:
        queue.append(i)
        visited[i]=0


input=sys.stdin.readline
n,m,v=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
  x,y=map(int, input().split())
  graph[x][y]=1
  graph[y][x]=1
visited=[0 for _ in range(n+1)]

dfs(v)
print()
bfs(v)

#bfs 함수에서 visited 값이 반대인 이유는 dfs를 한 번 돈 후 다시 초기화하지 않았기 때문
