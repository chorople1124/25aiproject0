<!DOCTYPE html>
<html>
<head>
    <title>공룡 달리기 게임</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
        }
        #game {
            width: 600px;
            height: 200px;
            border: 2px solid black;
            margin: 0 auto;
            position: relative;
            overflow: hidden;
            background-color: #f0f0f0;
        }
        #dino {
            width: 40px;
            height: 40px;
            background-color: green;
            position: absolute;
            bottom: 0;
            left: 50px;
        }
        #obstacle {
            width: 20px;
            height: 40px;
            background-color: red;
            position: absolute;
            bottom: 0;
            left: 600px;
        }
    </style>
</head>
<body>

<h1>🦖 공룡 달리기 게임</h1>
<p>스페이스바를 눌러 점프하세요!</p>

<div id="game">
    <div id="dino"></div>
    <div id="obstacle"></div>
</div>

<py-script>
import js
from pyodide.ffi import create_proxy
import asyncio

game = js.document.getElementById("game")
dino = js.document.getElementById("dino")
obstacle = js.document.getElementById("obstacle")

is_jumping = False
jump_height = 80

async def jump(event):
    global is_jumping
    if event.code == "Space" and not is_jumping:
        is_jumping = True
        for i in range(10):
            dino.style.bottom = f"{i * 8}px"
            await asyncio.sleep(0.02)
        for i in range(10, -1, -1):
            dino.style.bottom = f"{i * 8}px"
            await asyncio.sleep(0.02)
        is_jumping = False

async def move_obstacle():
    while True:
        left = 600
        while left > -20:
            obstacle.style.left = f"{left}px"
            await asyncio.sleep(0.02)
            left -= 4
            # 충돌 감지
            dino_top = int(dino.style.bottom.replace("px", ""))
            if 50 <= left <= 90 and dino_top < 40:
                js.alert("💥 게임 오버!")
                return
        await asyncio.sleep(1)

js.document.addEventListener("keydown", create_proxy(jump))
asyncio.ensure_future(move_obstacle())
</py-script>

</body>
</html>
