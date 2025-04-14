####################
# 변수의 스코프(범위)

val = 0
def processing(data):
    global val
    val = data
    data = data * 10
    return data*data

data = 10
result = processing(data)
print(val) # 10
print(data) # 10
print(result)   # 10000

####################
# Call by Reference
def processing(data):
    data[0] = 100

val = [1, 2, 3]
processing(val)
print(val)  # [100, 2, 3]
