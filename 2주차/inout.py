# 사용자가 입력한 값은 문자열입니다.
variable = input()
print("Input String %s, Ineger %d" % (variable, int(variable)))

#사용자에게 메시지를 표시하면서 입력받을 수 있습니다.
variable = input("Enter a number: ") # 5
variable = int(variable) ** 2
print(f'Result : {variable}') # Result : 25

# print를 이용한 다양한 출력 방법
variable = [1, 2, 3, 4, 5]
print(f'List : {variable}') # List : [1, 2, 3, 4, 5]

variable = (1, 2, 3, 4, 5)
print(f'Tuple : {variable}') # Tuple : (1, 2, 3, 4, 5)

print("Hello" "World") # 문자열을 붙여서 출력합니다. # HelloWorld
print("Hello", "World") # 문자열을 ,로 구분하여 출력합니다. # Hello World

for variable in range(1, 10):
    print(variable, end=" ") # end는 줄바꿈을 하지 않고, 공백으로 구분하여 출력합니다. # end는 기본값이 줄바꿈입니다. # 1 2 3 4 5 6 7 8 9