'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 집합 set()
'''

# 빈 집합 생성
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2, 1, 3}
print("집합1 : ", number1)   # 내가 입력한 순서대로 출력을 해주지 않는다.

# 리스트로부터 집합 생성.
number2 = set([1, 2, 3, 1, 2])
print("집합2 : ", number2)      # 순서가 없다. + 중복을 허용하지 않는다.

# 문자열을 집합으로 생성.
text1 = set("asdfasdf")
print("text1 : ", text1)       # 순서가 없다. + 중복을 허용하지 않는다.

numbers = {2,4,5,1,2}
if 1 in numbers :   # 1이 집합 안에 있는가?
    print("집합에 1이 있습니다.")   # 있다면 출력이 된다.
    
# 집합은 순서가 없어서 index로 접근이 불가능하다.
# 반복문으로 접근하여 출력 가능하다.
numbers = {9,1,5,2,4,7,6,3,4,9,1}   # 중복하여 생성한 경우 밑에 문장으로 덮어쓰기가 된다.
for num in numbers :   # 집합을 반복하는 동안
    print(num, end=' ')    # 중복을 허용하지 않고 정렬하여 출력한다.
    
print()

# 정렬 후 출력하기
for num in sorted(text1) :
    print(num, end=' ')

print()

# 추가하기
numbers.add(100)    # 랜덤으로 집합 안에 추가한다.
print(numbers)     # 집합 전체를 출력한다.

for num in sorted(numbers) :    # 추가한 후 집합을 정렬하여 각 원소만 출력한다.
    print(num, end=' ')
    
print()

# 삭제하기
numbers.remove(100)
for num in sorted(numbers) :    # 삭제한 후 집합을 정렬하여 각 원소만 출력한다.
    print(num, end=' ')
