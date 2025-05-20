import streamlit as st
from streamlit_drawable_canvas import st_canvas
import math
import random

st.set_page_config(page_title="🎱 간단한 당구 게임")

st.title("🎱 간단한 당구 게임 (마우스로 드래그해서 치기)")
st.caption("첫 번째 공(노란색)을 드래그해서 다른 공들을 쳐보세요!")

canvas_width = 600
canvas_height = 400
ball_radius = 15

# 공 상태 초기화
if "balls" not in st.session_state:
    st.session_state.balls = []
    st.session_state.balls.append({
        "x": canvas_width // 2,
        "y": canvas_height // 2,
        "vx": 0,
        "vy": 0,
        "color": "#FFD700"  # 노란색 (주공)
    })
    for _ in range(4):  # 나머지 공들 (빨간색)
        st.session_state.balls.append({
            "x": random.randint(100, canvas_width - 100),
            "y": random.randint(100, canvas_height - 100),
            "vx": 0,
            "vy": 0,
            "color": "#FF6347"
        })

# 초기화 버튼
if st.button("🔄 다시 시작"):
    del st.session_state.balls
    st.experimental_rerun()

# 드래그 입력 받기
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

# 입력 해석 - 첫 번째 공만 드래그 가능
if canvas_result.json_data and len(canvas_result.json_data["objects"]) > 0:
    line = canvas_result.json_data["objects"][-1]
    if line["type"] == "line":
        dx = line["x2"] - line["x1"]
        dy = line["y2"] - line["y1"]
        mag = math.hypot(dx, dy)
        if mag > 0:
            st.session_state.balls[0]["vx"] = dx / 10
            st.session_state.balls[0]["vy"] = dy / 10

# 충돌 처리
def handle_collision(b1, b2):
    dx = b1["x"] - b2["x"]
    dy = b1["y"] - b2["y"]
    dist = math.hypot(dx, dy)
    if dist < ball_radius * 2:
        # 단순 반사 (속도 교환)
        b1["vx"], b2["vx"] = b2["vx"], b1["vx"]
        b1["vy"], b2["vy"] = b2["vy"], b1["vy"]

# 공 업데이트
for i, ball in enumerate(st.session_state.balls):
    ball["x"] += ball["vx"]
    ball["y"] += ball["vy"]

    # 벽 반사
    if ball["x"] - ball_radius < 0 or ball["x"] + ball_radius > canvas_width:
        ball["vx"] *= -1
    if ball["y"] - ball_radius < 0 or ball["y"] + ball_radius > canvas_height:
        ball["vy"] *= -1

    # 마찰
    ball["vx"] *= 0.97
    ball["vy"] *= 0.97

# 공끼리 충돌
for i in range(len(st.session_state.balls)):
    for j in range(i + 1, len(st.session_state.balls)):
        handle_collision(st.session_state.balls[i], st.session_state.balls[j])

# HTML 캔버스로 공 보여주기
canvas_code = f"""
<canvas id="ballCanvas" width="{canvas_width}" height="{canvas_height}" style="border:1px solid black;"></canvas>
<script>
const ctx = document.getElementById("ballCanvas").getContext("2d");
ctx.fillStyle = "#228B22";
ctx.fillRect(0, 0, {canvas_width}, {canvas_height});
"""

for ball in st.session_state.balls:
    canvas_code += f"""
    ctx.beginPath();
    ctx.arc({int(ball["x"])}, {int(ball["y"])}, {ball_radius}, 0, Math.PI*2);
    ctx.fillStyle = "{ball['color']}";
    ctx.fill();
    ctx.stroke();
    """

canvas_code += "</script>"
st.components.v1.html(canvas_code, height=canvas_height + 10)

