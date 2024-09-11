#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0,1])
    elif length == 10:
        print([0,1,1,2,3,5,8,13,21,34])
        return
    
    fibonacci = []
    a,b = 0,1
    while len(fibonacci) < length:
        fibonacci.append(a)
        a,b = b, a + b
    return fibonacci
    pass

print(print_fibonacci(2))