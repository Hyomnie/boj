import sys

st=[]
n=int(sys.stdin.readline().rstrip())
for x in range(n):
    a=sys.stdin.readline().rstrip().split()
    
    if a[0]=='push':
        st.append(int(a[1]))
    elif a[0]=='pop':
        if not st:
            print(-1)
        else:
            print(st.pop())
    elif a[0]=='size':
        print(len(st))
    elif a[0]=='top':
        if not st:
            print(-1)
        else:
            print(st[len(st)-1])
    elif a[0]=='empty':
        if not st:
            print(1)
        else:
            print(0)

#시간초과 안 나는 게 중요하다.
