# controller/treo_manager.py

from controller.adb_controller import adb_tap
from config.settings import TREO_BUTTON_X, TREO_BUTTON_Y, ACTION_DELAY
import time

def press_treo():
    print("[ACTION] Nhấn nút Treo")
    adb_tap(TREO_BUTTON_X, TREO_BUTTON_Y)
    time.sleep(ACTION_DELAY)
