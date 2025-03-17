#####################################
# if 문의 활용 예

# 기본
cond = True
if cond:
    print("Execute")

# if ~ else
var = 10
if 0 < var:
    print("Big")
else:
    print("Small")

# if ~ elif ~ else
var = input("Enter a number: ")
var = int(var)

if 10 < var:
    print("Bigger than 10")
elif 5 < var:
    print("Bigger than 5")
elif 0 < var:
    print("Bigger than 0")
else:
    print("Too Small")
    
# 비교 / 논리 연산자
x, y = 10, 20
if 0 < x and y < 30:
    print("Good")
else:
    print("Bad")
    
var = input("Enter a number: ")
var = int(var)

if x != var and y != var:
    print("Bad")
else:
    print("Good")


# in, not 연산자
var = [1, 2, 3] 
print (1 in var) 

var = ["chris", "tommy", "harray"]
print("chris" in var)

var = "Hello Python"
print("J" not in var)

# 조건부 표현식
var = input("Enter a number: ")
var = int(var)

var = "Big" if 10 < var else "Small"
print(var)
    