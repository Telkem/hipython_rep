import streamlit as st

############################# button click 
st.button('Reset', type='primary')

def button_write():
    st.write('버튼이 클릭되었습니다.')
st.button('activate', on_click=button_write)

clicked = st.button('activate2', type='primary')
if clicked:
    st.write('버튼2가 클릭되었습니다.')

###################################

st.header("같은 버튼 여러개 만들기")
for i in range(5):
    st.button('activate', type='primary', key=f'act_btn_{i}')

#######################################
st.title('Title')
st.header('header')
st.subheader('subheader')

st.write('write 문장입니다.')
st.text('text 문장입니다.')
st.markdown(
    '''
    여기는 메인 텍스트입니다.\n
    :red[Red], :blue[Blue], :green[Green]\n
    **굵게도 할 수 있고** *이탤릭체*로도 표현 할 수 있다.
    '''
)

st.code(
    '''
st.title('Title')
st.header('header')
st.subheader('subheader')
    '''
    ,language="python"
)

st.divider()

st.button('Hello',icon='✔') #secondary type
st.button('Hello',type='primary')
st.button('Hello',key='1',type='primary', disabled=True)



