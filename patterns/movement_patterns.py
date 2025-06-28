# patterns/movement_patterns.py

from controller.movement_controller import move_random
import random

DIRECTIONS = ["up", "down", "left", "right"]

def change_direction(ld_name):
    """
    Khi bị kẹt, đổi hướng ngẫu nhiên.
    Có thể nâng cấp thành tìm hướng ưu tiên sau.
    """
    new_dir = random.choice(DIRECTIONS)
    print(f"[{ld_name}] Đổi hướng sang {new_dir}")
    move_random(ld_name, new_dir, 0.6)
