import functools


def index(a1, a2):
    return a1 + a2

# 偏函数，帮助开发者自动传递第一个参数
new_func = functools.partial(index, 666)

ret = new_func(1)
print(ret)
