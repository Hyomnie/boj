from itertools import permutations
import math

def check(num):
    s=math.sqrt(num)
    if num<2:
        return False
    for i in range(2, int(s)+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        pool = list(map(''.join, permutations(numbers, i)))
        for j in list(set(pool)):
            if check(int(j)):
                answer.append(int(j))
    answer=len(set(answer))
    return answer
    
#다시 풀어볼 것.
