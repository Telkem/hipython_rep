import streamlit as st

def show_common_ui():
    st.write("모든 탭에서 공유되는 내용입니다.")
    st.button("공통 버튼")

tab1, tab2 = st.tabs(["탭 1", "탭 2"])

with tab1:
    st.header("탭 1")
    show_common_ui()
    st.text_input("탭 1 전용 입력창")

with tab2:
    st.header("탭 2")
    show_common_ui()
    st.slider("탭 2 전용 슬라이더")