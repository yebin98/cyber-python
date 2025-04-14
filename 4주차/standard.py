# 표준 라이브러리는 import하여 사용한다.
# 대표적인 것만 살펴보며, 함께 메모해 드릴 인터넷 자료도 함께 참고하시면 좋겠습니다.

import datetime
date = datetime.date(2023, 3, 1)
print(date) # 2023-03-01
print(date.isoweekday()) # 3

import time 
current = time.time()
print(current)# 1677628800.0
current = time.localtime(current)
print(current)# time.struct_time(tm_year=2025, tm_mon=4, tm_mday=14, tm_hour=23, tm_min=35, tm_sec=37, tm_wday=0, tm_yday=104, tm_isdst=0)
current = time.strftime('%c', current)
print(current) # Mon Apr 14 23:35:37 2025

import random
for count in range(5):
    print(f'count : {count}')
    print(random.randint(1, 10))
    time.sleep(1)

# 객체를 직접 저장하고 읽어 들이기    
import pickle
data = {'chris' : 1, 'tommy' : 2, 'harry' : 3}
file = open('picket.txt', 'wb')
pickle.dump(data, file)
file.close()

file = open('picket.txt', 'rb')
data = pickle.load(file)
file.close()
print(data) # {'chris': 1, 'tommy': 2, 'harry': 3}

import os
print(os.environ['PATH']) # 환경변수 PATH를 출력한다.
os.system('dir')
file = os.popen('dir') 
print(file.read()) # dir 명령어를 실행하여 결과를 읽어온다.
file.close()

