'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 심화문제 8.6
            오늘의 마지막 문제
            해결 한 사람은 제출하고 수업 끝~!
'''
# 튜플을 이용한 리스트 생성
student_tuple = [('211101','강이안','010-123-1111'),('211102','박동민','010-123-2222'),('211103','김수정','010-123-3333')]

# student_tuple을 출력
print("student_tuple =", student_tuple)

# 빈 딕셔너리 생성
student_dict = {}

for id_num, name, phone in student_tuple :  # 튜플을 반복하는 동안
    student_dict[id_num] = [name, phone]    # 학번이란 변수에 이름이 저장된 변수를 저장한다.
    
for key, value in student_dict.items() :    # key와 value를 변수로 받아
    print(key, " : ", value[0])             # key라는 변수에 저장된 값과 이름 출력을 위해 value에 저장된 0번지 값을 출력한다.

# 학번 입력 받는다.
number = input("학번을 입력하세요 : ")

# 학번에 맞는 이름과 전화번호를 출력한다.
print(f"{number} 학생은 {student_dict[number][0]}이며, 전화번호는 {student_dict[number][1]}")

