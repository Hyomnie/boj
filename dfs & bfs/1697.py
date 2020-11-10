from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
dist=[-1 for _ in range(100002)]
dist[n]=0
q=deque()
q.append(n)
dx=[-1,1,2]
while dist[k]==-1:
  x=q.popleft()
  for i in range(3):
    if dx[i]==-1 or dx[i]==1:
      nx=x+dx[i]
    else:
      nx=x*dx[i]
    if 0<=nx<=100000:
      if dist[nx]==-1:
        dist[nx]=dist[x]+1
        q.append(nx)
print(dist[k])

#배열크기를 100001보다 크게 해야 런타임 에러를 피할 수 있다.
