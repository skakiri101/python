'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : LAB 8-1 편의점 재고 관리 프로그램
'''
# 딕셔너리 생성
items = {"커피음료" : 7, "펜" : 3, "종이컵" : 2, "우유" : 1, "콜라" : 4, "책" : 5}

print()   # 한 줄 띄우기

# 물건 목록 출력
# print("제품 목록 :", items.keys() - "dict_keys")
print("제품 목록 :", end=' ')
for key in items.keys() :
    print(key, end=', ')

print()   # 한 줄 띄우기

# 물건 이름을 입력 받는다.
name = input("물건의 이름을 입력하시오 : ")

# 입력 받은 물건의 재고 출력
print("재고 :", items[name])