# -*- coding:utf-8 -*-
# author xin.luo

# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，
# 以及出错的原因。在操作系统提供的调用中，返回错误码非常常见
# 程序报错
def must_error():
    a = 10
    print(a / 0)


# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）
# python内置了一套try...except...finally...的错误处理机制
# try exception捕获错误
def try_catch():
    try:
        must_error()
    except Exception as e:
        # 打印异常的信息
        print(repr(e))
    finally:
        # 捕获结束后的剩余操作
        print("remain thing need to do")


if __name__ == '__main__':
    try_catch()