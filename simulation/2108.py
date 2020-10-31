from collections import Counter
import sys
input=sys.stdin.readline

n=int(input())
num=[]
for i in range(n):
  num.append(int(input()))
num.sort()

print(round(sum(num)/n))
print(num[n//2])

freq=Counter(num).most_common()
if len(freq)>1:
  if freq[0][1]==freq[1][1]:
    print(freq[1][0])
  else:
    print(freq[0][0])
else:
  print(freq[0][0])
print(num[n-1]-num[0])

#최빈값 구하는 게 어려웠다. counter 쓰는 문제.
