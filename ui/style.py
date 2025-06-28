
# from PyQt5.QtWidgets import (
#     QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
#     QLabel, QListWidget, QFrame, QListWidgetItem, QGraphicsDropShadowEffect
# )
# from PyQt5.QtGui import QFont, QColor, QPainter, QBrush, QPixmap
# from PyQt5.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QEasingCurve
# import random

# class Particle(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.particles = []
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_particles)
#         self.timer.start(50)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#     def add_particle(self):
#         p = {
#             "pos": QPoint(random.randint(0, self.width()), 0),
#             "vel": QPoint(random.randint(-1, 1), random.randint(1, 3)),
#             "radius": random.randint(2, 4),
#             "color": QColor(0, 191, 255, 100)
#         }
#         self.particles.append(p)

#     def update_particles(self):
#         if len(self.particles) < 40:
#             self.add_particle()
#         for p in self.particles:
#             p["pos"] += p["vel"]
#         self.particles = [p for p in self.particles if p["pos"].y() < self.height()]
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         for p in self.particles:
#             painter.setBrush(QBrush(p["color"]))
#             painter.setPen(Qt.NoPen)
#             painter.drawEllipse(p["pos"], p["radius"], p["radius"])

# class LightDot(QWidget):
#     def __init__(self, parent=None, top_left=True):
#         super().__init__(parent)
#         self.radius = 6
#         self.pos_x = 0
#         self.top_left = top_left
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.animate)
#         self.timer.start(50)
#         self.setFixedSize(100, 40)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)
#         self.setStyleSheet("background: transparent;")

#     def animate(self):
#         self.pos_x = (self.pos_x + 3) % self.width()
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         color = QColor(0, 191, 255, 120)
#         painter.setBrush(QBrush(color))
#         painter.setPen(Qt.NoPen)
#         painter.drawEllipse(QPoint(self.pos_x, 20), self.radius, self.radius)

# class BackgroundImage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.pixmap = QPixmap("assets/bg_blur.png")  # Đường dẫn tới ảnh nền mờ
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setOpacity(0.5)  # Điều chỉnh độ mờ tại đây
#         painter.drawPixmap(self.rect(), self.pixmap)

# class Ui_MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("🌿 Auto Farm Manager")
#         self.setGeometry(300, 200, 550, 500)
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #e0f7fa;
#                 font-family: 'Segoe UI';
#                 font-size: 14px;
#             }
#             QPushButton {
#                 background-color: #4dd0e1;
#                 border: none;
#                 border-radius: 12px;
#                 padding: 10px 16px;
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
#                 border-radius: 10px;
#                 padding: 8px;
#             }
#             QLabel.title {
#                 font-size: 18px;
#                 font-weight: bold;
#                 padding: 10px;
#                 background-color: #b2ebf2;
#                 border-radius: 10px;
#                 color: #004d40;
#             }
#         """)

#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

#         self.bg_image = BackgroundImage(self)
#         self.bg_image.resize(self.width(), self.height())
#         self.bg_image.show()

#         self.particle_effect = Particle(self)
#         self.particle_effect.resize(self.width(), self.height())
#         self.particle_effect.show()

#         self.light_top_left = LightDot(self)
#         self.light_top_left.move(10, 10)
#         self.light_top_left.show()

#         self.light_top_right = LightDot(self)
#         self.light_top_right.move(self.width() - 110, 10)
#         self.light_top_right.show()

#         self.label = QLabel("📋 Danh sách LDPlayer đang chạy:")
#         self.label.setObjectName("title")
#         self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
#         self.label.setStyleSheet("QLabel#title { qproperty-alignment: AlignCenter; }")
#         self.label.setProperty("class", "title")
#         self.layout.addWidget(self.label)

#         self.list_ld = QListWidget()
#         self.layout.addWidget(self.list_ld)

#         self.btn_group = QHBoxLayout()
#         self.btn_refresh = QPushButton("🔄 Quét lại")
#         self.btn_start = QPushButton("▶️ Chạy bot")
#         self.btn_stop = QPushButton("⛔ Dừng bot")

#         self._add_shadow(self.btn_refresh)
#         self._add_shadow(self.btn_start)
#         self._add_shadow(self.btn_stop)

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

#         self._add_shadow(self.btn_start_all)
#         self._add_shadow(self.btn_stop_all)

#         self.btn_group_all.addWidget(self.btn_start_all)
#         self.btn_group_all.addWidget(self.btn_stop_all)
#         self.layout.addLayout(self.btn_group_all)

