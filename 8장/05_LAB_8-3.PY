'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 집합의 연산
'''

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))  # 교집합 메소드 intersection()

# 도전문제 8-3
print("파티 A, B에 참석한 사람들 :", partyA.union(partyB))     # 합집합 메소드 union()

print("파티 A, B에 중복없이 참석한 사람 :", partyA.symmetric_difference(partyB))     # 대칭 차집합 메소드 symmetric_difference()

print("파티 A에만 참석한 사람 :", partyA.difference(partyB))     # 차집합 메소드 difference()


