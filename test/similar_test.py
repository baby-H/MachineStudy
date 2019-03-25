# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )

from gensim.models import Word2Vec


def get_result(positive=None, negative=None, topn=10, restrict_vocab=None, indexer=None):
    model = Word2Vec.load('C:/Users/ymsx30018/PycharmProjects/wikiextractor/data/model/word2vec_gensim')
    result = model.most_similar(positive, negative, topn, restrict_vocab, indexer)
    return result


if __name__ == '__main__':
    temp = get_result(['发烧', '头晕', '病名', '外感', '发热', '头痛'])
    print(temp)
