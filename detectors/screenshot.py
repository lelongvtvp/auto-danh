# detectors/screenshot.py

import cv2
import os
from controller.adb_controller import adb_screencap

def capture_screen(save_path="temp_screen.png"):
    adb_screencap(save_path)
    if os.path.exists(save_path):
        image = cv2.imread(save_path)
        return image
    else:
        print("[ERROR] Không tìm thấy ảnh màn hình đã chụp.")
        return None
