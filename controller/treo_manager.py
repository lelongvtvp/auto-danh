# controller/treo_manager.py

from controller.adb_controller import adb_tap
from config.settings import TREO_BUTTON_X, TREO_BUTTON_Y, ACTION_DELAY
import time

def press_treo(ld_name):
    print(f"[{ld_name}] Nhấn nút Treo")
    adb_tap(ld_name, TREO_BUTTON_X, TREO_BUTTON_Y)
    time.sleep(ACTION_DELAY)

