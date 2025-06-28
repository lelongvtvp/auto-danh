# controller/adb_controller.py

import subprocess
import time
def adb_tap(ld_name, x, y):
    cmd = f'adb -s {ld_name} shell input tap {x} {y}'
    subprocess.run(cmd, shell=True)

def adb_keyevent(ld_name, key_code):
    cmd = f'adb -s {ld_name} shell input keyevent {key_code}'
    subprocess.run(cmd, shell=True)

def adb_screencap(ld_name, save_path="screen.png"):
    subprocess.run(f"adb -s {ld_name} shell screencap -p /sdcard/screen.png", shell=True)
    subprocess.run(f"adb -s {ld_name} pull /sdcard/screen.png {save_path}", shell=True)
    time.sleep(0.2)  # Thêm delay nhỏ để đảm bảo ảnh được cập nhật