#         self.status_label = QLabel("Farm")
#         self.status_label.setAlignment(Qt.AlignCenter)
#         self.status_label.setStyleSheet("""
#             QLabel {
#                 color: #00796b;
#                 font-style: italic;
#                 padding: 15px;
#             }
#         """)
#         self.layout.addWidget(self.status_label)

#     def resizeEvent(self, event):
#         self.light_top_right.move(self.width() - 110, 10)
#         self.particle_effect.resize(self.width(), self.height())
#         self.bg_image.resize(self.width(), self.height())
#         super().resizeEvent(event)

#     def _add_shadow(self, widget):
#         shadow = QGraphicsDropShadowEffect()
#         shadow.setBlurRadius(10)
#         shadow.setOffset(2, 2)
#         widget.setGraphicsEffect(shadow)

#     def update_status(self, message: str, level: str = "info"):
#         colors = {
#             "info": "#00796b",
#             "warning": "#f57c00",
#             "error": "#d32f2f"
#         }
#         self.status_label.setText(message)
#         self.status_label.setStyleSheet(f"color: {colors.get(level, '#00796b')}; font-style: italic; padding-top: 10px;")

#     def add_ld_item(self, ld_name, status):
#         item = QListWidgetItem(f"{ld_name} - {status}")
#         if status == "Running":
#             item.setBackground(QColor("#C8E6C9"))
#         elif status == "Idle":
#             item.setBackground(QColor("#FFF9C4"))
#         elif status == "Error":
#             item.setBackground(QColor("#FFCDD2"))
#         self.list_ld.addItem(item)

import json, os, random
from pathlib import Path
from PyQt5.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QVariantAnimation
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QCheckBox, QGraphicsOpacityEffect, QFrame,
    QListWidget, QListWidgetItem, QGraphicsBlurEffect, QHBoxLayout
)

# ---------- cấu hình theme / settings ----------
CONFIG_DIR = Path("config"); CONFIG_DIR.mkdir(exist_ok=True)
THEME_PATH   = CONFIG_DIR / "theme.json"
SETTINGS_PATH = CONFIG_DIR / "settings.json"

_DEFAULT_THEME = {
    "theme": "light", "primary": "#4dd0e1",
    "background": "#e0f7fa", "accent": "#00796b",
    "error": "#d32f2f", "warning": "#f57c00"
}
_DEFAULT_SETTINGS = {
    "particle": True, "season_effect": "none",  # "snow" | "leaf" | "none"
    "blur": True
}

def _ensure(path: Path, default: dict):
    if not path.exists(): path.write_text(json.dumps(default, indent=2), "utf-8")
    try: return json.loads(path.read_text("utf-8"))
    except Exception: return default

def load_theme()    : return _ensure(THEME_PATH, _DEFAULT_THEME)
def load_settings() : return _ensure(SETTINGS_PATH, _DEFAULT_SETTINGS)

def build_qss(t):
    return f"""
    QWidget {{
        background: {t['background']}; font-family: 'Segoe UI'; font-size:14px;
    }}
    QPushButton {{
        background:{t['primary']}; color:#fff; border:none; border-radius:12px;
        padding:8px 14px; font-weight:600;
    }}
    QPushButton:hover {{ background:{t['accent']}; }}
    QListWidget {{
        background:#fff; border:2px solid {t['primary']}40; border-radius:10px; padding:6px;
    }}
    QLabel.title {{ font-size:20px; font-weight:bold; color:{t['accent']}; }}
    """

# ---------- hiệu ứng hạt/ mùa ----------
class Particle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent); self.p = []; self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.t = QTimer(self); self.t.timeout.connect(self.tick); self.t.start(60)
    def add_p(self):
        self.p.append({"pos": QPoint(random.randint(0,self.width()),0),
                       "vel": QPoint(random.randint(-1,1), random.randint(1,3)),
                       "r": random.randint(2,4),
                       "c": QColor(0,191,255,100)})
    def tick(self):
        if len(self.p)<35: self.add_p()
        for x in self.p: x["pos"] += x["vel"]
        self.p=[x for x in self.p if x["pos"].y()<self.height()]; self.update()
    def paintEvent(self,_):
        qp=QPainter(self); qp.setRenderHint(QPainter.Antialiasing)
        for x in self.p:
            qp.setBrush(QBrush(x["c"])); qp.setPen(Qt.NoPen)
            qp.drawEllipse(x["pos"], x["r"], x["r"])

