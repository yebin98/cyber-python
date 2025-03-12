# 사용자가 입력한 값은 문자열입니다.
variable = input()
print("Input String %s, Ineger %d" % (variable, int(variable)))

#사용자에게 메시지를 표시하면서 입력받을 수 있습니다.

variable = input("Enter a number: ")
variable = int(variable) ** 2
print(f'Result : {variable}')

# print를 이용한 다양한 출력 방법
variable = [1, 2, 3, 4, 5]
print(f'List : {variable}')

variable = (1, 2, 3, 4, 5)
print(f'Tuple : {variable}')

print("Hello" "World")
print("Hello", "World")

for variable in range(1, 10):
    print(variable, end=" ")