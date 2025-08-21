import streamlit as st

img1 = 'https://i.ibb.co/YFwM64MH/1.jpg'
img2 = 'https://ic.zigbang.com/ic/items/45726063/1.jpg?w=400&h=300&q=70&a=1'
img3 = 'https://ic.zigbang.com/ic/items/45596346/1.jpg?w=400&h=300&q=70&a=1'

homes = {}
##############################################################################

st.markdown(
    f'''
    <style>
    .st-key-homes > div {{
      background-color: #ffffff;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
      display: flex;
      flex-direction: column;
      gap: 15px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }}
    .st-key-homes > div > div::before{{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        opacity: 0.2; /* 배경 이미지 투명도 조절 */
    }}
    .st-key-home1::before{{
        background-image: url({img1});
    }}
    .st-key-home2::before{{
        background-image: url({img2});
    }}
    .st-key-home3::before{{
        background-image: url({img3});
    }}
    .stSidebar {{
        display: flex;
        flex-direction: column;
        height: 100vh !important; /* 뷰포트 높이 100%로 설정하여 하단 고정 효과를 줍니다. */
    }}
    .st-key-fixed-buttons {{
        display: flex;
        margin-top: auto; /* 상단 여백을 최대로 설정하여 버튼을 하단으로 밀어냅니다. */
        padding: 10px; /* 위아래 패딩을 하나로 통합 */
        border-top: 1px solid #e0e0e0;
        background-color: #f0f2f6; /* 사이드바 배경색과 동일하게 설정하여 자연스럽게 연결 */
        position: sticky; /* 스크롤에 따라 하단에 고정 */
        bottom: 0; /* 하단에서 0px 위치에 고정 */
        z-index: 1000; /* 다른 요소 위로 올라오도록 설정 */
    }}
    </style>
    ''',
    unsafe_allow_html=True
)


##############################################################################
st.sidebar.selectbox('연령대를 선택하세요',['선택안함', '20대', '30대', '40대', '50대'])

st.sidebar.divider()
def format_deposit_value(value):
    if value == 0:
        return '0원'
    if value == 20000:
        return '상관없음'
    if value >= 10000:
        return f'{value / 10000}억'
    return f'{value}만원'

deposit = st.sidebar.slider(
    '원하는 보증금 범위를 선택하세요',
    min_value=0,
    max_value=20000,
    value=5000,
    step=100,
)
st.sidebar.write(
    format_deposit_value(deposit)
)

st.sidebar.divider()
def format_rent_value(value):
    if value == 0:
        return '0원'
    if value == 200:
        return '상관없음'
    return f'{value}만원'

rent = st.sidebar.slider(
    '원하는 월세 범위를 선택하세요',
    min_value=0,
    max_value=200,
    value=100,
    step=10,
)
st.sidebar.write(
    format_rent_value(rent)
)


st.sidebar.divider()
st.sidebar.selectbox('평수를 선택하세요', ['선택 안함', '~5', '~10', '~15', '~20', '~25', '~30 이상'])

st.sidebar.divider()
st.sidebar.selectbox('방 개수를 선택하세요', ['선택 안함', '1개', '2개', '3개 이상'])

st.sidebar.divider()
with st.sidebar.expander('상세 필터'):
    st.checkbox('주차 가능')
    st.checkbox('관리비 있음')
    st.checkbox('반려동물 가능')
    st.checkbox('반지하 포함')
    st.checkbox('세탁기')
    st.checkbox('건조기')
    st.checkbox('에어컨')
    st.checkbox('가스레인지')
    st.checkbox('인덕션')
    st.checkbox('엘리베이터')
    st.checkbox('역 근처')
    
with st.sidebar.container(key = 'fixed-buttons'):
    side_col1, side_col2 = st.columns(2)
    with side_col1:
        st.button('이전', use_container_width=True)
    with side_col2:
        st.button('확인', use_container_width=True)
    

##############################################################################


##############################################################################
def home_info(num ,header, point, address, standard):
    with st.container(key='home' + str(num)):
            st.header(header)
            st.write(point)
            st.write(address)
            homes['home' + str(num)] = standard


homes['home1'] = '거리'
homes['home2'] = '가격'
homes['home3'] = '치안'

def show_homes(option):
    num=1
    with st.container(key='homes'):
        if (option == '종합') | (option == '거리'):
            home_info(
                num,
                '**매물1** :선택한 지역 1순위로 반영',
                '매물의 특징: 거리가 가깝습니다!',
                '서울 강남구, 20평, 방 3개, 보증금 1,000만원, 월세 45만원',
                homes['home' + str(num)]
            )
        num += 1
        if (option == '종합') | (option == '가격'):
            home_info(
                num,
                '**매물2** :선택한 예산 1순위로 반영',
                '매물의 특징: 가격이 저렴합니다!',
                '서울 마포구, 15평, 방 1개, 보증금 500만원, 월세 30만원',
                homes['home' + str(num)]
            )
        num += 1
        if (option == '종합') | (option == '치안'):
            home_info(
                num,
                '**매물3** :치안 1순위로 반영',
                '매물의 특징: 치안이 좋습니다!',
                '서울 관악구, 25평, 방 2개, 보증금 2,000만원, 월세 40만원',
                homes['home' + str(num)]
            )
            
            
main_col1, main_col2, main_col3 ,main_col4 = st.columns(4)

with main_col1:
    all = st.button('종합')
with main_col2:
    cost = st.button('가격')
with main_col3:
    safety = st.button('치안')
with main_col4:
    distance = st.button('거리')

if cost:
    show_homes('가격')
elif safety:
    show_homes('치안')
elif distance:
    show_homes('거리')
else:
    show_homes('종합')