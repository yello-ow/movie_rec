<div align="center">
  <h1> 🎬 콘텐츠 기반 필터링을 이용한 영화 추천 시스템  </h1>
  <br>
  <img  src="https://user-images.githubusercontent.com/86868063/169565058-96adf9fa-cdb9-49ab-a707-fedafe87bf24.png">
  <br><br>
  
  ### ⚒ 기술 스택
  ![Python](https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=FFFFFF) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-sqare&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=flat-square&logo=scikit+learn&logoColor=FFFFFF) ![flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white) ![heroku](https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=Heroku&logoColor=white)
  <br><br>
  </div>
  
  ## 프로젝트 개요 
  - 📅 프로젝트 기간 : 2021.12.10 - 2021.12.22   
  - 프로젝트 목표 : 장르 기반의 영화 추천시스템을 제작   
  <br>
  
  ## 추천 시스템 
  - 정보 필터링 기술의 일종으로 특정 고객이 관심을 가질만한 정보를 추천하는 것 
  - **콘텐츠 기반 필터링 : 상품의 특성만을 비교하여 가장 비슷한 상품을 추천하는 방법**
  - 협업 필터링 : 고객들의 다양한 행동 데이터에 기반해 아직 접하지 않은 상품에 대한 행동을 예측해 추천하는 방법 
  <br>
  
  ## 데이터 파이프라인 
  <img  src="https://user-images.githubusercontent.com/86868063/169566263-d3979803-f61f-4ce1-8043-425a1c7d1a4c.png">
  <br>
  
  ## 프로젝트 과정 
  - 데이터 : kaggle의 the movie database의 영화 데이터 [🔗링크](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
  - 데이터 전처리 
    - 총 20개의 열에서 추천 시스템 구현에 필요한 7개의 열만 남김
    - 장르 열에서 장르 글자만 추출
    - 장르 데이터를 countvectorizer를 사용해 벡터화 
    - 벡터화된 장르 데이터로 장르들의 코사인 유사도 계산 
  - Flask, Heroku를 이용해 Web application 배포  
  <br>
  
  ## 프로젝트 결과 
  - APP : [🔗Web APP](https://recomovie.herokuapp.com/)
  <img src="https://user-images.githubusercontent.com/86868063/152792862-f5e3ae7b-4b94-4230-b39e-ab5a4d1dd8f6.png">
  <br>
  
  ## 프로젝트 회고
  - 데이터와 코딩을 배우면서부터 꼭 구현해보고 싶은게 추천 시스템이어서 도전했지만 아직 다른 추천시스템을 구현하기에는 부족해서 가장 간단한 콘텐츠 기반 필터링 추천 시스템을 구현해 아쉬움이 남는다. 
  - 게다가 web application에서 장르가 비슷한 영화를 추천받으려면 데이터 목록에 있는 영화만 입력할 수 있으며 영화제목은 전부 영어만 가능하다. 
  - 영화 목록을 확인하는 방법을 좀 더 보기좋고 편리하게 만들고 싶었는데 그부분도 아쉽다. 이번 프로젝트에서는 추천시스템을 구현해봤다 하는 정도만 만족하고 나머지 부분은 다 너무 아쉬움이 남는 프로젝트인 것 같다. 

