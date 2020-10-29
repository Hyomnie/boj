n=int(input())
meeting=[]
for i in range(n):
  s,e=map(int,input().split())
  meeting.append((s,e))
meeting=sorted(meeting, key=lambda t: t[0])
meeting=sorted(meeting, key=lambda t: t[1])

cnt=0
start=0
for t in meeting:
  if t[0]>=start:
    start=t[1]
    cnt+=1
print(cnt)

#lambda 처음 써봤다
