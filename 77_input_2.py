import streamlit as st

#checkbox
agree = st.checkbox('I agree')
if agree:
    st.write("체크했습니다.")
    
def checkbox_write():
    st.write("체크했습니다.")
    
st.checkbox('체크박스', on_change=checkbox_write)


# 세션-상태 값에 저장
if 'checkbox_state' not in st.session_state:
    st.session_state.checkbox_state = False
    
def checkbox_write1():
    st.session_state.checkbox_state = True

if st.session_state.checkbox_state:
    st.write('yes')
st.checkbox('real', on_change=checkbox_write1)


st.divider()
# 토글버튼
selected = st.toggle('Turn on the switch')
if selected:
    st.text('turn on')
else:
    st.text('turn off')
    
    
# selectbox선택지
option = st.selectbox(
    'your selection is',
    options=[f'{i}' for i in range(1,11)],
    index=None,
    placeholder='select a number'
)
if option:
    st.text(f'{option}번을 선택하셨습니다.')
    
    
# radio
genre = st.radio(
    '무슨 영화를 좋아하세요', ['멜로', '스릴러','판타지'],
    index=None, captions=['봄날은 간다', '트리거', '웬즈데이']
)
if genre:
    st.text(f'당신이 좋아하는 영화는 {genre} 장르 입니다.')
    
    
#multiselect
menus = st.multiselect(
    '음식 종류', ['김밥','떡볶이','라면', '햄버거', '피자']
)
if menus:
    st.text(f'내가 선택한 메뉴는 {menus}')
    
#slider
score = st.slider('내 점수 선택',0,100,50,5) # 최소값, 최대값, 시작값, 스텝
st.text(f'score : {score}')

from datetime import time
st_time, end_time = st.slider(
    '공부시간 선택',
    min_value=time(0), max_value=time(20),
    value=(time(9), time(18)),format='HH,mm'
)
st.text(f'공부시간 : {st_time} ~ {end_time}')


# text_input
txt1 = st.text_input('영화제목', placeholder='제목을 입력하세요')
txt2 = st.text_input('비밀', placeholder='비밀', type='password')
st.text(f'텍스트 입력 결과 : {txt1}, {txt2}')



#파일 업로더
#업로드한 파일은 사용자의 세션에 있고 화면을 갱신하면 사라짐
#서버에 저장하려면 별도로 구현해야 함
#데이터베이스에 저장하는 로직도 구현 할 수 있음
file = st.file_uploader(
    '파일 선택', type='csv', accept_multiple_files=False
)
import pandas as pd
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    with open(file.name, 'wb') as out:
        out.write(file.getbuffer())