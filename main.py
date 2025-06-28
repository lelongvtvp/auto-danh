# main.py
import time
from detectors.health_bar_checker import is_fighting
from controller.movement_controller import move_random
from controller.target_switcher import switch_target
from controller.treo_manager import press_treo

def run_bot():
    print("🤖 AutoFarm LDPlayer bắt đầu...")
    while True:
        print("[BOT] Kiểm tra trạng thái...")
        if is_fighting():
            print("✅ Đang đánh quái → nghỉ 2s")
            time.sleep(2)
            continue

        print("❌ Không có quái → bắt đầu tìm...")
        for _ in range(10):
            move_random()
            switch_target()
            if is_fighting():
                print("🎯 Đã tìm thấy quái → nhấn Treo")
                press_treo()
                break
            time.sleep(0.5)
        
        # Đợi trước khi bắt đầu chu kỳ mới
        time.sleep(1.5)

if __name__ == "__main__":
    run_bot()
