import streamlit as st
from streamlit_drawable_canvas import st_canvas
import math
import random

st.set_page_config(page_title="🎱 업그레이드 당구 게임")

st.title("🎱 업그레이드 당구 게임")
st.markdown("1번 공을 드래그해서 다른 공들을 쳐보세요!")

canvas_width = 600
canvas_height = 400
ball_radius = 15

# 초기 공 데이터 정의
if "balls" not in st.session_state:
    st.session_state.balls = []
    # 공 1개는 중앙에, 나머지는 무작위 배치
    st.session_state.balls.append({
        "x": canvas_width // 2,
        "y": canvas_height // 2,
        "vx": 0,
        "vy": 0,
        "color": "#FFD700"  # 노란색
    })
    for _ in range(4):  # 2~5번 공
        st.session_state.balls.append({
            "x": random.randint(100, canvas_width - 100),
            "y": random.randint(100, canvas_height - 100),
            "vx": 0,
            "vy": 0,
            "color": "#FF6347"  # 빨간색
        })

# 초기화 버튼
if st.button("🔄 게임 초기화"):
    del st.session_state.balls

# 캔버스 그리기 도구
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=2,
    stroke_color="#000000",
    background_color="#228B22",
    update_streamlit=True,
    height=canvas_height,
    width=canvas_width,
    drawing_mode="freedraw",
    key="canvas",
)

# 공 치는 드래그 이벤트 해석 (첫 번째 공만)
if canvas_result.json_data and len(canvas_result.json_data["objects"]) > 0:
    last_line = canvas_result.json_data["objects"][-1]
    if last_line["type"] == "line":
        x1, y1 = last_line["x1"], last_line["y1"]
        x2, y2 = last_line["x2"], last_line["y2"]
        dx = x2 - x1
        dy = y2 - y1
        mag = math.hypot(dx, dy)
        if mag != 0:
            st.session_state.balls[0]["vx"] = dx / 10
            st.session_state.balls[0]["vy"] = dy / 10

# 공 이동 및 충돌 감지
for ball in st.session_state.balls:
    ball["x"] += ball["vx"]
    ball["y"] += ball["vy"]
    # 벽 튕기기
    if ball["x"] - ball_radius < 0 or ball["x"] + ball_radius > canvas_width:
        ball["vx"] *= -1
    if ball["y"] - ball_radius < 0 or ball["y"] + ball_radius > canvas_height:
        ball["vy"] *= -1
    # 마찰
    ball["vx"] *= 0.98
    ball["vy"] *= 0.98

# 공끼리 충돌 처리 (간단한 반사)
def handle_collision(b1, b2):
    dx = b1["x"] - b2["x"]
    dy = b1["y"] - b2["y"]
    dist = math.hypot(dx, dy)
    if dist < ball_radius * 2:
        # 단순 반사
        b1["vx"], b2["vx"] = b2["vx"], b1["vx"]
        b1["vy"], b2["vy"] = b2["vy"], b1["vy"]

# 충돌 검사
n = len(st.session_state.balls)
for i in range(n):
    for j in range(i + 1, n):
        handle_collision(st.session_state.balls[i], st.session_state.balls[j])

# HTML 캔버스로 공 시각화
canvas_code = f"""
<canvas id="ballCanvas" width="{canvas_width}" height="{canvas_height}" style="border:1px solid black;"></canvas>
<script>
    const canvas = document.getElementById('ballCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#228B22';
    ctx.fillRect(0, 0, {canvas_width}, {canvas_height});
"""

for ball in st.session_state.balls:
    canvas_code += f"""
    ctx.beginPath();
    ctx.arc({int(ball["x"])}, {int(ball["y"])}, {ball_radius}, 0, 2 * Math.PI);
    ctx.fillStyle = '{ball["color"]}';
    ctx.fill();
    ctx.stroke();
    """

canvas_code += "</script>"

st.write(canvas_code, unsafe_allow_html=True)
