import math 
import time

def calculate_operations(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Calculation time: "+str(finish-start)+"\n")
    return inner

@calculate_operations
def power(a,b):
    print(f"Result: {math.pow(a,b)}")
    
@calculate_operations
def factorial(num):
    print(f"Result: {math.factorial(num)}")

power(2,3)
factorial(5)
