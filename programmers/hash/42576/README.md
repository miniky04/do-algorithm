링크 :
https://programmers.co.kr/learn/courses/30/lessons/42576

설명 : 
1. 변수설명 : 
   to_dic이라는 함수를 설명해보자면 , d라는 dictionary를 만들어서 source를 name에 집어넣으면서 d[name] = source.count(name) 즉, 이름: 이름이 나온 수 를 셀 수 있도록 하는 함수이다.
   d_p 는 to_dic(participant) 즉, 참가자 수를 센다. 참가자 이름: 동명이인수
   d_c 는 d_p와 마찬가지로 to_dic(completion) 즉, 성공한 사람 수를 센다. 성공한 사람 이름: 동명이인수
2. 코드설명 : 
   코드 설명을 solution 함수 부터 해보자면,
   solution(particpant, completion)을 하면 실패한 사람 이름을 출력하는 함수이다.
   d_p와 d_c변수를 to_dic함수를 이용해 만들어두고
   d_p.keys() 즉 name값을 name이라는 변수에 넣어준다.
   if 문으로 d_c 성공한 사람 수도 name에 넣었을 때 d_p[name] -= d_c[name] 즉, 참가한 사람 이름 수에서 성공한 사람 이름 수만큼 빼준다.
   if문에 해당하지 않을 때 name값을 반환한다.
   for문이 끝나면 x = d_p.items()라고 생각하고 lambda x: x[1] > 0, 해서 남아있는 사람을 filter하고 dict로 형식을 바꿔서 keys()로 값을 출력해낸 것을 list로 바꾼다음 거기서 [0]번째 값을 반환한다
   
3. 주의할 점 :
동명이인을 조심해야한다. 
   예를들어 참가자[min,min,gye,hye,min] 이고 성공한사람[min,min,hye,gye]이면 min이라는 사람이 2명이 성공한것이니 참가자수에서 min이라는 사람 2명을 제거해준다.
   