import random

food = ['짜장', '짬뽕', '볶음밥']

for i in range(100):
    #print(f'{i+1}. hello world')

    a = input('짜장면먹을래 짬뽕먹을래? : ')

    #짜장 or 짬뽕 둘 중 하나를 고르면
    if a == '짜장' or a == '짬뽕':
        print('선택한 메뉴 : ' + a)
        #가능한 메뉴인지
        print('나오나? 나오면 TRUE')
        #food[]에서 랜덤으로 골라주기
        print('추천메뉴 : ' + random.choice(food))
    #고른 음식이 짜장, 짬뽕이 아닐 경우
    else:
        print('짬짜면 먹어')