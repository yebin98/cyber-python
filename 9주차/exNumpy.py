# pip install numpy
import numpy as np

#######################################33
# 기본 사용법
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array = np.array(data)

print(array)
print(array.dtype)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.nbytes)

print(array[0][0]) # 1행 1열

subarray = array[ :, :2]
print(subarray)
print(subarray.shape)

array = np.arange(0, 10, 2)
print(array) # [0 2 4 6 8]

array = np.zeros((3,3)) # 3행 3열의 0으로 채워진 배열
print(array) 

array = np.ones((3,3)) # 3행 3열의 1로 채워진 배열
print(array)

array = np.eye(3) # 3행 3열의 단위행렬
print(array) 

array = np.random.randint(0, 100, (3,3)) # 0~100 사이의 랜덤한 정수로 채워진 3행 3열의 배열
print(array) 

array = np.full((8,8), 255) # 8행 8열의 255로 채워진 배열
print(array) 

array = array.flatten() # 1차원 배열로 변환
print(array)

array = array.reshape((8,8)) # 8행 8열로 변환
print(array)

array[2:6, 2:6] = 0
print(array) # 2행 2열부터 6행 6열까지 0으로 채워짐

array = np.where(array == 0, 1, array) # 0인 값을 1로 변경
print(array) 

arrayA = np.array([1,2,3])
arrayB = np.array([4,5,6])
array = np.concatenate((arrayA, arrayB))
print(array) # [1 2 3 4 5 6]

array = arrayA + arrayB
print(array) # [5 7 9]

array = arrayA * arrayB
print(array) # [4 10 18]

array = arrayA / arrayB
print(array)  # [0.25 0.4  0.5 ]

result = np.dot(arrayA, arrayB) # 행렬 곱
print(result) # 32




