# 경고 지우기 
import warnings
warnings.filterwarnings("ignore")

# 라이브러리 import
import pandas as pd 
import numpy as np

## 문자열 -> 객체 변경 라이브러리
from ast import literal_eval 

## 벡터화 라이브러리
from sklearn.feature_extraction.text import CountVectorizer

## 코사인 유사도 라이브러리 
from sklearn.metrics.pairwise import cosine_similarity

# 데이터 불러오기 
import os.path
folder = os.path.abspath('tmdb_5000_movies.csv')
movie = pd.read_csv(folder)

# 필요한 column만 남기기 
columns = ['id', 'title', 'genres', 'vote_average', 'vote_count', 'popularity', 'keywords', 'overview']
df = movie[columns]

# overview 결측치 제거 
df['overview'].isnull().sum()
df['overview'] = df['overview'].fillna('')

# 장르, 키워드 str 추출 
## str -> list{dict} : 문자열을 객체로 변환
df['genres'] = df['genres'].apply(literal_eval)
df['keywords'] = df['keywords'].apply(literal_eval)

## dict에 있는 장르 name만 추출
df['genres'] = df['genres'].apply(lambda x : [dic['name'] for dic in x])
df['keywords'] = df['keywords'].apply(lambda x : [dic['name'] for dic in x])

# 가중 평점 계산 
m = df['vote_count'].quantile(0.8)
c = df['vote_average'].mean()

## 가중 평점 계산 함수 
def weighted_rating(x, m=m, c=c) : 
    V = x['vote_count']
    R = x['vote_average']
    return ((V/(V+m))*R) + ((m/(m+V))*c) # 계산식은 IMDb참고 

df['weighted_vote'] = df.apply(weighted_rating, axis=1)

# 장르 유사도 구하기  - 코사인 유사도 
# 쉼표 제거 후 장르 합치기 
df['genres'] = df['genres'].apply(lambda x : (' ').join(x))

# 장르 벡터화 
count_v = CountVectorizer(ngram_range=(1,3))
genre_v = count_v.fit_transform(df['genres'])

# 코사인 유사도 구하기
genre_csine = cosine_similarity(genre_v, genre_v)

# 장르 기반 추천 함수 
def genre_sim_movie(title_name) : 
    
    # 영화 제목 일치 행 찾기 
    title_movie = df[df['title'] == title_name]

    # 영화의 인덱스 찾기 
    title_index = title_movie.index.values

    # 입력한 영화 제목과 영화 목록의 코사인 유사도 
    df['similarity'] = genre_csine[title_index, :].reshape(-1,1)

    # 유사도 기반 내림차순 정렬 
    temp = df.sort_values(by='similarity', ascending=False)

    # 입력한 영화 제외 
    temp = temp[temp.index.values != title_index]
    
    # 상위 10개 영화의 인덱스 
    final_index = temp.index.values[:10]

    return df[['title', 'genres', 'weighted_vote', 'similarity']].iloc[final_index]

##------------------------------------------------------------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index() : 
    return render_template('home.html'), 200

@app.route('/recommend', methods=['GET', 'POST'])
def home() : 
    movie_name = request.form['name'] 

    genre_rec = genre_sim_movie(movie_name)['title'].tolist()

    return render_template('after.html', data = genre_rec)

@app.route('/movie_list', methods=['GET', 'POST'])
def list() : 
    movie_list = df['title'].tolist()
    movie_list.sort()

    return render_template('list.html', data = movie_list)