class SeasonEffect(Particle):
    def __init__(self, img, parent=None):
        super().__init__(parent); self.pix=QPixmap(img)
    def add_p(self):
        size=random.randint(14,22)
        self.p.append({"pos": QPoint(random.randint(0,self.width()),0),
                       "vel": QPoint(random.randint(-1,1), random.randint(1,2)),
                       "pix": self.pix.scaled(size,size,Qt.KeepAspectRatio,Qt.SmoothTransformation)})
    def paintEvent(self,_):
        qp=QPainter(self)
        for x in self.p:
            qp.drawPixmap(x["pos"], x["pix"])

# ---------- toast, switch, blur‑list ----------
class Toast(QWidget):
    """
    Floating toast (sub‑window) – icon + text – tự mờ dần.
    * Không chặn chuột (nút bên dưới vẫn nhận mouse‑release).
    * Hoạt động với PyQt5.
    """

    _CFG = {
        "info":    {"bg": "#00796b", "emoji": "✅"},
        "warning": {"bg": "#f57c00", "emoji": "⚠️"},
        "error":   {"bg": "#d32f2f", "emoji": "⛔"},
    }

    def __init__(
        self,
        parent: QWidget,
        text: str,
        level: str = "info",
        timeout: int = 3000,
        margin: int = 12,
    ):
        super().__init__(parent)

        cfg = self._CFG.get(level, self._CFG["info"])

        # ---- window flags & attributes ----
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.SubWindow               # toạ độ local theo parent
            | Qt.WindowStaysOnTopHint    # luôn nổi trong cửa sổ cha
        )
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)

        # ---- style ----
        self.setStyleSheet(
            f"""
            QWidget {{
                background: {cfg['bg']};
                border-radius: 8px;
            }}
            QLabel {{
                color: white;
                font-weight: 500;
            }}
            """
        )

        # ---- layout ----
        lay = QHBoxLayout(self)
        lay.setContentsMargins(12, 6, 12, 6)
        lay.setSpacing(8)

        icon = QLabel(cfg["emoji"], self)
        icon.setFixedWidth(18)
        icon.setAlignment(Qt.AlignCenter)

        msg = QLabel(text, self)
        msg.setWordWrap(False)  # toast ngắn gọn

        lay.addWidget(icon)
        lay.addWidget(msg)

        # ---- position (local to parent) ----
        self.adjustSize()
        x = (parent.width() - self.width()) // 2
        y = parent.height() - self.height() - margin
        self.move(x, y)

        # ---- fade‑in ----
        eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(eff)
        fade = QPropertyAnimation(eff, b"opacity", self)
        fade.setDuration(250)
        fade.setStartValue(0)
        fade.setEndValue(1)
        fade.start()

        self.show()

        # ---- auto‑close ----
        QTimer.singleShot(timeout, self.close)


class ToggleSwitch(QCheckBox):
    def __init__(self,parent=None): super().__init__(parent); self.setCursor(Qt.PointingHandCursor); self.setFixedSize(50,24)
    def paintEvent(self,e):
        qp=QPainter(self); qp.setRenderHint(QPainter.Antialiasing)
        track=QColor("#4dd0e1") if self.isChecked() else QColor("#b0bec5")
        qp.setBrush(track); qp.setPen(Qt.NoPen); qp.drawRoundedRect(0,0,50,24,12,12)
        qp.setBrush(Qt.white); qp.drawEllipse(26 if self.isChecked() else 2,2,20,20)

class FrostListWidget(QListWidget):
    def __init__(self, blur=True, parent=None):
        super().__init__(parent)
        if blur: blurEff=QGraphicsBlurEffect(); blurEff.setBlurRadius(10); self.setGraphicsEffect(blurEff)
        self.setStyleSheet("background:rgba(255,255,255,0.35);")

# ---------- Animation helpers ----------
def animate_item_bg(item,start,end,dur=400):
    an=QVariantAnimation(item.listWidget()); an.setDuration(dur); an.setStartValue(start); an.setEndValue(end)
    an.valueChanged.connect(lambda c: item.setBackground(c))
    an.start(QVariantAnimation.DeleteWhenStopped)

def fade_in(label,text):
    if not hasattr(label,"eff"): label.eff=QGraphicsOpacityEffect(); label.setGraphicsEffect(label.eff)
    anim=QPropertyAnimation(label.eff,b"opacity",label); anim.setDuration(350); anim.setStartValue(0); anim.setEndValue(1)
    label.setText(text); anim.start()
