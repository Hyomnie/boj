def d(n):
  ans=n
  while n:
    ans+=n%10
    n=int(n/10)
  return ans

l=[]
for i in range(1,10001):
  l.append(d(i))

for i in range(1,10001):
  if i not in l:
    print(i)
