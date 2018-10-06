import rcpy
import time
import rcpy.servo as servo
import rcpy.clock as clock
import getopt, sys

def handshake():

        servo.enable()

        srvo1 = servo.Servo(2)
        clck = clock.Clock(srvo1, 0.01)
        clck.start()
        srvo1.set(-1.2)

        srvo2 = servo.Servo(4)
        clck = clock.Clock(srvo2, 0.01)
        clck.start()
        srvo2.set(-1.2)

        srvo3 = servo.Servo(6)
        clck = clock.Clock(srvo3, 0.01)
        clck.start()
        srvo3.set(1.2)

        srvo4 = servo.Servo(8)
        clck = clock.Clock(srvo4, 0.01)
        clck.start()
        srvo4.set(1.2)

        srvo5 = servo.Servo(1)
        clck = clock.Clock(srvo5, 0.01)
        clck.start()
        srvo5.set(1.2)

        time.sleep(3)

        srvo1.set(-1.5)
        srvo2.set(-1.5)
        srvo3.set(1.5)
        srvo4.set(1.5)
        srvo5.set(1.4)

        time.sleep(0.5)

        servo.disable()
        return

handshake()

