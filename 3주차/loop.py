#####################################
# while 문의 활용 예

cond = 0
while cond < 10:
    cond = cond + 1
    if cond % 3 == 0:
        continue
    if cond % 5 == 0:
        break
    print(cond) # 1 2 4
    
while True:
    var = input("Enter a number: ")
    var = int(var)
    if var == 0:
        print("Good Bye")
        break;

#####################################
# for 문의 활용 예

var = [1, 2, 3]
for one in var:
    print(one)  # 1 2 3
    
var = [(1,1), (2,2), (3,3)]
for (first, second) in var:
    print(first, second) # 1 1 2 2 3 3

sum = 0
var = range(1, 11)
for one in var:
    if (one % 2 == 0):
        continue
    sum = sum + one
print(sum)  # 25