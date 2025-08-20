import streamlit as st

#layout 요소
#columns는 요소를 왼쪽->오른쪽으로 배치할 수 있다

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        '오늘의 온도',
        value='35도',
        delta='+3'
    )
with col2:
    st.metric(
        '오늘의 미세먼지',
        value='좋음',
        delta='-30',
        delta_color='inverse'
    )
with col3:
    st.metric(
        '오늘의 습도',
        value='30%'
    )
    
##
st.markdown('---')

data = {
    '이름' : ['홍길동', '김길동', '박길동'],
    '나이' : [10,20,30]
}
import pandas as pd
df = pd.DataFrame(data)
st.dataframe(df)

st.divider()
st.table(df)

st.divider()
st.json(data)

#datafile.csv > table 출력 > px 차트 > st.plotly_chart()

df_co2 = pd.read_csv('./data/CO2_Emissions.csv')
x_options = ['Cylinders', 'Fuel Type']
y_options = ['CO2 Emissions(g/km)','Fuel Consumption Comb (mpg)', 'Engine Size(L)']
hue_options = ['Vehicle Class','Transmission']

df_co2_head = df_co2.head()
st.table(df_co2_head)
import plotly.express as px

x_option = st.selectbox(
    'Select X-axis',
    index=None,
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

hue_option = st.selectbox(
    'Select Hue',
    index=None,
    options=hue_options
)
if (x_option != None) & (y_option != None):
    if hue_option != None:
        fig = px.box(data_frame=df_co2, x=x_option,
            y=y_option, color = hue_option
        )
    else:  
        fig = px.box(data_frame=df_co2, x=x_option,
            y=y_option
        )
    fig.update_xaxes(showline=True, linecolor='black', linewidth=3)
    fig.update_yaxes(showline=True, linecolor='black', linewidth=3)
    st.plotly_chart(fig)