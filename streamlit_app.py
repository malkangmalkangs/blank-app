import streamlit as st
import pydeck as pdk

st.title("🗺️ Hello Minkang")

# 위치 데이터
data = [
    {"lat": 35.017, "lon": 126.717, "name": "식당 A"},
    {"lat": 35.027, "lon": 126.727, "name": "식당 B"},
    {"lat": 35.037, "lon": 126.737, "name": "식당 C"},
]

# DeckGL 지도 레이어
layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position='[lon, lat]',
    get_radius=200,
    get_color=[255, 0, 0],
    pickable=True
)

# 뷰포트
view_state = pdk.ViewState(
    latitude=35.027, longitude=126.727, zoom=12
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"}))
