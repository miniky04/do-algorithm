링크 :
https://programmers.co.kr/learn/courses/30/lessons/42748

설명 : 
1. 변수설명 :
   array3 = 받아온 배열 변수
   command = [[i,j,k]] -> 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을때, k번째에 있는 수를 구한다.
   answer = 빈리스트
2. 코드설명 :
commands값을 command에 하나씩 담는다
   array3 은 array[i-1,j]을 하고나서 정렬한다.
   answer에 array3의 k-1번째 수를 출력한다.
   
3. 주의할 점 :