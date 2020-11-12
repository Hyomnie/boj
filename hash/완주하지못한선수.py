def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]

#hash를 쓰는 것은 모르겠음. 일단 정렬로 풀었다.
