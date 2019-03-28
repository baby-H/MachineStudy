# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import os


def _test_for():
    # 获取当前路径
    base_dir = os.path.dirname(__file__)
    for i in range(10):
        path = os.path.join(base_dir, str(i) + '.txt')
        f = open(path, 'w+', encoding='utf8')
        f.write(str(i))
        f.close()


if __name__ == '__main__':
    list_t = []
    with open('Word_in.txt', 'r+', encoding='utf8') as f:
        for i in f.readlines():
            list_t.append(i[:-1])
    print(list_t)

