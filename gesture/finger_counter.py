class FingerCounter:
    TIP_IDS = [4, 8, 12, 16, 20]

    def count_fingers(self, hand_landmarks):
        fingers = 0

        # Thumb
        if hand_landmarks.landmark[self.TIP_IDS[0]].x < hand_landmarks.landmark[self.TIP_IDS[0] - 1].x:
            fingers += 1

        # Other 4 fingers
        for id in range(1, 5):
            if hand_landmarks.landmark[self.TIP_IDS[id]].y < hand_landmarks.landmark[self.TIP_IDS[id] - 2].y:
                fingers += 1

        return fingers