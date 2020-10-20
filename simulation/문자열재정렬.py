n=input()
count=0
m=[]
for i in range(len(n)):
  if n[i].isdigit(): #숫자이면
    count+=int(n[i])
  else:
    m.append(n[i])
x=''.join(sorted(m)) #알파벳 오름차순으로 정렬
x=x+str(count)
print(x)
