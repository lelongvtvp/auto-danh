# detectors/stuck_detector.py

class MovementTracker:
    """
    Theo dõi số lần không tìm thấy quái để suy đoán bị kẹt mép bản đồ.
    """
    def __init__(self, threshold=5):
        self.counter = 0
        self.threshold = threshold

    def reset(self):
        self.counter = 0

    def increase(self):
        self.counter += 1

    def is_stuck(self):
        return self.counter >= self.threshold
