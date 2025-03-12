variable = "%d books" % 3
print(variable)

variable = "%s books" % "3"
print(variable)

variable = "%s books" % 3
print(variable)

variable = "I have {0} {1}".format(3, "books")
print(variable)

number = 3
variable = f"I have {number+2} books"
print(variable)

variable = "I have %d apples and %d books" % (number, number+2)
print(variable)

variable = "The error rates : %d%%" % 55
print(variable)

# 오른쪽 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력
variable = "%10s" % "Hello"
print(variable)

# 왼쪽 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력
variable = "%-10s" % "Hello"
print(variable)

# 왼쪽 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력 (format 메서드 사용)
variable = "{0:<10}".format("Hello")
print(variable)

# 오른쪽 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력 (format 메서드 사용)
variable = "{0:>10}".format("Hello")
print(variable)

# 가운데 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력 (format 메서드 사용)
variable = "{0:^10}".format("Hello")
print(variable)

# 가운데 정렬하여 10칸의 공간을 확보하고 문자열 "Hello"를 출력, 빈 공간은 '-'로 채움 (format 메서드 사용)
variable = "{0:-^10}".format("Hello")
print(variable)

# 기본 소수점 형식으로 실수 3.141592를 출력
variable = "%f" % 3.141592
print(variable)

# 소수점 이하 4자리까지 실수 3.141592를 출력
variable = "%.4f" % 3.141592
print(variable)

# 소수점 이하 4자리까지 실수 3.141592를 출력 (format 메서드 사용)
variable = "{0:.4f}".format(3.141592)
print(variable)

# 소수점 이하 4자리까지 실수 3.141592를 출력하고, 전체 10칸의 공간을 확보
variable = "%10.4f" % 3.141592
print(variable)
