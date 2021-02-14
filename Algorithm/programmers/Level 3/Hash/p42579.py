def solution(genres, plays):
    answer = []
    for i in range(len(genres)):
        for j, gp in enumerate(zip(genres, plays)):
            print(j, gp)
        return answer


g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution(g, p))
