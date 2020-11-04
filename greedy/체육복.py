def solution(n, lost, reserve):
    answer = n-len(lost)
    slost = set(lost)-set(reserve)
    srese = set(reserve)-set(lost)
    for i in srese:
        if i-1 in slost:
            slost.remove(i-1)
        elif i+1 in slost:
            slost.remove(i+1)
    answer=n-len(slost)
    return answer
