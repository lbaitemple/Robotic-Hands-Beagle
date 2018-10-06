import argparse
import rcpy
import time
import rcpy.servo as servo
import rcpy.clock as clock
import getopt, sys
import json

servo.enable()

parser = argparse.ArgumentParser(description='RCPY for robotic hand')
parser.add_argument('-i', '--input', type=str, required=True)
args = parser.parse_args()

filename = args.input
with open(filename, 'r') as f:
        data = json.load(f)

print(len(data['poses']))

#channel = data['poses'][i]['position']['x']
#period = data['poses'][i]['position']['y']
#duty = data['poses'][i]['position']['z']

datalen = len(data['poses']) - 1
srvo = [0 for i in range(4)]
print(srvo)

def rock():
    for i in range(0, 4):
        servo.enable()
        print(data['poses'][i]['position']['x'])
        srvo[i] = servo.Servo(data['poses'][i]['position']['x'])
        clck = clock.Clock(srvo[i], data['poses'][i]['position']['y'])
        print(srvo)
        clck.start()
        srvo[i].set(data['poses'][i]['position']['z'])
    time.sleep(0.5)
    return

def close():
    for i in range(0, 4):
        srvo[i].set(data['poses'][i]['position']['z'])
    time.sleep(0.5)
    return

def paper():
    for i in range(5, 9):
        srvo[i-5].set(data['poses'][i]['position']['z'])
    time.sleep(0.5)
    return

def scissors():
    for i in range(10, 14):
        print(data['poses'][i]['position']['x'])
        srvo[i-10].set(data['poses'][i]['position']['z'])
    time.sleep(0.5)
    return

#close->open->close->open
rock()
print('close')
time.sleep(0.5)
paper()
print('open')
time.sleep(0.5)
close()
print('close')
time.sleep(0.5)
paper()
print('open')
time.sleep(0.5)

#Generate random number
randno = random.randint(1, 3)
print(randno)
if randno == 1:
    close()
    print('rock')
    servo.disable()
elif randno == 2:
    paper()
    print('paper')
    servo.disable()
else:
    scissors()
    print('scissors')
    servo.disable()

