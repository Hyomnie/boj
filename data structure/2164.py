from collections import deque
import sys

input = sys.stdin.readline
n=int(input())
queue=deque()
for i in range(1,n+1):
  queue.append(i)

while True:
  if len(queue)==1:
    break
  queue.popleft()
  x=queue.popleft()
  queue.append(x)

print(queue[0])
