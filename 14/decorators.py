import functools
import logging
import time
from functools import wraps
from time import sleep
from timeit import timeit


def uppercase(func):
    '''Decorator that uppercases func, no args'''

    @wraps(func)  # preserves function meta data
    def wrapper():
        return func().upper()

    return wrapper


def sleep_decorator(func):
    '''Decorator that sleeps n seconds, passes through args
    Also called a 'rate-limiting' decorator'''
    interval = 0.1

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Sleep {interval} seconds')
        sleep(interval)
        return func(*args, **kwargs)

    return wrapper


def log(func):
    '''Decorator that logs the function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger()
        try:
            logger.info(f'{func.__name__} being called')
            a = func(*args, **kwargs)
            logger.info(f'{func.__name__} AFTER being called')
        except Exception as e:
            print(e)
        return a

    return wrapper

def cached(function_to_decorate):
    '''Decorator to cache results of function
    This is also called 'memoisation'
    There is an existing decorator that does something similar LRUcache
    '''
    _cache = {} # Where we keep the results
    @wraps(function_to_decorate)
    def decorated_function(*args):
        start_time = time.time()
        # print('_cache:', _cache)
        if args not in _cache:
            _cache[args] = function_to_decorate(*args) # Perform the computation and store it in cache
        # print('Compute time: %ss' % round(time.time() - start_time, 2))
        return _cache[args]
    return decorated_function

@uppercase
def hello_world():
    return 'hello world'


@sleep_decorator
def print_word(word):
    '''Print a word'''
    print(word)


@log
def hey2():
    return ('heya!!!')


def long_loop(arg):
    if arg == 1:
        return "-".join(map(str, range(100)))
    if arg == 2:
        return "-".join([str(i) for i in range(100)])
    if arg == 3:
        return "-".join(str(i) for i in range(100))

def timer(fn):
    '''Decorator that repeats a function 10000 times then prints time taken'''
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        for i in range(9999):
            fn(*args, **kwargs)
        return_value = fn(*args, **kwargs)
        end = time.time()
        print(f'function name: {fn.__name__}')
        print(f'---- {end-start:.6f} seconds ----')
        return return_value
    return wrapper



if __name__ == '__main__':
    print('1. Printing "hello world" to upper with decorator:')
    print(hello_world())

    print()
    print('2. Sleep n seconds before calling func:')

    words = 'today is a great pythonic day'.split()

    for w in words:
        print_word(w)

    print()
    print('3. decorate with adding a logger')
    print(hey2())

    print()
    print('4. using timeit in lieu of a decorator')
    print(timeit('long_loop(1)', number=10000,
                 setup="from __main__ import long_loop"))
    print(timeit('long_loop(2)', number=10000,
                 setup="from __main__ import long_loop"))
    print(timeit('long_loop(3)', number=10000,
                 setup="from __main__ import long_loop"))

    print()
    print('5. using a timer decorator')
    for i in range(1,4):
        timed_fn = timer(long_loop)
        timed_fn(i)

    print()
    print('6. using a cached timer decorator, which is also logged')
    for i in range(1, 4):
        timed_fn = log(timer(cached(long_loop)))
        timed_fn(i)