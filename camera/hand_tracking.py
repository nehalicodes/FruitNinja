import cv2
import mediapipe as mp
import sys
print(sys.executable)
print(sys.version)
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandTracker:
    def __init__(self, max_num_hands=1, detection_confidence=0.5, tracking_confidence=0.5):
        self.cap = cv2.VideoCapture(0)

        # New Tasks API setup
        base_options = python.BaseOptions(
            model_asset_path='hand_landmarker.task'  # must be in project folder
        )
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_hands=max_num_hands,
            min_hand_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.landmarker = vision.HandLandmarker.create_from_options(options)
        self.fingertip = None

    def update(self):
        """Read a frame, run hand tracking, update fingertip position."""
        success, frame = self.cap.read()
        if not success:
            self.fingertip = None
            return None

        frame = cv2.flip(frame, 1)  # mirror
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to mediapipe Image format
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        results = self.landmarker.detect(mp_image)

        self.fingertip = None
        if results.hand_landmarks:
            hand = results.hand_landmarks[0]
            h, w, _ = frame.shape
            x = int(hand[8].x * w)   # index fingertip
            y = int(hand[8].y * h)
            self.fingertip = (x, y)

        return frame

    def get_fingertip(self):
        return self.fingertip

    def release(self):
        self.cap.release()
        self.landmarker.close()