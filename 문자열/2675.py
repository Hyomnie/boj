t=int(input())
for i in range(t):
  r, s=input().split()
  p=''
  for j in s:
    p+=int(r)*j
  print(p)
