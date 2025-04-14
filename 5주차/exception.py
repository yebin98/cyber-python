# 존재하지 않는 파일을 읽기모드로 여는 경우 : FileNotFoundError 후 종료
#myFile = open('NotExist.txt', 'r')

# 잘못된 접근 : IndexError 후 종료
#myList = [1, 2, 3]
#print(myList[3])

# 예외처리 : try ~ except
try:
    myFile = open('NotExist.txt', 'r')
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.') 
    print(e) # [Errno 2] No such file or directory: 'NotExist.txt'
    
try:
    myList = [1, 2, 3]
    print(myList[3])
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.')
    print(e) # list index out of range
    
try:
    print('Hello world!') #Hello world!
    raise Exception('My Exception')
except Exception as e:
    print(e) #My Exception

# 예외처리 : try ~ except: 내가 원하는 예외만 처리 ~ finally: 항상 처리
# 여러개의 예외를 한번에 처리하려면 튜플로 묶어서 처리할 수 있음
# except (FileNotFoundError, IndexError, ZeroDivisionError) as e:
try:
    myFile_1 = open('example.txt', 'w')
    myFile_1.write('Hello world!')
    myList = [1, 2, 3]
    result = myList[3] / 0
    print(result) 
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.') # 리스트의 인덱스가 존재하지 않습니다.
    print(e) # list index out of range
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
    print(e)
finally:
    myFile_1.close()
    print('항상 실행됩니다.') # 항상 실행됩니다.
    
# 예외처리 : try ~ except ~ else: 예외가 발생하지 않은 경우
try:
    myFile_2 = open('example.txt', 'r')
    data = myFile_2.readline()
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
else:
    print(data) # Hello world!
    myFile_2.close()
    
# 예외처리 : try ~ except ~ else ~ finally
try:
    myList = [1, 2, 3]
    result = myList[3] / 0
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.') # 리스트의 인덱스가 존재하지 않습니다.
    print(e) # list index out of range
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
    print(e)
else:
    print(result)
finally:
    print('항상 실행됩니다.') # 항상 실행됩니다.
    
# 예외 처리 vs. 조건문
data = input('숫자를 입력하세요 : ') # 5
try:
    result = 10 * int(data)
    print(result) # 50
except ValueError as e:
    print('숫자를 입력하세요.')
    print(e)
    
data = input('숫자를 입력하세요 : ') # 5
if data.isdigit():
    result = 10 * int(data)
    print(result) # 50
else:
    print('숫자를 입력하세요.')
    
# assert 조건식, '에러메시지': 조건에 맞지 않으면 AssertionError 발생
# assert는 주로 디버깅할 때 사용
data = input('7을 입력하세요 : ') # 7을 입력하세요 : 8
try:
    assert data == '7', '7을 입력하세요.'
except AssertionError as e:
    print(e) # 7을 입력하세요.