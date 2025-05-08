# pip install matplotlib
# 설치한 라이브러리 목록 확인 / 저장 : pip freeze > requirements.txt
# 라이브러리 설치 : pip install -r requirements.txt 

# https://matplotlib.org/
# https://www.w3schools.com/python/matplotlib_subplot.asp

import matplotlib.pyplot as plt
import numpy as np

# Scatter
x = np.random.randint(1, 100, size = 30)
y = np.random.randint(1, 100, size = 30)

plt.scatter(x, y) # 랜덤한 점을 찍음
plt.show()

# Plot
data = {'X data' : [1, 2, 3, 4, 5],'Y data' : [2, 4, 8, 10, 3]}

plt.plot('X data', 'Y data', data = data) # data['X data']와 data['Y data']를 연결한 선을 그림
plt.show()

# Plot with Label
plt.plot('X data', 'Y data', data = data)
plt.xlabel('X Lable', labelpad=10) # labelpad : label과 축 사이의 간격
plt.ylabel('Y Label', labelpad=10) # labelpad : label과 축 사이의 간격
plt.show()

# Legend
plt.plot('X data', 'Y data', data = data, label = 'My Data') # label : 범례에 표시할 이름
plt.xlabel('X Lable', labelpad=10, fontdict={'color': 'red'}, loc='right') # loc : 위치
plt.ylabel('Y Label', labelpad=10, fontdict={'color': 'blue'}, loc='top')
plt.legend() # 범례 표시
plt.show()

# 2개의 데이터(꺽은 선)
plt.plot([1, 2, 3, 4], [2, 3, 7, 9], linestyle='dashed', marker='o', label='Up') # linestyle : 선의 종류, marker : 점의 종류
plt.plot([1, 2, 3, 4], [9, 6, 5, 2], linestyle='dotted', label='Down') 
plt.xlabel('Up Data') # x축 이름
plt.ylabel('Down Data') # y축 이름
plt.grid(True) # 격자 표시
plt.title('Up & Down') # 제목
plt.legend(loc='best', ncol=2, fontsize=10, frameon=True, shadow=True) # 범례 표시, ncol : 열의 개수, fontsize : 글자 크기, frameon : 테두리 표시, shadow : 그림자 표시

plt.show()

# 막대 그래프
x = np.arange(3) # [0, 1, 2]
years = ['2021', '2022', '2023'] # x축 레이블
values = [100, 200, 500] # y축 값

plt.bar(x, values) # 막대 그래프
plt.xticks(x, years) # x축 레이블 설정
plt.show()

y = np.arange(3) # [0, 1, 2]
plt.barh(y, values) # 수평 막대 그래프
plt.yticks(y, years) # y축 레이블 설정
plt.show()

# 파이 챠트
ratio = [10, 30, 40, 20] # 비율
labels = ['chris', 'tommy', 'harry', 'hans'] # 레이블
explode = [0, 0.10, 0, 0.10] # 각 사이 간격

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode) # autopct : 비율 표시, startangle : 시작 각도, counterclock : 시계 방향으로 그리기, explode : 조각 강조
plt.show()

# 이미지로 저장
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
plt.savefig('pie.png') # 이미지 저장

# 객체지향 인터페이스 사용
x = np.arange(1, 5)     # [1, 2, 3, 4]

fig, ax = plt.subplots(2, 2) # 2행 2열의 서브플롯 생성
ax[0][0].plot(x, np.sqrt(x))     # left-top
ax[0][1].plot(x, -x)             # right-top
ax[1][0].plot(x, 2*x)            # left-bottom
ax[1][1].plot(x, 3*x)            # right-bottom

plt.show()
