# 2021년도에 취업준비 하면서 진행한 Toy Project의 Source code
- 예전 노트북에서 이 코드를 찾아서 뒤늦게 깃허브에 올려둠
- **현재에는 청원게시판이 사라져서 다시 코드를 돌려보기 어려움**

## 주제:
청와대 청원게시판에 어떤 글이 가장 많을까??
<br>
## 방법론:
#### 1. 크롤링 (scrapping.py)
- 청와대 청원 게시판 내 게시글들을 크롤링
#### 2. 토큰화 (tokenize.py)
- 게시글 제목들을 토크나이징
#### 3. 시각화 (worcloud.py)
- 토큰화된 단어를 기준으로 워드클라우드 시각화
<br>
## 수집 변수:
|이름|설명|
|---|--|
|번호|게시글의 고유 번호|
|제목|게시글의 제목|
|분류|게시글의 카테고리|
|참여인원|청원에 동의한 사람의 수|
|만료일|청원 만료일|
