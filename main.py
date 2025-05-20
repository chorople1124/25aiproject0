import streamlit as st
import random
import time

st.set_page_config(page_title="공룡 달리기 게임", page_icon="🦖")

st.title("🦖 공룡 달리기 게임")
st.write("스페이스바 대신 버튼을 눌러 장애물을 피하세요!")

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.is_game_over = False

# 게임 종료 시 메시지
if st.session_state.is_game_over:
    st.error("💥 충돌! 게임 오버!")
    st.write(f"🏁 최종 점수: **{st.session_state.score}**")
    if st.button("🔁 다시 시작"):
        st.session_state.score = 0
        st.session_state.is_game_over = False
    st.stop()

# 점프 버튼
if st.button("🆙 점프!"):
    jump = True
else:
    jump = False

# 장애물 등장 여부 (30% 확률)
obstacle = random.choice([True, False, False])

# 화면 표시
if obstacle:
    st.write("🌵 장애물 등장!")
    if jump:
        st.success("🦖 점프 성공!")
        st.session_state.score += 1
    else:
        st.session_state.is_game_over = True
        st.experimental_rerun()
else:
    st.write("🟢 길이 평탄합니다.")
    st.session_state.score += 1

# 점수 표시
st.metric("현재 점수", st.session_state.score)
