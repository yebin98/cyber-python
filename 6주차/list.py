# 리스트 자료구조의 특징과 기본적인 사용법
var = [1,'chris',['tommy', 'harry'], ('hans', 2)]
print(var) # [1, 'chris', ['tommy', 'harry'], ('hans', 2)]
print(var[3]) # ('hans', 2)
print(var[3][0]) # hans
print(var[-1]) # ('hans', 2)

var[0]=7
print(var[:2]) # [7, 'chris']

del var[3:]
print(var) # [7, 'chris', ['tommy', 'harry']]

print(len(var)) # 3

# 리스트의 연산
x = [1,2,3]
y = [4,5,6]
var = x + y
print(var) # [1, 2, 3, 4, 5, 6]

var = x * 2
print(var) # [1, 2, 3, 1, 2, 3]

# append() : 리스트의 마지막에 값을 추가
var = [1,2,3]
var.append(4)
print(var) # [1, 2, 3, 4]

# extend() : 리스트의 마지막에 리스트를 추가
var.extend([10,11,12])
print(var) # [1, 2, 3, 4, 10, 11, 12]

# insert() : 리스트의 특정 위치에 값을 추가
var.insert(0, 0)
print(var) # [0, 1, 2, 3, 4, 10, 11, 12]

# remove() : 리스트의 특정 값을 제거
var = var * 2
print(var) # [0, 1, 2, 3, 4, 10, 11, 12, 0, 1, 2, 3, 4, 10, 11, 12]
var.remove(4) # 리스트의 첫 번째 값만 제거
print(var) # [0, 1, 2, 3, 10, 11, 12, 0, 1, 2, 3, 4, 10, 11, 12]

# pop() : 리스트의 특정 위치의 값을 제거
var.pop()
print(var) # [0, 1, 2, 3, 10, 11, 12, 0, 1, 2, 3, 4, 10, 11]
var.pop(0)
print(var) # [1, 2, 3, 10, 11, 12, 0, 1, 2, 3, 4, 10, 11]

# count() : 리스트의 특정 값의 개수를 반환
print(var.count(2)) # 리스트에 2가 몇 개 있는지 반환 # 2

print(var) # [1, 2, 3, 10, 11, 12, 0, 1, 2, 3, 4, 10, 11]

# index() : 리스트의 특정 값의 인덱스를 반환
print(var.index(3)) # 리스트에 3이 몇 번째 인덱스에 있는지 반환 # 2
try:
    print(var.index(1)) # 0
except ValueError:
    print('ValueError')

# sort() : 리스트의 값을 정렬
import random
var = list()
for i in range(10):
    var.append(random.randint(1, 100))
print(var) # [30, 42, 68, 38, 85, 60, 45, 19, 94, 84]

var.sort()
print(var) # [19, 30, 38, 42, 45, 60, 68, 84, 85, 94]

# reverse() : 리스트의 값을 역순으로 정렬
var.reverse()
print(var) # [94, 85, 84, 68, 60, 45, 42, 38, 30, 19]

# clear() : 리스트의 모든 값을 제거
var.clear()
print(var) # []

# 리스트 컴프리헨션의 특징과 예
var = []
# var = list()
for data in range(1, 11):
    if data % 2 == 0:
        var.append(data)
print(var) # [2, 4, 6, 8, 10]

var = list(filter(lambda x: x % 2 == 0, range(11)))
print(var) # [0, 2, 4, 6, 8, 10]

var = [data for data in range(1, 11) if data % 2 == 0]
print(var) # [2, 4, 6, 8, 10]

var = [(x, y) for x in range(1, 11) for y in range(1, 11) if x + y == 10]
print(var) # [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]

var = [ x for x in range(1, 11) if x % 2 == 0 if 5 < x]
print(var) # [6, 8, 10]

# 제너레이터의 특징과 예
var = (data + 10 for data in range(1,11) if data % 2 ==0)
print(var) # <generator object <genexpr> at 0x0000021D7A2F5C80>

try:
    print(next(var)) # 12
    print(next(var)) # 14
    print(next(var)) # 16
    print(next(var)) # 18
    print(next(var)) # 20

    print(next(var)) # StopIteration 예외 발생
except StopIteration:
    print('StopIteration') # StopIteration
    
# 리스트의 활용 - 스택 first in last out
# 스택은 나중에 들어온 데이터가 먼저 나가는 구조이다.
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print(stack) # [1, 2, 3, 4, 5]

var = stack.pop()
print(var) # 5
print(stack) # [1, 2, 3, 4]

var = stack.pop()
print(var) # 4
print(stack) # [1, 2, 3]

# 참고 - 큐 first in first out
# 큐는 스택과 반대로 먼저 들어온 데이터가 먼저 나가는 구조이다.
from collections import deque
queue = deque(["chris", "tommy", "harry"])
queue.append("hans")
print(queue) # deque(['chris', 'tommy', 'harry', 'hans'])
     
var = queue.popleft()               
print(var) # chris
print(queue) # deque(['tommy', 'harry', 'hans'])

var = queue.popleft()         
print(var) # tommy
print(queue) # deque(['harry', 'hans'])
