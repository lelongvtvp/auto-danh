# # detectors/health_bar_checker.py

# import cv2
# import pytesseract
# import os
# from config.settings import HEALTH_BAR_REGION
# from detectors.screenshot import capture_screen

# # Đảm bảo đường dẫn đến tesseract đã đúng
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def is_fighting(ld_name, debug=False):
#     print(f"[{ld_name}] ➤ Kiểm tra trạng thái đánh quái...")

#     image = capture_screen(ld_name)
#     if image is None:
#         print(f"[{ld_name}] ❌ Không lấy được ảnh màn hình.")
#         return False

#     try:
#         x, y, w, h = HEALTH_BAR_REGION
#         roi = image[y:y+h, x:x+w]

#         # Resize giảm nhiễu, nhẹ hơn cho OCR
#         roi = cv2.resize(roi, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
#         gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#         _, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

#         # OCR an toàn có bắt lỗi
#         custom_config = r'--oem 3 --psm 6'
#         try:
#             text = pytesseract.image_to_string(thresh, config=custom_config, timeout=3)
#         except RuntimeError as e:
#             print(f"[{ld_name}] ❗ OCR timeout hoặc lỗi: {e}")
#             return False

#         if debug:
#             print(f"[{ld_name}] 🧠 OCR Text phát hiện:\n{text}")
#             cv2.imshow("Thanh máu (OCR)", thresh)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()

#         # Từ khóa xuất hiện trong thanh máu quái
#         keywords = ["Kazekage", "tam", "Exp", "13500", "exp", "Quái", "Phong", "Thổ", "Hỏa", "Lôi", "Thủy"]
#         for keyword in keywords:
#             if keyword in text:
#                 print(f"[{ld_name}] ✅ Phát hiện quái (qua từ khóa: {keyword})")
#                 return True

#         print(f"[{ld_name}] ❌ Không thấy quái.")
#         return False

#     except Exception as e:
#         print(f"[{ld_name}] ❗ LỖI khi xử lý ảnh/OCR: {e}")
#         return False
# detectors/health_bar_checker.py

import cv2
import pytesseract
from config.settings import HEALTH_BAR_REGION
from detectors.screenshot import capture_screen

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def is_fighting(ld_name, debug=False):
    image = capture_screen(ld_name)
    if image is None:
        return False

    x, y, w, h = HEALTH_BAR_REGION
    roi = image[y:y+h, x:x+w]

    # Chuyển sang grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Áp threshold đơn giản
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    if debug:
        cv2.imshow("Ảnh Sau Threshold", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    text = pytesseract.image_to_string(thresh, config='--oem 3 --psm 6')

    if debug:
        print(f"[{ld_name}] 🧠 OCR Text phát hiện:\n{text}")

    keywords = ["Exp","+","Lv" "/", "0", "000", "00"]
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return True

    return False

