from gensim.models import Word2Vec

temp = Word2Vec.load('word2vec_gensim')
temp = temp.most_similar(['伤风感冒', '风寒', '外感'])
print(temp)