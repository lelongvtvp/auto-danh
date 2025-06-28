# multi_ld/bot_worker.py

from detectors.stuck_detector import MovementTracker
from detectors.health_bar_checker import is_fighting
from controller.movement_controller import move_random
from controller.target_switcher import switch_target
from controller.treo_manager import press_treo
from patterns.movement_patterns import change_direction
import time

def run_bot(ld_name):
    print(f"[{ld_name}] Khởi động bot...")
    tracker = MovementTracker(threshold=5)

    while True:
        found = False
        for _ in range(5):
            switch_target(ld_name)
            fighting = is_fighting(ld_name)
            if fighting:
                press_treo(ld_name)
                tracker.reset()
                found = True
                break
            else:
                tracker.increase()
                if tracker.is_stuck():
                    print(f"[{ld_name}] Có thể bị kẹt, đổi hướng...")
                    change_direction(ld_name)
                    tracker.reset()
                else:
                    move_random(ld_name, "right", 0.5)
        if not found:
            time.sleep(1)
