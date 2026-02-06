import time
import threading
try:
    import winsound
except ImportError:
    winsound = None

class AlertSystem:
    def __init__(self):
        self.last_alert_time = 0
        self.cooldown = 3.0 # seconds between alerts to avoid spam
        self.lock = threading.Lock()

    def trigger_alert(self):
        """
        Triggers a sound alert if not on cooldown.
        """
        with self.lock:
            now = time.time()
            if now - self.last_alert_time > self.cooldown:
                self.last_alert_time = now
                # Run sound in separate thread to not block video loop
                threading.Thread(target=self._play_sound, daemon=True).start()

    def _play_sound(self):
        if winsound:
            # Frequency 2500 Hz, Duration 1000 ms
            winsound.Beep(2500, 1000)
        else:
            print("\a") # Bell character as fallback
