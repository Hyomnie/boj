n=int(input())
l=[]
length=[]
for i in range(n):
  word=input()
  if (len(word),word) in l:
    continue
  l.append((len(word),word))
l=sorted(l)
for i in range(len(l)):
  print(l[i][1])
