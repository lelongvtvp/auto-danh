# controller/target_switcher.py

from controller.adb_controller import adb_tap
from config.settings import SWITCH_TARGET_X, SWITCH_TARGET_Y, ACTION_DELAY
import time

def switch_target():
    print("[ACTION] Nhấn nút Chuyển Mục Tiêu")
    adb_tap(SWITCH_TARGET_X, SWITCH_TARGET_Y)
    time.sleep(ACTION_DELAY)
