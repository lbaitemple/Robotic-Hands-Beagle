import rcpy
import time
import rcpy.servo as servo
import rcpy.clock as clock
import getopt, sys
import random

x = random.randint(1,3)
print(x)

def rock():
        servo.enable()
        print('rock')

        srvo1 = servo.Servo(2)
        clck = clock.Clock(srvo1, 0.01)
        clck.start()
        srvo1.set(1.5)

        srvo2 = servo.Servo(4)
        clck = clock.Clock(srvo2, 0.01)
        clck.start()
        srvo2.set(1.5)

        srvo3 = servo.Servo(6)
        clck = clock.Clock(srvo3, 0.01)
        clck.start()
        srvo3.set(-1.5)

        srvo4 = servo.Servo(8)
        clck = clock.Clock(srvo4, 0.01)
        clck.start()
        srvo4.set(-1.5)

        srvo5 = servo.Servo(1)
        clck = clock.Clock(srvo5, 0.01)
        clck.start()
        srvo5.set(1.0)

        time.sleep(0.5)

        servo.disable()
        return

def paper():

        servo.enable()
        print('paper')

        srvo1 = servo.Servo(2)
        clck = clock.Clock(srvo1, 0.01)
        clck.start()
        srvo1.set(-1.5)

        srvo2 = servo.Servo(4)
        clck = clock.Clock(srvo2, 0.01)
        clck.start()
        srvo2.set(-1.5)

        srvo3 = servo.Servo(6)
        clck = clock.Clock(srvo3, 0.01)
        clck.start()
        srvo3.set(1.5)

        srvo4 = servo.Servo(8)
        clck = clock.Clock(srvo4, 0.01)
        clck.start()
        srvo4.set(1.5)

        srvo5 = servo.Servo(1)
        clck = clock.Clock(srvo5, 0.01)
        clck.start()
        srvo5.set(1.4)

        time.sleep(0.5)

        servo.disable()
        return

def scissors():

        servo.enable()
        print('scissors')

        srvo1 = servo.Servo(2)
        clck = clock.Clock(srvo1, 0.01)
        clck.start()
        srvo1.set(1.5)

        srvo2 = servo.Servo(4)
        clck = clock.Clock(srvo2, 0.01)
        clck.start()
        srvo2.set(-1.5)

        srvo3 = servo.Servo(6)
        clck = clock.Clock(srvo3, 0.01)
        clck.start()
        srvo3.set(1.5)

        srvo4 = servo.Servo(8)
        clck = clock.Clock(srvo4, 0.01)
        clck.start()
        srvo4.set(-1.5)

        srvo5 = servo.Servo(1)
        clck = clock.Clock(srvo5, 0.01)
        clck.start()
        srvo5.set(0.2)
        print('scissors')

        time.sleep(0.5)

        servo.disable()
        return

if(x == 1):

        rock()

elif(x == 2):

        paper()

else:

        scissors()

