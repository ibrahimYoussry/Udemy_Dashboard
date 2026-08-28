#Import_Library 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Udemy",
                page_icon=None,
                layout="wide",
                initial_sidebar_state="expanded")

df = pd.read_csv('udemy_courses-raw.csv')
# df2 = st.dataframe(df)

#Sidbar
st.sidebar.header('Udemy Dashboard' , text_alignment="center")
st.sidebar.write('                                           ')
st.sidebar.image('udemy.png')
st.sidebar.text('Performing EDA on Udemy courses data to explore courses, subjects, levels, prices, and subscribers Creating KPIs & visualizations to identify key trends and insights the data')
st.sidebar.write('                               ')
st.sidebar.subheader('Filters')
cat_fil = st.sidebar.selectbox('cat' , [None,'subject','level'])
num_fil = st.sidebar.selectbox('num' , [None ,'price','num_subscribers','content_duration'])
st.sidebar.write('                                           ')
st.sidebar.write('                                           ')
st.sidebar.write('                                           ')
st.sidebar.markdown("Created by : Ibrahim Youssry")


#body
cl1 ,cl2 , cl3, cl4 = st.columns(4)
cl1.metric('MaxPrice ' , df['price'].max() ,)
cl2.metric('TotalSubscribes' , df['num_subscribers'].sum())
cl3.metric('TotalReview ' , df['num_reviews'].sum())
cl4.metric('TotaLLec' , df['num_lectures'].sum())
st.write('_______________________________________________________________________________________')
st.subheader('Price & Sub')
fig = px.scatter(data_frame= df, 
                x= 'price',
                y = 'num_subscribers' ,
                color= cat_fil,
                size= num_fil, hover_name='subject')
st.plotly_chart(fig , use_container_width=True)
st.markdown("**Summary Insight**:   *A large number of students enrolled in free courses*......  **⬆** ")
paid_free = df.groupby('is_paid').agg(
    courses=('course_id', 'count'),
    subscribers=('num_subscribers', 'sum')
).reset_index()

paid_free['type'] = paid_free['is_paid'].map({
    True: 'Paid',
    False: 'Free'
})

fig = px.pie(
    paid_free,
    names='type',
    values='courses',
    title='Paid vs Free Courses'
)

fig.update_traces(
    hovertemplate='<b>%{label}</b><br>' +
                'Courses: %{percent}<br>' +
                'Subscribers: %{customdata:.1f}%'
    ,
    customdata=paid_free['subscribers'] / paid_free['subscribers'].sum() * 100
)

st.plotly_chart(fig, use_container_width=True)
st.subheader('Lec & Duration')
fig = px.scatter(data_frame= df, 
                x= 'num_lectures',
                y = 'content_duration'
                )
st.plotly_chart(fig , use_container_width=True)
st.write('_______________________________________________________________________________________')
st.header('All chart' , text_alignment='center')

#c1,c2,c3 = st.columns((4,3,3))

#with c1:
st.text('subject by  price')
fig = px.bar(data_frame= df , x='subject', y='price' , color_discrete_sequence=['gray'])
st.plotly_chart(fig , use_container_width=True)
#with c2:
st.text('Level by lec')
fig = px.pie(data_frame= df , names='level', values='num_lectures' , color_discrete_sequence=['green' , 'orange' , 'yellow' ,'red'])
st.plotly_chart(fig , use_container_width=True)
#with c3:
st.text('Subject by subscribe')
fig = px.pie(data_frame= df , names='subject', values='num_subscribers' , hole=0.6 ,  color_discrete_sequence=['blue' , 'pink' , 'brown' ,'red'])
st.plotly_chart(fig , use_container_width=True)
