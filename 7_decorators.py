from functools import wraps
from datetime import datetime
from time import sleep
from helpers import print_green


def time_logger(f):
    # @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        print_green(f"Function '{f.__name__}' execution time is {(datetime.now() - start).seconds} sec.")
        return result

    return wrapper


@time_logger
def func_add(x: int, y: int):
    """Add two numbers"""
    return x + y


@time_logger
def complex_calc(x: int, y: int):
    """Add two numbers"""
    sleep(2)
    return x + y


print(func_add(2, 4))
# print(complex_calc(2, 4))
# print(time_logger(func_add)(2, 4))
# wrapper = time_logger(func_add)
# wrapper(2, 4)

# print(func_add.__name__)
# print(func_add.__doc__)

# def logger(n: int = 1):
#     def wrapper_1(f):
#         # @wraps(f)
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 print(f'Args: {args}')
#             result = f(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return wrapper_1
#
#
# @logger(n=3)
# def func_add(x, y):
#     return x + y
#
#
# @logger(n=3)
# def func_div(x, y):
#     return x / y
#
#
# # func_add = logger(3)(func_add)
#
#
# print(func_add(3, 7))
# print(func_div(3, 0))
# print(func_add.__name__)
