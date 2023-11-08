'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대천', 1531)]

max_pop = city_info[0][1]      # 첫번째 항목이 기준
min_pop = city_info[0][1]   
total_pop = 0                   # 전체 인구 수 0으로 지정한다.

max_city = city_info[0][0]      # 첫번째 항목이 기준
min_city = city_info[0][0]

# 리스트에서 각각의 변수(도시명, 인구수)에 저장
for city, population in city_info:    # city_info 리스트를 반복한다.
    total_pop += population    # 반복하는 동안 city_info 리스트에 있는 튜플의 1번지를 더한다.
    if population > max_pop :  # 만약 튜플의 1번지가 0보다 크면
        max_pop = population   # 최대 인구 수는 튜플 1번지와 같다.
        min_city = city     # 
    if population < min_pop :
        min_pop = population
        min_city = city
        
print("최대인구: {0}, 인구: {1} 천명".format(max_city[0], max_city[1]))
print("최소인구: {0}, 인구: {1} 천명".format(min_city[0], min_city[1]))
print("리스트 도시 평균 인구: {0} 천명".format(total_pop / len(city_info)))