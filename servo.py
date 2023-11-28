import RPi.GPIO as GPIO
import time

servoPin = 16
melody = [262, 330, 392, 525]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

class Servo:
    def __init__(self):
        self.pin = servoPin
        self.servo = GPIO.PWM(servoPin, 50)

    def setAngle(self, angle):
        duty = 2.5 + 10 * angle / 180
        self.servo.ChangeDutyCycle(duty)
        GPIO.cleanup()

    def control_servo(self, angle):
        if angle is not None:
            self.setAngle(int(angle))
        GPIO.cleanup()