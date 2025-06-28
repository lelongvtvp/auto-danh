# patterns/movement_patterns.py

from controller.movement_controller import move_random, swipe_direction
import random

DIRECTIONS = ["up", "down", "left", "right"]

def change_direction(ld_name):
    new_dir = random.choice(DIRECTIONS)
    print(f"[{ld_name}] Đổi hướng sang {new_dir}")
    swipe_direction(ld_name, new_dir, duration_ms=600)

