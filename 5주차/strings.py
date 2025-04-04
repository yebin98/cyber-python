# type : 문자열 자료형 확인
str = 'Hello World'
print(type(str))

# len : 문자열 길이
str = 'Hello World'
print(len(str))

# count : 문자 개수 세기
str = 'Hello World'
print(str.count('l'))

# find : 문자열 찾기, 위치 반환
str = 'Hello My World'
print(str.find('My'))
print(str.find('Your')) # 없으면 -1 반환

# rfind : 문자열을 뒤에서 부터 찾기, 위치 반환
str = 'Hello My World'
print(str.rfind('o'))

# index : 문자열 찾기, 위치 반환 (없으면 예외 발생)
str = 'Hello My World'
try:
    print(str.index('Your'))
except ValueError as e:
    print(e)
    
# join : 문자열 삽입
str = '-'.join('Hello')
print(str)

# upper : 대문자로 변환
str = 'Hello World'
print(str.upper())

# lower : 소문자로 변환
str = 'Hello World'
print(str.lower())

# lstrip : 왼쪽 공백 제거
str = '    Hello World   '
print(str.lstrip())

# rstrip : 오른쪽 공백 제거
str = '    Hello World   '
print(str.rstrip())

# strip : 양쪽 공백 제거
str = '    Hello World   '
print(str.strip())

# replace : 문자열 변경(바꾸기)
str = 'Hello My World'
print(str.replace('My', 'Your'))

# split : 문자열 나누기
str = 'Hello My World'
print(str.split(' '))

str = 'Hello-Your-World'
print(str.split('-', 1))

# zfill : 문자열의 길이가 지정된 숫자가 될 대까지 0으로 문자열 채우기
str = 'Start'
print(str.zfill(10))

# rjust : 문자열의 길이가 지정된 숫자가 될 때까지 지정된 값으로 채우기 (왼쪽)
str = 'Start'
print(str.rjust(10, '1'))

# ljust : 문자열의 길이가 지정된 숫자가 될 때까지 지정된 값으로 채우기 (오른쪽)
str = 'Start'
print(str.ljust(10, '1'))

# center : 문자열의 길이가 지정된 숫자가 될 대까지 지정된 값으루 채우기 (양쪽)
str = 'Start'
print(str.center(10, '-'))

# 문자열을 뒤집어 저장하는 방법 (1)
str = 'Hello World'
reversed_str = ''
for c in str:
    reversed_str = c + reversed_str
print(reversed_str)

# 문자열을 뒤집어 저장하는 방법 (2)
str = 'Hello World'
str_list = list(str)
str_list.reverse()
reversed_str = ''.join(str_list)
print(reversed_str)

# 문자열을 뒤집어 저장하는 방법 (3) - 슬라이싱의 마지막 숫자는 방법, -1은 뒤에서 부터
str = 'Hello World'
reversed_str = str[::-1]
print(reversed_str)
