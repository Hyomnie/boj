c=int(input())
for i in range(c):
  n=list(map(int, input().split()))
  avg=(sum(n)-n[0])/(len(n)-1)
  cnt=0
  for j in range(1,len(n)):
    if n[j]>avg:
      cnt+=1
  print(format(cnt/(n[0])*100,".3f"),end='%\n')
  
  #format 쓰는 문제
