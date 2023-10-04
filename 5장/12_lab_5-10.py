'''
    
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 조건에 따라 반복하는 while문
            교재 133 페이지

            문제 분석 : y가 입력 되면 계속 반복한다.
                       y 가 아니면 종료한다.
                       입력 받은 수의 합계를 계속 계산한다.
'''
sum = 0
answer = 'yes'

# 대답이 yes 이면 무한 반복
while answer == 'yes':
    num = int(input('숫자를 입력하시오: '))
    sum = sum + num
    answer = input("계속?(yes/no): ")
print("합계는 : ", sum)