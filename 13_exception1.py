def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError as e:
        print(e)
        print(e.args)
        print(e.errno)
        name = name.replace('/', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError as e:
        print(e)
        name = 'test123'
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except:
        print('Unknown Exception!')

createFile('test/test1.txt')
createFile('test?test')