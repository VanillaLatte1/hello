#print('hello world')
#print('짜장면이냐 짬뽕이냐')

#만약 짜장과 짬뽕과 볶음밥 세 개 중 하나 추천
#내가 짜장, 짬뽕, 볶음밥 중 하나를 적으면 짜장, 짬뽕, 볶음밥 중 추천
#아니면 둘다

import random

food = ['짜장', '짬뽕', '볶음밥']

a = input('짜장면먹을래 짬뽕먹을래? : ')

#짜장 or 짬뽕 둘 중 하나를 고르면
if a == '짜장' or a == '짬뽕':
    #가능한 메뉴인지
    print('나오나? 나오면 TRUE')
    #food[]에서 랜덤으로 골라주기
    print(random.choice(food))
#고른 음식이 짜장, 짬뽕이 아닐 경우
else:
    print('짬짜면 먹어')


# import random

# food = ['짜장', '짬뽕', '볶음밥']

# while True:
#     user = input('짜장, 짬뽕, 볶음밥 중 뭘 드시겠습니까? : ')
#     if user == food[0]:
#         print(food[0] + "으로 드리겠습니다. " + random.choice(food) + "은 어떠신가요?")
#     elif user == food[1]:
#         print(food[1] + "으로 드리겠습니다. " + random.choice(food) + "은 어떠신가요?")
#     elif user == food[2]:
#         print(food[2] + "으로 드리겠습니다. " + random.choice(food) + "은 어떠신가요?")
#     else:
#         print(food[0], food[1], food[2] + " 중 하나를 골라주십시오")





 