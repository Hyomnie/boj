def solution(number, k):
    answer = ''
    stack=[]
    
    for i in number:
        while len(stack)>0 and stack[-1]<i and k>0:
            k-=1
            stack.pop()
        stack.append(i)
    if k!=0:
        stack=stack[:-k]
    for i in stack:
        answer+=i
    return answer
