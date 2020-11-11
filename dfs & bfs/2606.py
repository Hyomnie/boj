from collections import deque
import sys

def bfs(v):
  queue=deque()
  queue.append(v)
  visited[v]=1
  cnt=0
  while queue:
    x=queue.popleft()
    cnt+=1
    for i in range(1, com+1):
      if visited[i]==0 and graph[x][i]==1:
        visited[i]=1
        queue.append(i)
  print(cnt-1)

input=sys.stdin.readline
com=int(input())
node=int(input())
graph=[[0]*(com+1) for _ in range(com+1)]
for i in range(node):
  x,y=map(int, input().split())
  graph[x][y]=1
  graph[y][x]=1
visited=[0 for _ in range(com+1)]

bfs(1)

#cnt에서 빼는 1은 1번 컴퓨터이다
