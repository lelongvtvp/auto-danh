# controller/target_switcher.py

from controller.adb_controller import adb_tap
from config.settings import SWITCH_TARGET_X, SWITCH_TARGET_Y, ACTION_DELAY
import time

def switch_target(ld_name):
    print(f"[{ld_name}] Nhấn nút Chuyển Mục Tiêu")
    adb_tap(ld_name, SWITCH_TARGET_X, SWITCH_TARGET_Y)
    time.sleep(ACTION_DELAY)

