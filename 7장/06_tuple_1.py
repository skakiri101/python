'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
# 리스트 생성
color_list = ['red', 'green', 'blue', 'orange']

# 튜플 생성
color = ('red', 'green', 'blue', 'orange')

# 튜플 출력
print(f"color : {color}")

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# AttributeError: 'tuple' 개체에 'append' 속성이 없습니다
# 튜플은 추가, 삭제가 안된다.
# color.append('black') = X

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 : ', color)
print('color 튜플 중 2,3,4번은? ', color[1:4])     # range랑 같다고 생각하면 된다.
print('color 튜플 중 1,2,3번은? ', color[0:3])
# print('color 튜플 중 시작~3번(2번지까지)은? ', color[:3]) 도 가능하다.
print('color 튜플 중 3번~끝은? ', color[2:])
print('color 튜플 중 1,3,5번은? ', color[::2])  # 2씩 증가
print('color 튜플 거꾸로 출력은? ', color[::-1])  # 거꾸로 출력

# 튜플 끼리의 결함 => + 연산자, 반복 => * 연산자.
colors = color + color      # 튜플을 2번 출력한다. (튜플을 더한 수 만큼 출력한다.)
print('colors 튜플 : ', colors)
print('colors 튜플을 10번 반복 : ', color*10)   # 튜플을 10번 출력한다. 