# type : 문자열 자료형 확인
str = 'Hello World'
print(type(str)) # <class 'str'>

# len : 문자열 길이
str = 'Hello World'
print(len(str)) # 11

# count : 문자 개수 세기
str = 'Hello World'
print(str.count('l')) # 3

# find : 문자열 찾기, 위치 반환
str = 'Hello My World'
print(str.find('My')) # 있으면 위치 반환 # 6
print(str.find('Your')) # 없으면 -1 반환

# rfind : 문자열을 뒤에서 부터 찾기, 위치 반환
str = 'Hello My World'
print(str.rfind('H')) # 0
print(str.rfind('r')) # 11

# index : 문자열 찾기, 위치 반환 (없으면 예외 발생)
str = 'Hello My World'
try:
    print(str.index('Your'))
except ValueError as e:
    print(e) # substring not found
    
# join : 문자열 삽입
str = '-'.join('Hello')
print(str) # H-e-l-l-o

# upper : 대문자로 변환
str = 'Hello World'
print(str.upper()) # HELLO WORLD

# lower : 소문자로 변환
str = 'Hello World'
print(str.lower()) # hello world

# lstrip : 왼쪽 공백 제거
str = '    Hello World   '
print(str.lstrip()) # Hello World

# rstrip : 오른쪽 공백 제거
str = '    Hello World   '
print(str.rstrip()) #    Hello World

# strip : 양쪽 공백 제거
str = '    Hello World   '
print(str.strip()) # Hello World

# replace : 문자열 변경(바꾸기)
str = 'Hello My World'
print(str.replace('My', 'Your')) # Hello Your World

# split : 문자열 나누기
str = 'Hello My World'
print(str.split(' ')) # ['Hello', 'My', 'World']

str = 'Hello-Your-World'
print(str.split('-', 1)) # ['Hello', 'Your-World']

# zfill : 문자열의 길이가 지정된 숫자가 될 대까지 0으로 문자열 채우기
str = 'Start'
print(str.zfill(10)) # 00000Start

# rjust : 문자열의 길이가 지정된 숫자가 될 때까지 지정된 값으로 채우기 (왼쪽)
str = 'Start'
print(str.rjust(10, '1')) # 11111Start

# ljust : 문자열의 길이가 지정된 숫자가 될 때까지 지정된 값으로 채우기 (오른쪽)
str = 'Start'
print(str.ljust(10, '1')) # Start11111

# center : 문자열의 길이가 지정된 숫자가 될 대까지 지정된 값으루 채우기 (양쪽)
str = 'Start'
print(str.center(10, '-')) # --Start----

# 문자열을 뒤집어 저장하는 방법 (1)
str = 'Hello World'
reversed_str = ''
for c in str:
    reversed_str = c + reversed_str
print(reversed_str) # dlroW olleH

# 문자열을 뒤집어 저장하는 방법 (2)
str = 'Hello World'
str_list = list(str)
str_list.reverse()
reversed_str = ''.join(str_list)
print(reversed_str) # dlroW olleH

# 문자열을 뒤집어 저장하는 방법 (3) - 슬라이싱의 마지막 숫자는 방법, -1은 뒤에서 부터
str = 'Hello World'
reversed_str = str[::-1]
print(reversed_str) # dlroW olleH
