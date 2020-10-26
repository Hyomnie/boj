n=int(input())
cnt=0
new=100
m=n
while new!=n:
  s=m//10 + m%10
  new=(m%10)*10 + s%10
  m=new
  cnt+=1
print(cnt)
