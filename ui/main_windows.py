
# import sys
# from PyQt5.QtWidgets import QApplication, QMessageBox
# from .style import Ui_MainWindow        # ✅ Đúng rồi
# from multi_ld.ld_scanner import get_running_ldplayers
# from multi_ld.manager import start_bot_for_ld, stop_bot_for_ld, get_ld_status, stop_all_bots, run_all_bots


# class MainController(Ui_MainWindow):
#     def __init__(self):
#         super().__init__()

#         self.btn_refresh.clicked.connect(self.load_ldplayers)
#         self.btn_start.clicked.connect(self.start_bot)
#         self.btn_stop.clicked.connect(self.stop_bot)
#         self.btn_start_all.clicked.connect(self.start_all_bots)
#         self.btn_stop_all.clicked.connect(self.stop_all_bots)

#         self.load_ldplayers()

#     def load_ldplayers(self):
#         self.list_ld.clear()
#         lds = get_running_ldplayers()
#         if not lds:
#             QMessageBox.information(self, "Thông báo", "Không phát hiện LDPlayer nào đang chạy.")
#         else:
#             for ld in lds:
#                 status = get_ld_status(ld)
#                 self.list_ld.addItem(f"{ld} - {status}")

#     def get_selected_ld(self):
#         item = self.list_ld.currentItem()
#         return item.text().split(" - ")[0] if item else None

#     def start_bot(self):
#         ld = self.get_selected_ld()
#         if ld:
#             start_bot_for_ld(ld)
#             self.load_ldplayers()
#             QMessageBox.information(self, "Bot", f"✅ Đã bật bot cho {ld}")
#         else:
#             QMessageBox.warning(self, "Lỗi", "⚠️ Chọn một LDPlayer trước.")

#     def stop_bot(self):
#         ld = self.get_selected_ld()
#         if ld:
#             stop_bot_for_ld(ld)
#             self.load_ldplayers()
#             QMessageBox.information(self, "Bot", f"⛔ Đã dừng bot cho {ld}")
#         else:
#             QMessageBox.warning(self, "Lỗi", "⚠️ Chọn một LDPlayer trước.")

#     def stop_all_bots(self):
#         stop_all_bots()
#         self.load_ldplayers()
#         QMessageBox.information(self, "Bot", "🛑 Đã dừng tất cả bot.")

#     def start_all_bots(self):
#         run_all_bots()
#         self.load_ldplayers()
#         QMessageBox.information(self, "Bot", "▶️ Đã bật bot cho tất cả LDPlayer.")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainController()
#     window.show()
#     sys.exit(app.exec_())
# ui/main_windows.py
# ui/main_windows.py
# ui/main_windows.py
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui   import QIcon, QColor, QMovie
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QProgressBar, QFrame, QListWidgetItem,
    QSizePolicy
)

# ---- helper từ style.py (không Toast) ----
from ui.style import (
    _DEFAULT_THEME, load_settings, build_qss,
    Particle, SeasonEffect, FrostListWidget,
    animate_item_bg
)

# ---- stub cho multi_ld (thay bằng code thật nếu đã có) ----
try:
    from multi_ld.ld_scanner import get_running_ldplayers
    from multi_ld.manager import (
        start_bot_for_ld, stop_bot_for_ld, get_ld_status,
        stop_all_bots, run_all_bots
    )
except ImportError:
    print("⚠️  Dùng stub multi_ld.")
    get_running_ldplayers = lambda: ["emulator-5554"]
    start_bot_for_ld = stop_bot_for_ld = stop_all_bots = run_all_bots = lambda *a, **k: None
    get_ld_status = lambda _: "Stop"

CONFIG_DIR = Path("config")
CONFIG_DIR.mkdir(exist_ok=True)


# ---------- Khung trạng thái cố định ----------
class StatusBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(10, 4, 10, 4)
        lay.addWidget(self.label)

        self.setFixedHeight(32)
        self.set_status("")

    def set_status(self, text, level="info"):
        colors = {"info": "#00796b", "warning": "#f57c00", "error": "#d32f2f"}
        self.setStyleSheet(
            f"""
            QFrame {{ background:{colors[level]}; border-radius:6px; }}
            QLabel {{ color:white; font-weight:500; }}
            """
        )
        self.label.setText(text)


