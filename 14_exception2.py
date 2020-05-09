def add(x, y):
    try:
        output = x + y
    except TypeError as e:
        print(e)
        try:
            output = int(x) + int(y)
        except ValueError as e:
            return None
    except:
        print(123)
    else:
        print('Answer is', output)
    finally:
        print('無論如何都會執行')

    return output

print(add(3, '5'))
print(add(3, 'x'))
print(add(3, 5))