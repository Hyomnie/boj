word=input()
word=word.lower()
alpha=[0 for i in range(26)]
for i in word:
  alpha[ord(i)-97]+=1
if alpha.count(max(alpha))>1:
  print('?')
else:
  mindex=alpha.index(max(alpha))
  print(chr(mindex+97).upper())