# ---------- Main window ----------
class MainController(QWidget):
    def __init__(self):
        super().__init__()

        # ---- theme & style (luôn sáng) ----
        self.theme = _DEFAULT_THEME.copy()
        self.settings = load_settings()
        self.setStyleSheet(build_qss(self.theme))

        # ---- window ----
        self.setWindowTitle("🌿 Auto Farm Manager")
        self.setWindowIcon(QIcon("assets/logo.png"))
        self.resize(560, 540)

        # ---- root layout (quan trọng!) ----
        self.root_layout = QVBoxLayout(self)
        self.root_layout.setSpacing(12)
        self.root_layout.setContentsMargins(16, 12, 16, 12)

        # ---- tiêu đề căn giữa ----
        top_bar = QHBoxLayout()
        title = QLabel("📋 Danh sách LDPlayer đang chạy")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        top_bar.addStretch()
        top_bar.addWidget(title)
        top_bar.addStretch()
        self.root_layout.addLayout(top_bar)

        # ---- hiệu ứng nền (tùy settings) ----
        if self.settings.get("particle", True):
            self.effect = Particle(self)
            self.effect.lower(); self.effect.resize(self.size())
        elif self.settings.get("season_effect") in {"snow", "leaf"}:
            asset = {"snow": "assets/snowflake.png",
                     "leaf": "assets/leaf.png"}[self.settings["season_effect"]]
            self.effect = SeasonEffect(asset, self)
            self.effect.lower(); self.effect.resize(self.size())

        # ---- danh sách LD ----
        self.list = FrostListWidget(self.settings.get("blur", False))
        self.root_layout.addWidget(self.list)

        # ---- nhóm nút 1 ----
        row1 = QHBoxLayout()
        self.btn_refresh = QPushButton("🔄 Quét lại")
        self.btn_start   = QPushButton("▶️ Chạy bot")
        self.btn_stop    = QPushButton("⛔ Dừng bot")
        for b in (self.btn_refresh, self.btn_start, self.btn_stop):
            b.setCursor(Qt.PointingHandCursor)
            row1.addWidget(b)
        self.root_layout.addLayout(row1)

        # GIF cho nút start (nếu có)
        gif_path = Path("assets/run.gif")
        if gif_path.exists():
            gif = QMovie(str(gif_path))
            gif.frameChanged.connect(lambda _: self.btn_start.setIcon(QIcon(gif.currentPixmap())))
            gif.start()

        # ---- separator ----
        line = QFrame(); line.setFrameShape(QFrame.HLine)
        self.root_layout.addWidget(line)

        # ---- nhóm nút 2 ----
        row2 = QHBoxLayout()
        self.btn_start_all = QPushButton("▶️ Chạy tất cả bot")
        self.btn_stop_all  = QPushButton("🛑 Dừng tất cả bot")
        for b in (self.btn_start_all, self.btn_stop_all):
            b.setCursor(Qt.PointingHandCursor)
            row2.addWidget(b)
        self.root_layout.addLayout(row2)

        # ---- progress ----
        self.progress = QProgressBar(); self.progress.hide()
        self.root_layout.addWidget(self.progress)

        # ---- status bar cố định ----
        self.status = StatusBar()
        self.root_layout.addWidget(self.status)

        # ---- kết nối ----
        self.btn_refresh.clicked.connect(self.load_ldplayers)
        self.btn_start.clicked.connect(self.start_bot)
        self.btn_stop.clicked.connect(self.stop_bot)
        self.btn_start_all.clicked.connect(self.start_all)
        self.btn_stop_all.clicked.connect(self.stop_all)

        # ---- initial load ----
        self.load_ldplayers()

    # ---- resize để giữ hiệu ứng nền ----
    def resizeEvent(self, e):
        if hasattr(self, "effect"):
            self.effect.resize(self.size())
        super().resizeEvent(e)

    # ---- helper LD ----
    def load_ldplayers(self):
        self.list.clear()
        lds = get_running_ldplayers()
        if not lds:
            self.status.set_status(" Không phát hiện LDPlayer đang chạy", "warning")
            return
        for ld in lds:
            self._add_item(ld, get_ld_status(ld))
        self.status.set_status(f"Phát hiện {len(lds)} LDPlayer", "info")

    def _add_item(self, ld, st):
        it = QListWidgetItem(f"{ld} – {st}")
        it.setBackground({
            "Running": QColor("#C8E6C9"),
            "Stop":    QColor("#FFF9C4"),
            "Error":   QColor("#FFCDD2")
        }.get(st, QColor("#ffffff")))
        self.list.addItem(it)

    def _sel_ld(self):
        cur = self.list.currentItem()
        return cur.text().split(" – ")[0] if cur else None

    # ---- actions ----
    def start_bot(self):
        ld = self._sel_ld()
        if not ld:
            self.status.set_status(" Chọn LDPlayer trước", "warning")
            return
        start_bot_for_ld(ld)
        self._update_item(ld, "Running", " Đã bật bot cho")

    def stop_bot(self):
        ld = self._sel_ld()
        if not ld:
            self.status.set_status(" Chọn LDPlayer trước", "warning")
            return
        stop_bot_for_ld(ld)
        self._update_item(ld, "Stop", " Đã dừng bot cho")

    def start_all(self):
        total = self.list.count()
        if total:
            self._bulk(run_all_bots, total, " Đã bật bot cho tất cả", "info")

    def stop_all(self):
        total = self.list.count()
        if total:
            self._bulk(stop_all_bots, total, " Đã dừng tất cả bot", "error")

    # ---- helpers ----
    def _update_item(self, ld, newst, msg):
        for i in range(self.list.count()):
            it = self.list.item(i)
            if it.text().startswith(ld):
                animate_item_bg(
                    it,
                    it.background().color(),
                    {"Running": QColor("#C8E6C9"),
                     "Stop":    QColor("#FFF9C4")}[newst]
                )
                it.setText(f"{ld} – {newst}")
                break
        self.status.set_status(f"{msg} {ld}", "info" if newst == "Running" else "error")

    def _bulk(self, func, total, msg, level):
        self.progress.setMaximum(total); self.progress.setValue(0); self.progress.show()
        for i in range(1, total + 1):
            func(); self.progress.setValue(i); QApplication.processEvents()
        self.progress.hide()
        self.load_ldplayers()                       # cập nhật list trước
        self.status.set_status(msg, level)


# ---------- run ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainController()
    win.show()
    sys.exit(app.exec_())
