# multi_ld/manager.py

from multi_ld.ld_scanner import get_running_ldplayers
from multi_ld.bot_worker import run_bot
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor()
running_bots = {}
def run_all_bots():
    ld_names = get_running_ldplayers()
    print(f"🧠 Phát hiện {len(ld_names)} LDPlayer đang mở: {ld_names}")

    with ThreadPoolExecutor(max_workers=30) as executor:
        for ld in ld_names:
            executor.submit(run_bot, ld)
def start_bot_for_ld(ld_name):
    if ld_name not in running_bots:
        future = executor.submit(run_bot, ld_name)
        running_bots[ld_name] = future

def stop_bot_for_ld(ld_name):
    # Giả lập tạm bằng in ra (tùy bạn triển khai terminate sau)
    print(f"[{ld_name}] STOP yêu cầu – Chưa xử lý luồng dừng.")

if __name__ == "__main__":
    run_all_bots()
