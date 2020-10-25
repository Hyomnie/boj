t=int(input())
for i in range(t):
  s=input()
  vps=[]
  for j in range(len(s)):
    if s[j]=='(':
      vps.append(1)
    elif s[j]==')':
      if 1 in vps:
        vps.remove(1)
      else:
        vps.append(2)
  if vps:
    print("NO")
  else:
    print("YES")
