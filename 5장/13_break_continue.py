'''
    
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 반복을 제어하는 break, continue
           교재 137 페이지

    Test word : programing
'''

# 단어(문자)를 입력받는다.
word = input("단어를 입력하세요 : ")

print(":: break1 ::")
for i in word :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :  # 즉 모음을 만나면 반복 중지.
        break
    else :
        print(i, end='')    # 결과 : or

print()

print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :  # 모음을 만나면 반복 중자.
        break  # 반복을 중단한다.  반복을 빠져 나간다.
    else :
        print(i, end='')

print()

print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] : 
        continue    # 반복의 처음으로 돌아간다. 아래 문장을 만날 수 없다.
    print(i, end='')    # 결과 예상