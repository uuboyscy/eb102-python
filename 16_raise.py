def devide(x, y):
    print('x:', x, 'y:', y)

    if y == 0:
        raise ZeroDivisionError('不可除以0')
    elif not (type(x) in [type(1), type(1.1)] and type(y) in [type(1), type(1.1)]):
        raise TypeError('x y 必須為數字')

    result = x / y

    return result

try:
    print(devide(2, 0))
except ZeroDivisionError as e:
    print(e)