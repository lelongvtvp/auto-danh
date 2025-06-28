# detectors/health_bar_checker.py

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from config.settings import HEALTH_BAR_REGION
from detectors.screenshot import capture_screen

def is_fighting(debug=False):
    image = capture_screen()
    if image is None:
        return False

    x, y, w, h = HEALTH_BAR_REGION
    roi = image[y:y+h, x:x+w]  # Cắt vùng thanh máu quái

    # Tiền xử lý ảnh cho dễ OCR
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

    # OCR
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    if debug:
        print("[OCR] Text phát hiện:", text)
        cv2.imshow("ROI", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Kiểm tra có đoạn chữ liên quan đến quái không
    keywords = ["Kazekage", "tam", "Exp", "13500"]
    for keyword in keywords:
        if keyword in text:
            return True
    return False
