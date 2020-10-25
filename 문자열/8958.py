t=int(input())
for i in range(t):
  s=input()
  score=0
  cnt=0
  for j in range(len(s)):
    if s[j]=='O':
      cnt+=1
      score+=cnt     
    else:
      cnt=0
  print(score)
