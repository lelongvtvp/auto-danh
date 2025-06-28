# controller/movement_controller.py

import random
import time
import subprocess
from config.settings import ACTION_DELAY

def swipe_direction(ld_name, direction, duration_ms=500):
    # Tọa độ trung tâm màn hình LDPlayer (ví dụ 720x1280)
    center_x, center_y = 540, 960

    distance = 300  # độ dài vuốt nửa màn hình

    if direction == "UP":
        x1, y1, x2, y2 = center_x, center_y, center_x, center_y - distance
    elif direction == "DOWN":
        x1, y1, x2, y2 = center_x, center_y, center_x, center_y + distance
    elif direction == "LEFT":
        x1, y1, x2, y2 = center_x, center_y, center_x - distance, center_y
    elif direction == "RIGHT":
        x1, y1, x2, y2 = center_x, center_y, center_x + distance, center_y
    else:
        return

    cmd = f'adb -s {ld_name} shell input swipe {x1} {y1} {x2} {y2} {duration_ms}'
    subprocess.run(cmd, shell=True)
    print(f"[MOVE] Vuốt theo hướng {direction}")
    time.sleep(ACTION_DELAY)

def move_random(ld_name):
    direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
    swipe_direction(direction, duration_ms=400)
