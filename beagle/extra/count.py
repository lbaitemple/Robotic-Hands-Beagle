import rcpy
import time
import rcpy.servo as servo
import rcpy.clock as clock
import getopt, sys

def count():

        print('one')
        servo.enable()

        srvo1 = servo.Servo(2)
        clck = clock.Clock(srvo1, 0.01)
        clck.start()
        srvo1.set(1)

        srvo2 = servo.Servo(4)
        clck = clock.Clock(srvo2, 0.01)
        clck.start()
        srvo2.set(1)

        srvo3 = servo.Servo(6)
        clck = clock.Clock(srvo3, 0.01)
        clck.start()
        srvo3.set(1.5)

        srvo4 = servo.Servo(8)
        clck = clock.Clock(srvo4, 0.01)
        clck.start()
        srvo4.set(-1)

        srvo5 = servo.Servo(1)
        clck = clock.Clock(srvo5, 0.018)
        clck.start()
        srvo5.set(0.7)

        time.sleep(2)

        print('two')

        srvo1.set(1.5)
        srvo2.set(-1.5)
        srvo3.set(1.5)
        srvo4.set(-1.5)
        srvo5.set(0.7)

        time.sleep(2);

        print('three')

        srvo1.set(-1.5)
        srvo2.set(-1.5)
        srvo3.set(-1.5)
        srvo4.set(-1.5)
        srvo5.set(0.7)

        time.sleep(2)

        print('four')

        srvo1.set(-1.5)
        srvo2.set(-1.5)
        srvo3.set(1.5)
        srvo4.set(-1.5)
        srvo5.set(0.7)

        time.sleep(2)

        print('five')

        srvo1.set(-1.5)
        srvo2.set(-1.5)
        srvo3.set(1.5)
        srvo4.set(1.5)
        srvo5.set(1)

        time.sleep(1000)

        servo.disable()
        return

count()

