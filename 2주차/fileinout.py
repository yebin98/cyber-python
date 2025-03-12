# 새로운 퍄일에 데이터 쓰기
file = open("test.txt", "w")
for data in range(1, 11):
    file.write(f'{data} line');
file.close()

# 기록한 데이터 읽기
file = open("test.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close

# 이미 존재하는 파일에 데이터 추가하기
file = open("test.txt", "a")
for data in range(1, 11):
    file.write(f'{data} line\n');
file.close()

# 기록한 데이터 읽기 (전체 라인을 한번에 읽기)
file = open("test.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()

# 기록한 데이터 읽기 (read함수를 이용하여 전체를 한번에 읽음)
file = open("test.txt", "r")
data = file.read()
print(data)
file.close()

# with ~ as 구문을 이용하여 간결한 코드 작성하기
with open("test.txt", "r") as file:
    data = file.read()
    print(data)

