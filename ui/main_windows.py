# ui/main_window.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QMessageBox
from multi_ld.ld_scanner import get_running_ldplayers
from multi_ld.manager import start_bot_for_ld, stop_bot_for_ld

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Farm Manager")
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()
        self.label = QLabel("Các LDPlayer đang mở:")
        self.list_ld = QListWidget()
        self.btn_refresh = QPushButton("🔄 Quét lại")
        self.btn_start = QPushButton("▶️ Chạy bot")
        self.btn_stop = QPushButton("⛔ Dừng bot")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.list_ld)
        self.layout.addWidget(self.btn_refresh)
        self.layout.addWidget(self.btn_start)
        self.layout.addWidget(self.btn_stop)
        self.setLayout(self.layout)

        self.btn_refresh.clicked.connect(self.load_ldplayers)
        self.btn_start.clicked.connect(self.start_bot)
        self.btn_stop.clicked.connect(self.stop_bot)

        self.load_ldplayers()

    def load_ldplayers(self):
        self.list_ld.clear()
        lds = get_running_ldplayers()
        if not lds:
            QMessageBox.information(self, "Thông báo", "Không phát hiện LDPlayer nào đang chạy.")
        else:
            for ld in lds:
                self.list_ld.addItem(ld)

    def get_selected_ld(self):
        item = self.list_ld.currentItem()
        if item:
            return item.text()
        return None

    def start_bot(self):
        ld_name = self.get_selected_ld()
        if ld_name:
            start_bot_for_ld(ld_name)
            QMessageBox.information(self, "Bot", f"Đã bật bot cho {ld_name}")
        else:
            QMessageBox.warning(self, "Lỗi", "Chọn một LDPlayer trước.")

    def stop_bot(self):
        ld_name = self.get_selected_ld()
        if ld_name:
            stop_bot_for_ld(ld_name)
            QMessageBox.information(self, "Bot", f"Đã dừng bot cho {ld_name}")
        else:
            QMessageBox.warning(self, "Lỗi", "Chọn một LDPlayer trước.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
