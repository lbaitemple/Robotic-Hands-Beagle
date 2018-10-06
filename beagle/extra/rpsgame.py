import rcpy
import time
import rcpy.servo as servo
import rcpy.clock as clock
import getopt, sys
import json
import random
import argparse

parser = argparse.ArgumentParser(description='RCPY for robotic hand')
parser.add_argument('-i', '--input', type=str, required = True)
args = parser.parse_args()

filename = args.input
with open(filename, 'r') as f:
    data = json.load(f)
print(data)

datalen = len(data['poses']) - 1
srvo = [0 for i in range(6)]
print(srvo)

def close():

    for i in range(0, 6):
        servo.enable()
        print(i, data['poses'][i]['position']['x'])
        srvo[i] = servo.Servo(data['poses'][i]['position']['x'])
        clck = clock.Clock(srvo[i], data['poses'][i]['position']['y'])
        clck.start()
        srvo[i].set(data['poses'][i]['position']['z'])

    srvo[4].set(data['poses'][10]['position']['z'])
    time.sleep(0.5)
    print('close')
    return

def close1():

    for i in range(0, 6):
        srvo[i].set(data['poses'][i]['position']['z'])

    srvo[4].set(data['poses'][10]['position']['z'])
    print('close')
    time.sleep(0.5)
    return

def open():

    for i in range(6, 12):
        srvo[i-6].set(data['poses'][i]['position']['z'])

    srvo[4].set(data['poses'][4]['position']['z'])
    print('open')
    time.sleep(0.5)
    return

def random_one():

    print('random one')
    randone = random.randint(1, 3)

    if randone == 1:
        rock()
    elif randone == 2:
        paper()
    else:
        scissors()

    srvo[4].set(data['poses'][10]['position']['z'])
    srvo[4].set(data['poses'][4]['position']['z'])
    time.sleep(0.4)
    return

def rock():

    for i in range(0, 4):
        srvo[i].set(data['poses'][i]['position']['z'])

    srvo[5].set(data['poses'][5]['position']['z'])
    print('rock')
    time.sleep(0.2)
    return

def paper():

    for i in range(6, 10):
        srvo[i-6].set(data['poses'][i]['position']['z'])

    srvo[5].set(data['poses'][11]['position']['z'])
    print('paper')
    time.sleep(0.2)
    return

def scissors():

    for i in range(12, 16):
        srvo[i-12].set(data['poses'][i]['position']['z'])

    srvo[5].set(data['poses'][16]['position']['z'])
    print('scissors')
    time.sleep(0.2)
    return

print('start')
close()
open()
close1()
open()
close1()
open()
close1()

print('final:')
randno = random.randint(1, 3)

print(randno)

if randno == 1:
    rock()
elif randno == 2:
    paper()
else:
    scissors()

srvo[4].set(data['poses'][10]['position']['z'])
srvo[4].set(data['poses'][4]['position']['z'])
time.sleep(1)
servo.disable()
