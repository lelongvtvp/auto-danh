# # multi_ld/bot_worker.py


import time
from threading import Event
from detectors.stuck_detector import MovementTracker
from detectors.health_bar_checker import is_fighting
from controller.movement_controller import move_random
from controller.target_switcher import switch_target
from controller.treo_manager import press_treo
from patterns.movement_patterns import change_direction

def run_bot(ld_name, stop_event: Event):
    print(f"[{ld_name}] Khởi động bot...")
    tracker = MovementTracker(threshold=5)

    while not stop_event.is_set():
        print(f"[{ld_name}] ➤ Kiểm tra trạng thái đánh quái...")
        if is_fighting(ld_name):
            print(f"[{ld_name}] ✅ Đang đánh quái → nghỉ 2s")
            time.sleep(2)
            tracker.reset()
            continue

        print(f"[{ld_name}] ❌ Không thấy quái → Bắt đầu tìm kiếm...")
        for _ in range(10):
            if stop_event.is_set(): return  # ⛔ Dừng tức thì nếu có lệnh
            switch_target(ld_name)
            time.sleep(0.4)

            if is_fighting(ld_name):
                print(f"[{ld_name}] 🎯 Phát hiện quái → Nhấn Treo và nghỉ")
                press_treo(ld_name)
                time.sleep(1.0)
                tracker.reset()
                break
            else:
                tracker.increase()
                if tracker.is_stuck():
                    print(f"[{ld_name}] 🔁 Có thể bị kẹt → Đổi hướng...")
                    change_direction(ld_name)
                    tracker.reset()
                else:
                    move_random(ld_name)
                    time.sleep(0.5)

        time.sleep(1.0)
    
    print(f"[{ld_name}] 🛑 Bot đã được dừng.")
