from konlpy.tag import Okt
from collections import Counter
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import matplotlib 
from IPython.display import set_matplotlib_formats
import numpy as np
from PIL import Image

# 토큰 str 불러오기
fr = open('../data/bluehouse_token.txt','r',encoding='CP949')
lists = fr.readlines()
fr.close()

# 토큰별 태그를 함께 tuple list로 저장
okt = Okt()
morphs = []

for sentence in lists:
    morphs.append(okt.pos(sentence))
    
# 이상한 토큰은 제거하고 리스트로 저장
noun_adj_list = []

for tuples in morphs:
    for word, tag in tuples:
        if tag in ['Noun'] and ("대한" not in word) and ("적용" not in word) and ("및" not in word) and ("요청" not in word) \
        and ("위" not in word) and ("관련" not in word) and ("수" not in word) and ("것" not in word) and ("저" not in word) \
        and ("입" not in word) and ("재" not in word) and ("등" not in word) and ("무" not in word) and ("제" not in word) \
        and ("시오" not in word) and ("이" not in word) and ("중" not in word) and ("더" not in word) and ("피" not in word) \
        and ("비" not in word) and ("자" not in word) and ("고" not in word) and ("대해" not in word) and ("를" not in word) \
        and ("왜" not in word) and ("요구" not in word) and ("의" not in word) and ("위" not in word) and ("을" not in word) \
        and ("청" not in word) and ("한" not in word) and ("자" not in word) and ("단" not in word) and ("제" not in word) \
        and ("제" not in word) and ("층" not in word) and ("개선" not in word):
            noun_adj_list.append(word)

# check
noun_adj_list[:10]

# 토큰별 개수 dict 저장
count = Counter(noun_adj_list)
word_count = dict(count.most_common())

# check
word_count

# 워드클라우드 생성
wordcloud = WordCloud(background_color="white", font_path='../data/NanumGothic.ttf', \
                        colormap='gist_ncar', width=800, height=800)

wordcloud = wordcloud.generate_from_frequencies(word_count)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()