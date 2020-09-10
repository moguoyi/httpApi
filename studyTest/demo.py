#coding:utf-8
import time

def deco(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        f(*args,**kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f(a,b,c):
    print("hello")
    time.sleep(1)
    print("world")
    print("总值：",a+b+c)
@deco
def mo(a,d,f,g):
    print(a*d-f+g)

if __name__ == '__main__':
    f(1,2,9)
    mo(1,2,3,4)