def solution(name):
    answer = 0
    a=[min(ord(i)-65, 91-ord(i)) for i in name]
    i=0
    while True:
        answer+=a[i]
        a[i]=0
        if sum(a)==0:
            break
        l,r=(1,1)
        while a[i-l]<=0:
            l+=1
        while a[i+r]<=0:
            r+=1
        if l<r:
            answer+=l
            i-=l
        else:
            answer+=r
            i+=r
    return answer

#좌우로 스틱 이동하는 것이 어려웠다
