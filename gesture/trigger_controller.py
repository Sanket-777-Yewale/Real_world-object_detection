from config.settings import settings

class TriggerController:
    def __init__(self):
        self.triggered = False

    def check_trigger(self, finger_count):
        if finger_count == settings.GESTURE_REQUIRED_FINGERS:
            self.triggered = True
        else:
            self.triggered = False

        return self.triggered