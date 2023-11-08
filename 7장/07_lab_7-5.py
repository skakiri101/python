'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : LAB 7-5 함수는 튜플을 돌려줄 수 있다.
    
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.(return)
        
        [함수]
            3. 반지름을 받아서 매개변수에 저장한다.
            4. 넓이와 둘레를 계산한다.
            5. 넓이와 둘레를 돌려준다.(함수를 호출한 곳으로)
                return 넓이, 둘레
            
        [메인]
            1. 반지름을 입력 받는다.
            2. 함수 호출 -> 반지름을 가지고 호출한다.
            6. 돌려 받은 넓이와 둘레를 저장한다.
            7. 출력한다.
'''

import math   # 파이값 가져오기.

# 함수 선언
def Circle(redius):
    Area = math.pi * redius**2   # 넓이 계산
    Circumference = 2*math.pi * redius   # 둘레 계산
    return Area, Circumference  # 넓이와 둘레의 값을 튜플로 반환 함

# 반지름을 입력 받는다.
r = float(input("반지름을 입력하세요 : "))    

# 출력한다.
(Area, Circumference) = Circle(r)   # 튜플에 저장한다.
print(f"반지름이 {r}인 원의 넓이는 {Area:.2f}이고, 원의 둘레는 {Circumference:.2f}이다.")

circle = Circle(r)  # 변수에 저장한다.
print(f"반지름이 {r}인 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f}이다.")



