import streamlit as st

import  pickle
import pandas as pd

def recommand(movie1):
    movie_index = movies[movies['title'] == movie1].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    list1 = []
    for i in movies_list:
        movie_id=i[0]
        list1.append(movies.iloc[i[0]].title)
    return list1

movie_list= pickle.load(open('movies_dict.pkl',"rb"))
movies=pd.DataFrame(movie_list)
similarity=pickle.load(open('similarity.pkl',"rb"))
st.title("Movie Recommander System")
selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values)

if st.button('Recommand'):
    recommandation = recommand(selected_movie_name)
    for i in recommandation:
        st.write(i)

