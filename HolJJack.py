# 컴퓨터가 홀짝문제 출제
# user가 홀짝 맞추기

import random

coin = int(input('몇 번 할래? : '))
holjjack = '홀', '짝'
score = 0

#coin만큼 반복
for i in range(coin):
    #a에 user 입력 받기
    print(f'{i+1} / {coin}')
    a = input("홀이게 짝이게 : ")
    #컴퓨터 문제 출제
    com = random.choice(holjjack)
    #문제랑 user 입력이 같으면
    if com == a:
        print('답 : ' + com)
        print('정답')
        score += 100
        print('현재 점수 : ' + str(score))
    #다르면
    else:
        print('답 : ' + com)
        print('실패')
        if score > 0:
            score -= 100
        else:
            score = score
        print('현재 점수 : ' + str(score))