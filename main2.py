# -----------------------------
# 별 정보 입력
# -----------------------------
st.sidebar.header("⭐ 별 물리량 계산")

distance_pc = st.sidebar.number_input(
    "거리 (pc)",
    min_value=0.1,
    value=10.0
)

apparent_mag = st.sidebar.number_input(
    "겉보기등급(m)",
    value=5.0
)

temperature = st.sidebar.number_input(
    "표면온도(K)",
    value=5778.0
)
