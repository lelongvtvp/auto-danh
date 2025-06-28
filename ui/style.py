# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QFrame

# class Ui_MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("🌿 Auto Farm Manager")
#         self.setGeometry(300, 200, 500, 420)
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #e0f7fa;
#                 font-family: 'Segoe UI';
#                 font-size: 14px;
#             }
#             QPushButton {
#                 background-color: #4dd0e1;
#                 border: none;
#                 border-radius: 8px;
#                 padding: 8px 12px;
#                 color: white;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #00acc1;
#             }
#             QPushButton:pressed {
#                 background-color: #007c91;
#             }
#             QListWidget {
#                 background-color: #ffffff;
#                 border: 2px solid #b2ebf2;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#             QLabel {
#                 font-size: 16px;
#                 font-weight: bold;
#                 color: #00796b;
#             }
#         """)

#         self.layout = QVBoxLayout(self)

#         self.label = QLabel("📋 Danh sách LDPlayer đang chạy:")
#         self.layout.addWidget(self.label)

#         self.list_ld = QListWidget()
#         self.layout.addWidget(self.list_ld)

#         self.btn_group = QHBoxLayout()
#         self.btn_refresh = QPushButton("🔄 Quét lại")
#         self.btn_start = QPushButton("▶️ Chạy bot")
#         self.btn_stop = QPushButton("⛔ Dừng bot")
#         self.btn_group.addWidget(self.btn_refresh)
#         self.btn_group.addWidget(self.btn_start)
#         self.btn_group.addWidget(self.btn_stop)
#         self.layout.addLayout(self.btn_group)

#         line = QFrame()
#         line.setFrameShape(QFrame.HLine)
#         line.setFrameShadow(QFrame.Sunken)
#         self.layout.addWidget(line)

#         self.btn_group_all = QHBoxLayout()
#         self.btn_start_all = QPushButton("▶️ Chạy tất cả bot")
#         self.btn_stop_all = QPushButton("🛑 Dừng tất cả bot")
#         self.btn_group_all.addWidget(self.btn_start_all)
#         self.btn_group_all.addWidget(self.btn_stop_all)
#         self.layout.addLayout(self.btn_group_all)

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QFrame, QListWidgetItem, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QFont, QColor, QPainter, QBrush, QPixmap
from PyQt5.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QEasingCurve
import random

class Particle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.particles = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(50)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def add_particle(self):
        p = {
            "pos": QPoint(random.randint(0, self.width()), 0),
            "vel": QPoint(random.randint(-1, 1), random.randint(1, 3)),
            "radius": random.randint(2, 4),
            "color": QColor(0, 191, 255, 100)
        }
        self.particles.append(p)

    def update_particles(self):
        if len(self.particles) < 40:
            self.add_particle()
        for p in self.particles:
            p["pos"] += p["vel"]
        self.particles = [p for p in self.particles if p["pos"].y() < self.height()]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for p in self.particles:
            painter.setBrush(QBrush(p["color"]))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(p["pos"], p["radius"], p["radius"])

class LightDot(QWidget):
    def __init__(self, parent=None, top_left=True):
        super().__init__(parent)
        self.radius = 6
        self.pos_x = 0
        self.top_left = top_left
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)
        self.setFixedSize(100, 40)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setStyleSheet("background: transparent;")

    def animate(self):
        self.pos_x = (self.pos_x + 3) % self.width()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        color = QColor(0, 191, 255, 120)
        painter.setBrush(QBrush(color))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPoint(self.pos_x, 20), self.radius, self.radius)

class BackgroundImage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap("assets/bg_blur.png")  # Đường dẫn tới ảnh nền mờ
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.5)  # Điều chỉnh độ mờ tại đây
        painter.drawPixmap(self.rect(), self.pixmap)

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌿 Auto Farm Manager")
        self.setGeometry(300, 200, 550, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #e0f7fa;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QPushButton {
                background-color: #4dd0e1;
                border: none;
                border-radius: 12px;
                padding: 10px 16px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00acc1;
            }
            QPushButton:pressed {
                background-color: #007c91;
            }
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #b2ebf2;
                border-radius: 10px;
                padding: 8px;
            }
            QLabel.title {
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                background-color: #b2ebf2;
                border-radius: 10px;
                color: #004d40;
            }
        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bg_image = BackgroundImage(self)
        self.bg_image.resize(self.width(), self.height())
        self.bg_image.show()

        self.particle_effect = Particle(self)
        self.particle_effect.resize(self.width(), self.height())
        self.particle_effect.show()

        self.light_top_left = LightDot(self)
        self.light_top_left.move(10, 10)
        self.light_top_left.show()

        self.light_top_right = LightDot(self)
        self.light_top_right.move(self.width() - 110, 10)
        self.light_top_right.show()

        self.label = QLabel("📋 Danh sách LDPlayer đang chạy:")
        self.label.setObjectName("title")
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setStyleSheet("QLabel#title { qproperty-alignment: AlignCenter; }")
        self.label.setProperty("class", "title")
        self.layout.addWidget(self.label)

        self.list_ld = QListWidget()
        self.layout.addWidget(self.list_ld)

        self.btn_group = QHBoxLayout()
        self.btn_refresh = QPushButton("🔄 Quét lại")
        self.btn_start = QPushButton("▶️ Chạy bot")
        self.btn_stop = QPushButton("⛔ Dừng bot")

        self._add_shadow(self.btn_refresh)
        self._add_shadow(self.btn_start)
        self._add_shadow(self.btn_stop)

        self.btn_group.addWidget(self.btn_refresh)
        self.btn_group.addWidget(self.btn_start)
        self.btn_group.addWidget(self.btn_stop)
        self.layout.addLayout(self.btn_group)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line)

        self.btn_group_all = QHBoxLayout()
        self.btn_start_all = QPushButton("▶️ Chạy tất cả bot")
        self.btn_stop_all = QPushButton("🛑 Dừng tất cả bot")

        self._add_shadow(self.btn_start_all)
        self._add_shadow(self.btn_stop_all)

        self.btn_group_all.addWidget(self.btn_start_all)
        self.btn_group_all.addWidget(self.btn_stop_all)
        self.layout.addLayout(self.btn_group_all)

        # self.status_label = QLabel("Farm")
        # self.status_label.setAlignment(Qt.AlignCenter)
        # self.status_label.setStyleSheet("""
        #     QLabel {
        #         color: #00796b;
        #         font-style: italic;
        #         padding: 15px;
        #     }
        # """)
        # self.layout.addWidget(self.status_label)

    def resizeEvent(self, event):
        self.light_top_right.move(self.width() - 110, 10)
        self.particle_effect.resize(self.width(), self.height())
        self.bg_image.resize(self.width(), self.height())
        super().resizeEvent(event)

    def _add_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2, 2)
        widget.setGraphicsEffect(shadow)

    def update_status(self, message: str, level: str = "info"):
        colors = {
            "info": "#00796b",
            "warning": "#f57c00",
            "error": "#d32f2f"
        }
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"color: {colors.get(level, '#00796b')}; font-style: italic; padding-top: 10px;")

    def add_ld_item(self, ld_name, status):
        item = QListWidgetItem(f"{ld_name} - {status}")
        if status == "Running":
            item.setBackground(QColor("#C8E6C9"))
        elif status == "Idle":
            item.setBackground(QColor("#FFF9C4"))
        elif status == "Error":
            item.setBackground(QColor("#FFCDD2"))
        self.list_ld.addItem(item)

