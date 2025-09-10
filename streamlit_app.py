import streamlit as st
import pydeck as pdk
import pandas as pd

st.title("🗺️ 나주 맛집 3D 지도 예시")

# 샘플 데이터 (위도, 경도, 값)
data = pd.DataFrame({
    'lat': [35.017, 35.027, 35.037],
    'lon': [126.717, 126.727, 126.737],
    'value': [10, 30, 50]   # 3D 높이로 표현할 값
})

# 3D ColumnLayer (막대 그래프)
layer = pdk.Layer(
    "ColumnLayer",
    data,
    get_position='[lon, lat]',
    get_elevation='value',        # value 값을 높이로
    elevation_scale=100,          # 스케일
    radius=200,                   # 원기둥 반지름
    get_fill_color='[200, 30, 0, 160]',
    pickable=True,
    auto_highlight=True,
)

# 지도 초기 뷰
view_state = pdk.ViewState(
    latitude=35.027,
    longitude=126.727,
    zoom=12,
    pitch=50   # 기울여서 3D 효과
)

# 지도 출력
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "위도: {lat}\n경도: {lon}\n값: {value}"}))