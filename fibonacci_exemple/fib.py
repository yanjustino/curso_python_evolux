#!/usr/bin/python
#-*- coding: utf8 -*-
 
import sys
 
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function
 
@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
 
 
if __name__ == '__main__':
    print fib(int(sys.argv[1]))