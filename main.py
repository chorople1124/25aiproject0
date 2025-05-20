import streamlit as st

st.set_page_config(page_title="🧩 미로 탈출 게임", layout="centered")

st.title("🧩 미로 탈출 게임")
st.caption("WASD 키를 눌러 캐릭터(🧍)를 출구(🚪)까지 이동하세요!")

# 미로 구성 (0: 길, 1: 벽, S: 시작, E: 출구)
maze = [
    ['1', '1', '1', '1', '1', '1', '1'],
    ['1', 'S', '0', '0', '1', 'E', '1'],
    ['1', '1', '1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1'],
]

# 캐릭터 시작 위치 찾기
if "player_pos" not in st.session_state:
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                st.session_state.player_pos = (i, j)

# 이동 함수
def move(dx, dy):
    x, y = st.session_state.player_pos
    new_x, new_y = x + dx, y + dy
    if maze[new_x][new_y] != '1':
        st.session_state.player_pos = (new_x, new_y)

# 키보드 컨트롤
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("🔼"):
        move(-1, 0)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("◀️"):
        move(0, -1)
with col3:
    if st.button("▶️"):
        move(0, 1)

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("🔽"):
        move(1, 0)

# 화면 출력
emoji_map = {
    '1': '🟥',  # 벽
    '0': '⬜️',  # 길
    'S': '⬜️',
    'E': '🚪',
}

output = ""
for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if (i, j) == st.session_state.player_pos:
            output += '🧍'
        else:
            output += emoji_map.get(cell, '⬜️')
    output += '\n'

st.markdown(f"```{output}```")

# 승리 조건
x, y = st.session_state.player_pos
if maze[x][y] == 'E':
    st.success("🎉 축하합니다! 미로를 탈출했어요!")
    if st.button("🔁 다시 시작"):
        del st.session_state.player_pos
        st.experimental_rerun()
