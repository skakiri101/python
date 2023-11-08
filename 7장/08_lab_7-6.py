'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395014 남태호
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대천', 1531)]

max_pop = 0     # 최대 인구 수(예를 들어 0이 아닌 10000인 경우 최대 값 10000보다 큰 값이 없어서 최대 값을 구하지 못하기 때문이다.)
min_pop = 999999999999999999    # 최소 인구 수(예를 들어 0이면 최소 값이 0보다 작은 값이 없어서 최소 값을 구하기 못하기 때문이다.)
total_pop = 0      # 전체 인구 수

max_city = None
min_city = None

# 튜플에서 담아서 저장
for city in city_info:    # city_info 리스트를 반복한다.
    total_pop += city[1]    # 반복하는 동안 city_info 리스트에 있는 튜플의 1번지를 더한다.
    if city[1] > max_pop :  # 만약 튜플의 1번지가 최대 인구 수 보다 크면
        max_pop = city[1]   # 최대 인구 수에 튜플 1번지 값을 저장
        max_city = city     # 최대 인구 도시에 변수값(city값)을 저장
    if city[1] < min_pop :  # 만약 튜플 1번지가 최소 인구 수 보다 작으면
        min_pop = city[1]   # 최소 인구 수에 튜플 1번지 값을 저장
        min_city = city     # 최소 인구 도시에 변수값(city값)을 저장

# 출력
print("최대인구: {0}, 인구: {1} 천명".format(max_city[0], max_city[1]))
print("최소인구: {0}, 인구: {1} 천명".format(min_city[0], min_city[1]))
print("리스트 도시 평균 인구: {0} 천명".format(total_pop / len(city_info)))
        
