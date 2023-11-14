import RPi.GPIO as GPIO
import time

buzzerPin = 16
melody = [262, 330, 392, 523]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setwarnings(False)

class Buzzer:
    def __init__(self):
        self.pin = 16
        self.pwm = GPIO.PWM(buzzerPin, 1.0)

    def Welcome(self):
        self.pwm.start(50.0)
        for i in range(4):
            self.pwm.ChangeFrequency(melody[i])
            time.sleep(1.0)
        self.pwm.stop()

    def Emergency(self):
        self.pwm.start(50.0)
        for i in range(5):
            self.pwm.ChangeFrequency(349)
            time.sleep(2.0)
        self.pwm.stop()

GPIO.cleanup()