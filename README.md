<div align="center">
  <h1> 🎬 콘텐츠 기반 필터링을 이용한 영화 추천 시스템  </h1>
  <br>
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
  
  ## 프로젝트 과정 
  - 데이터 : kaggle의 the movie database의 영화 데이터 [🔗링크](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
  - 데이터 전처리 
    - 총 20개의 열에서 추천 시스템 구현에 필요한 7개의 열만 남김
    - 장르 열에서 장르 글자만 추출
    - 장르 데이터를 countvectorizer를 사용해 벡터화 
    - 벡터화된 장르 데이터로 장르들의 코사인 유사도 계산 
  <br>
  
  ## 프로젝트 결과 
  - APP : [🔗Web APP](https://recomovie.herokuapp.com/)
  <img src="https://user-images.githubusercontent.com/86868063/152792862-f5e3ae7b-4b94-4230-b39e-ab5a4d1dd8f6.png">

  

<!--
- 추천시스템 : https://dsbook.tistory.com/334
- 레퍼런스 1 : https://romg2.github.io/mlguide/01_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%99%84%EB%B2%BD%EA%B0%80%EC%9D%B4%EB%93%9C-09.-%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%BD%98%ED%85%90%EC%B8%A0-%EA%B8%B0%EB%B0%98/
- 레퍼런스 2 : https://dkswnkk.tistory.com/119
- 레퍼런스 3 : https://wikidocs.net/24603
-->
