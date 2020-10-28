def solution(n):
  ans=0
  for i in range(1,n+1):
    l=[]
    while i:
      l.append(i%10)
      i=int(i/10)
    if len(l)==1 or len(l)==2:
      ans+=1
      continue
    else:
      l.reverse()
      sub=l[1]-l[0]
      for j in range(1,len(l)-1):
        if l[j+1]-l[j]!=sub:
          break
        ans+=1
  return ans

print(solution(int(input())))
