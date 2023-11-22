'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 문자열
'''

# 문자열 슬라이싱

s = 'Happy Day!'
print(s[0])     # 0번지를 짤라서 보여준다. -> H
print(s[6:10])      # 6 ~ 10번지 앞(9번지)까지 -> Day!
print(s[:-2])   # -2번지 앞(-1번지)까지 출력된다 -> Happy Da

# 문자열 분리 : split()
s = 'welcome to Python'
print(s.split())    # 공백을 기준으로 분리

s = '2023.11.15'
print(s.split('.')) # 분리 기준은 '.' 이다.

s = 'Hello, World'
print(s.split(','))     # 분리 기준은 ',' 이다. (공백도 문자열)
print(s.split(', '))    # 분리 기준 ', ' 이다. 

# 공백 제거 : strip()
s = 'Welcome, to, Python, and, bla, bla     '
print(s.strip())
print([x.strip() for x in s.split(',')])

print(list('Hello, World!'))    # 문자열 자르기 (공백도 문자열이라 잘린다.)

# 문자열 연결 : join()
print(','.join(['apple','grape','banana']))     # ,(쉼표)를 붙여서 연결하라.
print('-'.join('010.1234.5678'.split('.')))     # .으로 구분된 번호를 -로 고친다. ('.'을 기준으로 잘라서 '-'으로 연결하라.)

# . 을 -로 바꾸기
print('010.1234.5678'.replace('.','-'))

s = 'hello world!'
print(s)
# s에 저장된 문자열을 리스트로 문자열을 분리 시켜 slist에 저장.
slist = list(s)
print(slist)
# 분리된 문자를 다시 합치기
print(''.join(slist))   # 공백도 문자열이니 합치면 공백도 같이 합쳐진다.

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Have a Happy Day.'      # '\n'은 줄바꿈이고 '\t'는 탭이다.
print(a_string)

# 문자열 자르기 word_list에 저장.
word_list = a_string.split()
print(word_list)

# 다시 합치기 : 문자열을 자르고 다시 합치면 줄바꿈과 탭이 삭제됨.
refined_string = " ".join(word_list)
print(word_list)

# 대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s)
print(s.lower())     # lower은 모든 문자를 소문자로 변환
print(s.upper())     # upper는 모든 문자를 대문자로 변환

# 공백 제거 strip()
s = '    Hello, World!    '
print(s.strip())    # 왼쪽, 오른쪽 모든 공백 제거
print(s.lstrip())   # lstrip(left strip)은 왼쪽 공백 제거
print(s.rstrip())   # rstrip(right strip)은 오른쪽 공백 제거

s = '########Hello, World!########'
print(s)
print(s.lstrip('#'))    # 왼쪽 '#'문자만 제거

# 문자열 찾기
s = 'www.silla.ac.kr'
# .kr 찾기
print(s.find('.kr'))    # 12번지 출력(.부터 시작함으로 12번지부터 시작한다를 알림)
print(s.find('x'))      # -1 (문자열이 없다)

# . 이 몇 개 인가?
print(s.count('.'))

