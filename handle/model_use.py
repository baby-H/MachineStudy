# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )

from gensim.models import Word2Vec


def get_result(positive=None, negative=None, topn=50, restrict_vocab=None, indexer=None):
    model = Word2Vec.load('C:/Users/ymsx30018/PycharmProjects/wikiextractor/data/model/word2vec_gensim')
    result = model.most_similar(positive, negative, topn, restrict_vocab, indexer)
    return result


if __name__ == '__main__':
    temp = get_result(['病名', '发烧', '头晕', '发热', '头痛'])
    print(temp)
    t = get_result(['病名', '酸痛',  '胸痛', '气短', '咳血', '腿'])
    print(t)
    t = get_result(['尿血', '病名', '无'])
    print(t)
