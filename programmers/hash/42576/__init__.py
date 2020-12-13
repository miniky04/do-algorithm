def solution(participant, completion):
    d_p = to_dic(participant)
    d_c = to_dic(completion)
    for name in d_p.keys():
        if name in d_c:
            d_p[name] -= d_c[name]
        else:
            return name  # 완주한 사람 목록에 해당 사람이 없을 때
    return list(dict(filter(lambda x: x[1] > 0, d_p.items())).keys())[0]
#쌍을 x로 받아서 x값에서 인덱스 1이 0보다 크다 -> 이름에 있는 개수가 0보다 큰 것을 filter
#그 결과를 dict로 만들어서 keys()값을 뽑아내면 필터링된 결과의 쌍이 나오는 데 그 쌍 중 keys() 즉, 이름만 가져온다.
#다시 list로 바꾸어서 인덱스0값을 반환


def to_dic(source):
    d = {}
    for name in source:
        d[name] = source.count(name)
        # if name in d:
        #     d[name] += 1
        # else:
        #     d[name] = 1
    return d


p = ['mislav', 'stanko', 'mislav', 'ana']
c = ['stanko', 'ana', 'mislav']
print(solution(p, c))