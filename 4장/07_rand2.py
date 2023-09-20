'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 선택문 if~else
           random 을 이용한 가위바위보 게임.
           
           rnadom함수로 생성된 정수를 가지고 게임을 진행합니다.
           0 => 가위
           1 => 바위
           2 => 보
           뚜비
           두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random # random 함수 가져오기.(포함 시키기)

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("player1의 이름 : ")
player2 = input("player2의 이름 : ")

num1 = random.randrange(3) # player1의 랜덤 수
num2 = random.randrange(3) # player2의 랜덤 수

num = random.randrange(3) # 랜덤으로 0,1,2 생성하여 변수에 저장.

# player1의 가위 바위 보 출력
print(player1, " : ", end='')
if num1 == 0 :
    print("가위")
if num1 == 1 :
    print("바위")
if num1 == 2 :
    print("보")


# player2의 가위 바위 보 출력
print(player2, " : ", end='')
if num2 == 0 :
    print("가위")
if num2 == 1 :
    print("바위")
if num2 == 2 :
    print("보")

# 승자 판단하여 출력
if (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1) :
    print(f"{player1}이 이겼습니다.")
elif num1 == num2 :
    print("비겼습니다.")
else :
    print(f"{player2}가 이겼습니다.")

