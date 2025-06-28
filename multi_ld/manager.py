# from multi_ld.ld_scanner import get_running_ldplayers
# from multi_ld.bot_worker import run_bot
# from concurrent.futures import ThreadPoolExecutor
# import threading
# executor = ThreadPoolExecutor()
# running_bots = {}
# stop_events = {}
# ld_statuses = {}  # Trạng thái từng LD

# def run_all_bots():
#     ld_names = get_running_ldplayers()
#     print(f"🧠 Phát hiện {len(ld_names)} LDPlayer đang mở: {ld_names}")

#     with ThreadPoolExecutor(max_workers=30) as executor:
#         for ld in ld_names:
#             executor.submit(run_bot, ld)

# def start_bot_for_ld(ld_name):
#     if ld_name not in running_bots or ld_statuses.get(ld_name) == "⛔ Đã dừng":
#         future = executor.submit(run_bot, ld_name)
#         running_bots[ld_name] = future
#     # ✅ Cập nhật lại trạng thái DÙ ĐÃ CÓ
#     ld_statuses[ld_name] = "✅ Đang chạy"

# def stop_bot_for_ld(ld_name):
#     if ld_name in stop_events:
#         stop_events[ld_name].set()
#         ld_statuses[ld_name] = "⛔ Đã dừng"
#         print(f"[{ld_name}] Đã gửi yêu cầu dừng bot.")
# def stop_all_bots():
#     for ld_name in list(running_bots.keys()):
#         stop_bot_for_ld(ld_name)
# def get_ld_status(ld_name):
#     return ld_statuses.get(ld_name, "⏸️ Chưa chạy")

# if __name__ == "__main__":
#     run_all_bots()

# from multi_ld.ld_scanner import get_running_ldplayers
# from multi_ld.bot_worker import run_bot
# from concurrent.futures import ThreadPoolExecutor
# from threading import Event

# executor = ThreadPoolExecutor()
# running_bots = {}      # ld_name -> future
# stop_events = {}       # ld_name -> Event
# ld_statuses = {}       # ld_name -> status string

# def start_bot_for_ld(ld_name):
#     if ld_name not in running_bots:
#         stop_event = Event()
#         future = executor.submit(run_bot, ld_name, stop_event)
#         running_bots[ld_name] = future
#         stop_events[ld_name] = stop_event
#         ld_statuses[ld_name] = "✅ Đang chạy"

# def stop_bot_for_ld(ld_name):
#     if ld_name in stop_events:
#         stop_events[ld_name].set()
#         ld_statuses[ld_name] = "⛔ Đã dừng"
#         print(f"[{ld_name}] Đã gửi tín hiệu dừng bot.")
#     else:
#         print(f"[{ld_name}] ⚠️ Không có bot đang chạy.")

# def stop_all_bots():
#     for ld_name in list(running_bots.keys()):
#         stop_bot_for_ld(ld_name)

# def get_ld_status(ld_name):
#     return ld_statuses.get(ld_name, "⏸️ Chưa chạy")
from multi_ld.ld_scanner import get_running_ldplayers
from multi_ld.bot_worker import run_bot
from concurrent.futures import ThreadPoolExecutor
import threading

# Bộ điều khiển đa luồng
executor = ThreadPoolExecutor()
running_bots = {}              # { ld_name: Future }
ld_statuses = {}               # { ld_name: "⏸️ Chưa chạy" | "✅ Đang chạy" | "⛔ Đã dừng" }
stop_events = {}               # { ld_name: threading.Event }

# 🔁 Chạy tất cả bot
def run_all_bots():
    ld_names = get_running_ldplayers()
    print(f"🧠 Phát hiện {len(ld_names)} LDPlayer đang mở: {ld_names}")

    for ld in ld_names:
        start_bot_for_ld(ld)

# ▶️ Chạy bot cho một LD
def start_bot_for_ld(ld_name):
    if ld_name not in running_bots or running_bots[ld_name].done():
        stop_events[ld_name] = threading.Event()
        future = executor.submit(run_bot, ld_name, stop_events[ld_name])
        running_bots[ld_name] = future
        ld_statuses[ld_name] = "✅ Đang chạy"
        print(f"[{ld_name}] ▶️ Đã khởi chạy bot.")

# ⛔ Dừng bot cho một LD
def stop_bot_for_ld(ld_name):
    if ld_name in stop_events:
        stop_events[ld_name].set()
        ld_statuses[ld_name] = "⛔ Đã dừng"
        print(f"[{ld_name}] ⛔ Đã gửi tín hiệu dừng bot.")

# 🛑 Dừng tất cả bot
def stop_all_bots():
    for ld_name in list(running_bots.keys()):
        stop_bot_for_ld(ld_name)

# 📋 Lấy trạng thái hiện tại của một LD
def get_ld_status(ld_name):
    return ld_statuses.get(ld_name, "⏸️ Chưa chạy")
