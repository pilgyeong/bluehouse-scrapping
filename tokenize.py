import pandas as pd
from konlpy.tag import Okt, Kkma, Komoran, Hannanum, Twitter
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tag import untag
import xlsxwriter

my_df = pd.read_csv('../data/bluehouse.csv')

# 제목 col 토큰화
title_list = my_df.제목
my_str = ''
nouns_list = []
nlpy = Okt()
for title in title_list:
    nouns = nlpy.nouns(title)
    # 행별 토큰 저장 (이중 list 객체)
    nouns_list.append(nouns)
    for j in nouns:
        # 전체 토큰 저장 (str 객체)
        my_str = my_str + ' ' + j
        

# 각 row 토큰 엑셀로 저장
workbook = xlsxwriter.Workbook('../data/bluehouse_token.xlsx')
worksheet = workbook.add_worksheet()

for i, x in enumerate(nouns_list):
    worksheet.write_row('A'+str(i+1), x)

workbook.close()

# 모든 토큰을 Text로 저장
fw = open('../data/bluehouse_token.txt', 'w')
fw.write(my_str)
fw.close()