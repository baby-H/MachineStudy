# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
from bs4 import BeautifulSoup
from urllib import request, parse
import time


def get_ids_by_word(word_t=None, set_t=None):
    data = {'title': word_t,
            'dataClass': 'https://search.baikemy.com/disease'}

    url_t = 'https://www.baikemy.com/search/searchlist'
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                   "Content-Type": "application/x-www-form-urlencoded"}
    data = parse.urlencode(data)
    url_t = url_t + '?' + str(data)
    req = request.Request(url=url_t, headers=header_dict, method='POST')
    res = request.urlopen(req)
    soup = BeautifulSoup(res, 'html.parser')
    is_over = 0
    for div in soup.find_all('div', class_="ssjgye_jbkx_text"):
        for a in div.find_all('a', target='_blank'):
            if is_over > 7:
                return set_t
            is_over += 1
            set_t.add(str(a['href']).replace("/disease/view/", ''))
    return set_t


def get_ids_by_path(path=None):
    set_t = set()
    temp_start, index = time.time(), 0
    f = open(path, 'r', encoding='utf8')
    for line in f:
        index += 1
        print('index =', index)
        get_ids_by_word(word_t=line[:-1], set_t=set_t)
    print('获得ID用时 =', time.time() - temp_start)
    f.close()
    return set_t


def get_content(in_path=None, out_path=None):
    url_t = 'https://www.baikemy.com/disease/detail/'
    set_final = get_ids_by_path(in_path)
    f = open(out_path, 'w+', encoding='utf8')
    for t in set_final:
        res = request.urlopen(url_t + t + '/1')
        soup = BeautifulSoup(res, 'html.parser')
        for main_n1 in soup.find_all('div', class_='main_n1'):
            for lemma in main_n1.find_all('div', class_='lemma-main'):
                for para in lemma.find_all('div', class_='para'):
                    for p in para.find_all('p'):
                        f.write(p.get_text())
        f.write('\n')
        print('id = ', t)
    f.close()


if __name__ == '__main__':
    get_content(in_path=r'Word_in.txt', out_path=r'word_1_out.txt')

