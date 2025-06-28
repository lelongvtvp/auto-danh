# multi_ld/ld_scanner.py

import subprocess

def get_running_ldplayers():
    """
    Trả về danh sách LDPlayer đang kết nối adb (ví dụ: emulator-5554, emulator-5556,...)
    """
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]  # Bỏ dòng đầu
    devices = [line.split("\t")[0] for line in lines if "device" in line]
    return devices
