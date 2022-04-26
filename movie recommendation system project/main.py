import pickle
import pandas as pd
import streamlit as st 
import requests
# Streamlit

st.title("Welcome Movie Recommend system")

movies=pickle.load(open(r"E:\10.python\project\movie_recemadation\tmdb_5000_credits.csv\movie_file.pkl","rb"))
movies=pd.DataFrame(movies)
print(movies)
sm=pickle.load(open(r"E:\10.python\project\movie_recemadation\tmdb_5000_credits.csv\similarity_list.pkl","rb"))


def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend_movie(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    list_of_recomd=sorted(list(enumerate(sm[movie_index])),reverse=True,key=lambda x:x[1])
    
    Recommend_movie_list=[]
    Recommend_movie_poster=[]
    for i in list_of_recomd[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        print(movie_id)
        Recommend_movie_poster.append(poster(movie_id))
        Recommend_movie_list.append(movies.iloc[i[0]].title)
    return Recommend_movie_list,Recommend_movie_poster

# Recommend_movie("El Mariachi")
st.header("Please select movie from below dropdown?")
movies_list=movies["title"].values
seleced_movie=st.selectbox("Select Movie Name",movies_list)

if st.button("Recommend"):
    recomd_movie_name,recomd_poster=recommend_movie(seleced_movie)
    col1,col2,col3,col4,col5=st.columns([10,10,10,10,10])
    with col1:
        st.text(recomd_movie_name[0])
        st.image(recomd_poster[0])
    with col2:
        st.text(recomd_movie_name[1])
        st.image(recomd_poster[1])
    with col3:
        st.text(recomd_movie_name[2])
        st.image(recomd_poster[2])
    with col4:
        st.text(recomd_movie_name[3])
        st.image(recomd_poster[3])
    with col5:
        st.text(recomd_movie_name[4])   
        st.image(recomd_poster[4])