n=int(input())
cnt=0
for i in range(n):
  word=input()
  for j in range(1, len(word)):
    if word.find(word[j-1])>word.find(word[j]):
      cnt+=1
      break
print(n-cnt)

#다시 풀어볼 것
