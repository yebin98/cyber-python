# Dictionary의 특징과 기본 사용법
var = {'name' : 'chris', 'age' : 23, 1 : ['a' , 'b', 'c']}
print(var) # {'name': 'chris', 'age': 23, 1: ['a', 'b', 'c']}
print(var['name']) # chris

var['age'] = 33
print(var) # {'name': 'chris', 'age': 33, 1: ['a', 'b', 'c']}
del var[1] # 1이라는 key를 삭제
print(var) # {'name': 'chris', 'age': 33}
var[1] = 'Hi' # 1이라는 key에 'Hi'라는 value를 추가
print(var) # {'name': 'chris', 'age': 33, 1: 'Hi'}

var.update({'name' : 'hans', 'age' : 30})
print(var) # {'name': 'hans', 'age': 30, 1: 'Hi'}

data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = {'3rd' : 'hans', '4th' : 'james', '5th' : 'jenny'}
var = {**data_1, **data_2} # Python 3.5 이상에서만 사용 가능
print(var) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'hans', '4th': 'james', '5th': 'jenny'}
var = data_1 | data_2   # Python 3.9 이상에서만 사용 가능
print(var) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'hans', '4th': 'james', '5th': 'jenny'}

# 얕은 복사와 깊은 복사
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1 # 얕은 복사
print(data_1) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
print(data_2) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
data_1['1st'] = 'hans'
print(data_1) # {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}
print(data_2) # {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}
# 얕은 복사는 같은 메모리 주소를 참조하기 때문에 data_1의 값을 변경하면 data_2의 값도 변경된다.

data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1.copy() # 깊은 복사
print(data_1) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
print(data_2) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
data_1['1st'] = 'hans' # data_1의 값을 변경
print(data_1) # {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}
print(data_2) # {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}

# Dictionary Comprehension의 특징과 예
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var) # {'chris': 10, 'tommy': 30, 'harry': 20}
var = { name : age for name, age in var.items() if age < 20}
print(var) # {'chris': 10}

# Dictionary 관련 함수 
# keys() : Dictionary의 key를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var.keys()) # dict_keys(['chris', 'tommy', 'harry'])

# values() : Dictionary의 value를 반환
print(var.values()) # dict_values([10, 30, 20])

# items() : Dictionary의 key와 value를 반환 
print(var.items()) # dict_items([('chris', 10), ('tommy', 30), ('harry', 20)])

# clear() : Dictionary의 모든 값을 제거
var.clear()
print(var) # {}

# get() : Dictionary의 특정 key의 value를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print('chris' in var) # True
print(var.get('chris')) # 10
print('hans' in var) # False
print(var.get('hans')) # key가 없을 경우 None을 반환한다.
print(var.get('hans', 'hans is not in var')) # 기본값을 설정할 수 있다. # hans is not in var

# Dictionary의 활용
# 다양한 루프 테크닉
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
for k, v in var.items():
    print(k, v) # chris 10 tommy 30 harry 20

for i, v in enumerate(['chirs', 'tommy', 'harry']): # enumerate() : 리스트의 index와 value를 반환
    print(i, v) # 0 chirs 1 tommy 2 harry
    
name = ['chris', 'tommy', 'harry']
age = [10, 30, 20]
for k, v in zip(name, age): # zip() : 두 개의 리스트를 묶어준다.
    print(k, v) # chris 10 tommy 30 harry 20
    
# Json과 Dictionary 변환
import json

var = '{"chris" : 10, "tommy" : 30, "harry" : 20}' # Json 형식의 문자열
print(var) # {"chris" : 10, "tommy" : 30, "harry" : 20}
print(type(var)) # <class 'str'>

var = json.loads(var) # Json 형식의 문자열을 Dictionary로 변환
print(var) # {'chris': 10, 'tommy': 30, 'harry': 20}
print(type(var)) # <class 'dict'>

var = json.dumps(var) # Dictionary를 Json 형식의 문자열로 변환
print(var) # {"chris": 10, "tommy": 30, "harry": 20}
print(type(var)) # <class 'str'>

    