def strict(func):
    def wrapper(a, b):
        type1 = func.__annotations__['a']
        type2 = func.__annotations__['b']
        if type1 != type(a) or type2 != type(b):
            return TypeError('ошибка с типом данных, пробуй еще')
        return func(a, b)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
print(sum_two(1, True))