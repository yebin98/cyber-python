# 추가 : Process의 활용
# https://docs.python.org/ko/3/library/multiprocessing.html
# https://docs.python.org/ko/3/library/subprocess.html

from multiprocessing import Process, Queue
import subprocess
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid()) # 부모 프로세스 ID
    print('process id:', os.getpid()) # 현재 프로세스 ID

def fn1(name):
    info('function f')
    print('hello', name)
    
def fn2(q):
    q.put([42, None, 'hello']) # Queue에 데이터를 넣음
          
if __name__ == '__main__':
    
    print('----- Start (1) -----')
    info('main line')
    p = Process(target=fn1, args=('bob',)) # Process(target=함수이름, args=(인자들))
    p.start()
    p.join() # join()은 프로세스가 끝날 때까지 기다림
    print('----- Done (1) -----')

    print('----- Start (2) -----')
    q = Queue() # Queue 객체 생성
    p = Process(target=fn2, args=(q,)) # Queue를 인자로 받는 Process 생성
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join() 
    print('----- Done (2) -----')
    
    print('----- Start (3) -----')
    # https://blog.naver.com/PostView.nhn?blogId=sagala_soske&logNo=221280201722
    result = subprocess.call(['python', './06week/dict.py']) # subprocess.call()은 외부 프로그램을 실행하고, 종료될 때까지 기다림
    print(result)
    print('----- Done (3) -----')  