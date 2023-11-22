'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : LAB 9-2 : 트위터 처리의 단어 추출
        띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
'''

text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
        It’s because when we show up, things change."
        
# 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
print(text.split())     # 공백을 기준으로 문자열을 분리(리스트로 출력된다.)

print('world count :',len(text.split()))   # 분리된 문자열을 이용하여(리스트에서 각 원소의 개수를 구하면 된다.) 단어이 개수를 구한다.


# 도전문제 9-1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
    Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

# 1. ----------------------------
# 모든 문자를 소문자로 변환
# 소문자로 바뀐 단어들을 공백으로 구분한다.
# 구분된 단어를 검사한다.(판단) => 단어가 kt 또는 samsung 또는 lg 또는 skt 인가?
# 검사하는 단어가 회사명이면 **로 바꾼다.
# 아니면 그 단어는 그대로 사용한다.
low_text = text.lower() # 소문자 변환

text1 = ''
for word in low_text.split(' '):
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        text1 += '** '
    else:
        text1 += word + ' '
# 결과 출력
print(text1)

# 2. ----------------------------
# 모든 문자를 소문자로 변환
text_lower = text.lower()
print(text_lower)

# 소문자로 바뀐 단어들을 공백으로 구분하여 저장한다.
text_lower2 = text_lower.split()
print(text_lower2)

# 구분된 단어를 검사한다.(판단) => 단어가 kt 또는 samsung 또는 lg 또는 kst 인가?
print(text_lower2.index('kt'))
print(text_lower2.index('samsung'))
print(text_lower2.index('lg'))
print(text_lower2.index('skt'))

# 검사하는 단어가 회사명이면 **로 바꾼다.
# 아니면 그 단어는 그대로 리스트에 저장한다.
text_lower2[11] = '**' 
text_lower2[26] = '**' 
text_lower2[31] = '**' 
text_lower2[36] = '**'
print(text_lower2) 

# 분리된 단어들을 합친다.
# 출력한다.
print(' '.join(text_lower2))

# 3. GPT 검색 결과 ----------------------------
# 해당 단어 바꾸기.
text = text.replace('SKT', '**').replace('Samsung', '**').replace('LG', '**').replace('KT', '**')

print(text)

# 4. ----------------------------
# 문장을 소문자로 변경
text_lower = text.lower()

# 대체할 단어들을 리스트에 담기
replace_words = ['kt', 'samsung', 'skt', 'lg']

# 리스트에 있는 각 단어를 '**'로 대체
for word in replace_words:
    text_lower = text_lower.replace(word, '**')
    
print(text_lower)