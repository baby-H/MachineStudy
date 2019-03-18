import os


def test_for():
    for i in range(10):
        path = os.path.join(base_dir, str(i) + '.txt')
        f = open(path, 'w+', encoding='utf')
        f.write(str(i))
        f.close()
        fp = open(path, 'w+', encoding='utf8')


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, 'test.txt')
f = open(path, 'w+', encoding='utf')
if __name__ == '__main__':
    for i in range(10):
        f.write('hello')
    f.close()
    # 获取当前文件目录
    print(base_dir)


