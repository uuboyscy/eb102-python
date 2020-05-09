import os

print('CUrrent work dir:', os.getcwd())
print('List dir', os.listdir('./'))

# os.mkdir('./test1')
# os.makedirs('./test2/test3')
# os.remove('./test.txt')
# os.rmdir('test1')
# os.removedirs('./test2/test3')
if not os.path.exists('test1'):
    os.mkdir('test1')