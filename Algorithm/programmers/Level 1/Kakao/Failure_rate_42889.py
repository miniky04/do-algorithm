'''
n = 스테이지 개수
stages 는 이용하는 사용자가 어디 스테이지에 머물러있는지
result 는 실패율이 높은 순으로 적어둔 것(내림차순) 만약 실패율이 동점이면 스테이지 낮은순으로

실패율을 구하는 방법
스테이지 수 세는 법 : count()
스테이지 수 / len(stages)
'''


def solution(N, stages):
    key_list = []
    fail = {}
    length = len(stages)
    for i in range(1, N + 1):
        stage_count = stages.count(i)
        if length == 0:
            fail[i] = 0
        else:
            fail[i] = stage_count / length
            length -= stage_count
    # 정렬 기준이 item[1] = value 니까 value 로 정렬하겠다  ,, ?
    fail2 = sorted(fail.items(), reverse=True, key=lambda item: item[1])  # 내림차순
    # print(fail2) [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)]
    for i in range(N):
        key_list.append(fail2[i][0])
    return key_list


n = 4
stage = [4, 4, 4, 4, 4]
print(solution(n, stage))
