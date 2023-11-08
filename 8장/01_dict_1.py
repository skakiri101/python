'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 8.1 키와 값을 가지는 딕셔너리
    
    튜플 = ()   리스트 = []   딕셔너리 = {}
'''

# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. 1. key, value    [key] = value
phone_book1['남태호'] = '010-9756-9377'

print("phone_book1 :", phone_book1)    # {"남태호": "010-9756-9377"}

# 딕셔너리에 값 저장. 2. {key ; value}
phone_book2 = {'남뚜비' : "010-1234-5678", "남태호" : "010-9756-9377"}
print("phone_book2 :", phone_book2)

phone_book3 = {}
phone_book3['남태호'] = '010-9756-9377'
phone_book3['남뚜비'] = '010-3311-2411'
phone_book3['뚜비뚜'] = '010-2411-3311'
phone_book3['뚜밥뚜'] = '010-2424-3311'
phone_book3['뚜비남'] = '010-2411-9377'

print("phone_book3 :", phone_book3)

print()

print(":: 전화번호 phone_book3 출력 ::")

# 모든 key 출력
print(phone_book3.keys())

# 모든 value 출력
print(phone_book3.values())

# 모든 key, value 출려
print(phone_book3.items())

print()

print(":: 전화번호 phone_book3 item()출력 ::")
for name, phone_num in phone_book3.items():
    print(name, ':', phone_num)
    
print()

for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])
    
print()

print("딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성")
person_dict =  {'name' : '남태호', 'age' : 20, 'class' : '1학년'}

print('name :', person_dict['name'])    # 딕셔너리의 'name' 키로 값을 조회하여 출력
print('age :', person_dict['age'])     # 딕셔너리의 'age' 키로 값을 조회하여 출력
print('class :', person_dict['class'])

print()

print(":: 정렬 ::")
# phone_book3 를 정렬
# 딕셔너를 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))

print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)

print(":: 값을 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print()

print(":: 항목 삭제 ::")
del phone_book3["남태호"]
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)