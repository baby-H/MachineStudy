# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
import os


# reload(sys)

# sys.setdefaultencoding('utf-8')
def get_html(url):
    return urllib.request.urlopen(url, timeout=20).read().decode('utf-8')


temp_str = ''
n = 0
f = open(r'test.txt', 'r', encoding='utf8')
fp = open(r'word_0_out.txt', 'w+', encoding='utf8')
for line in f:
    if len(temp_str) > 400000:
        fp.close()
        path = os.path.join('word_' + str(++n) + '_out.txt')
        fp = open(path, 'w+', encoding='utf8')
    fp.write(line)
    line = line[:-1]
    print(line)
    try:
        url0 = "https://baike.baidu.com/item/"
        url = url0 + urllib.parse.quote(str(line))
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        if str(soup.title) == '<title>百度百科——全球最大中文百科全书</title>':
            print('404')
            continue
        for text in soup.find_all('div', class_="para"):
            for div_tag in text.find_all('div', class_="description"):
                div_tag.decompose()
            if text.span:
                text.span.decompose()
            new_str = "".join(text.get_text().split())
            new_str = re.sub(r'\[[\d]*\]', '', new_str)
            new_str = re.sub(r'\[[\d]*-[\d]\]', '', new_str)
            temp_str = temp_str + new_str
            fp.write(new_str)
        print()
        fp.write(u"\n")
    except:
        print('error')
        continue
fp.close()
f.close()
