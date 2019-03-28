# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )


class Wake:
    def __init__(self):
        self.is_wake = 0

    def get_wake(self):
        return self.is_wake

    def set_wake(self, wake_t):
        self.is_wake = wake_t


if __name__ == '__main__':
    w = Wake(5)
    print(w.get_wake())
