# detectors/screenshot.py

import cv2
import os
from controller.adb_controller import adb_screencap

def capture_screen(ld_name, save_path="temp_screen.png"):
    adb_screencap(ld_name, save_path)
    if os.path.exists(save_path):
        image = cv2.imread(save_path)
        return image
    else:
        print(f"[{ld_name}] ⚠️ Không tìm thấy ảnh sau khi chụp.")
        return None
