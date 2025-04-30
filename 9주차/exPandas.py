# pip install pandas
import pandas as pd

############################################################
# 리스트 / 딕셔터리-> 시리즈(Series)
series = pd.Series([100, 90, 80], index=['KOR', 'MATH', 'ENG'])
#series = pd.Series({'KOR':100, 'MATH':90, 'ENG':80})
series.name = '점수'
series.index.name = '과목'

print(series)
print('index : {}'.format(series.index))
print('values : {}'.format(series.values))

# 딕셔너리 -> 데이터프레임(DataFrame)
data = {'Subject':['KOR', 'MATH', 'ENG'], 'Score':[100, 90, 80]}
dataFrame = pd.DataFrame(data)

print(dataFrame)
print('index : {}'.format(dataFrame.index))
print('columns : {}'.format(dataFrame.columns))
print('values : {}'.format(dataFrame.values))
print('dataFrame[\'Subject\'] : {}'.format(dataFrame['Subject']))
print('dataFrame[\'Score\'] : {}'.format(dataFrame['Score']))

print('dataFrame[0:2] : {}'.format(dataFrame[0:2]))
print('dataFrame.iloc[:2] : {}'.format(dataFrame.iloc[:2])) # 행번호로 접근
print('dataFrame.loc[:2] : {}'.format(dataFrame.loc[:2])) # 인덱스 이름으로 접근

print('dataFreme[\'Subject\'][0] : {}'.format(dataFrame['Subject'][0]))

print(dataFrame[dataFrame['Score'] >= 90])
print(dataFrame.loc[dataFrame['Score'] >= 90, ['Subject']])

print(dataFrame.describe())

dataFrame['Score'] = 100
print(dataFrame)

dataFrame['Score'] = [100, 90, 80]
dataFrame['Grade'] = ['A+', 'A', 'B']
print(dataFrame)
print(dataFrame[['Subject','Grade']])

del dataFrame['Score']
print(dataFrame)

dataFrame.drop(['Grade'], axis=1) # axis=0: 행, axis=1: 열 drop 기존부분 변경 안됨
print(dataFrame)

dataFrame.drop(['Grade'], axis=1, inplace=True) # inplace=True: 기존부분 변경
print(dataFrame)

dataFrame.drop(dataFrame[dataFrame['Subject'] == 'KOR'].index, inplace=True)
print(dataFrame)

############################################################
# 엑셀(cvs) 파일 사용하기
dataFrame = pd.read_csv('grade.csv')

print(dataFrame.head()) # 처음 5개 행
print(dataFrame.tail()) # 마지막 5개 행
print(dataFrame)
print(dataFrame.describe()) # 통계정보

result=pd.crosstab(index=dataFrame.GRADE, columns="count", margins=True) # 교차표
print(result)

dataFrame = dataFrame[dataFrame['GRADE'] == 'A'] # A학점만 남기기
print(dataFrame)

dataFrame['MEAN'] = (dataFrame['KOR'] + dataFrame['MATH']) / 2 # 평균점수 추가
print(dataFrame)

dataFrame.drop(['GRADE'], axis=1, inplace=True) # GRADE 열 삭제
dataFrame.to_csv('gradeA.csv', index=False) # index=False: 인덱스 번호를 기록하지 않음


