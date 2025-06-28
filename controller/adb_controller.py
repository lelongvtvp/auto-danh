# controller/adb_controller.py

import subprocess

def adb_tap(ld_name, x, y):
    cmd = f'adb -s {ld_name} shell input tap {x} {y}'
    subprocess.run(cmd, shell=True)

def adb_keyevent(ld_name, key_code):
    cmd = f'adb -s {ld_name} shell input keyevent {key_code}'
    subprocess.run(cmd, shell=True)

def adb_screencap(ld_name, save_path="screen.png"):
    cmd = f'adb -s {ld_name} shell screencap -p /sdcard/screen.png'
    subprocess.run(cmd, shell=True)
    cmd = f'adb -s {ld_name} pull /sdcard/screen.png {save_path}'
    subprocess.run(cmd, shell=True)
