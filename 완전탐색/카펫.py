def solution(brown, yellow):
    answer = []
    i=yellow
    for i in range(yellow, int(yellow/i)-1, -1):
        if yellow%i!=0:
            continue
        if (i*2+((yellow/i)*2)+4) == brown:
            answer.append(i+2)
            answer.append(yellow/i+2)
            break
    return answer
    
    #다시 풀어볼 것.
