n=int(input())
stack=[]
ans=[]
cnt=1
temp=True
for i in range(n):
  num=int(input())
  while cnt<=num:
    stack.append(cnt)
    ans.append('+')
    cnt+=1
  if stack[-1]==num:
    stack.pop()
    ans.append('-')
  else:
    temp=False
if temp==True:
  for i in range(len(ans)):
    print(ans[i])
else:
  print("NO")
