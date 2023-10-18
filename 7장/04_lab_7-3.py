'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''

# 리스트 생성
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

print("서울 인구:", population[1])
print("인천 인구:", population[3])
print("도시 리스트:", population[::2])
print("인구의 합:", sum(population[1::2]))