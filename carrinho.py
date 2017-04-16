import pygame
from pygame.locals import *
import sys
import time
import RPi.GPIO as GPIO
from goto import goto, comefrom, label


# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()


# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24


StepLeftPinForward=16
StepLeftPinBackward=18


StepRightPinForward=15
StepRightPinBackward=11


LightPinFront=22
LightPinBack=13


sleeptime=0.1
light=0


GPIO.setmode(GPIO.BOARD)


GPIO.setup(StepLeftPinForward, GPIO.OUT)
GPIO.setup(StepLeftPinBackward, GPIO.OUT)
GPIO.setup(StepRightPinForward, GPIO.OUT)
GPIO.setup(StepRightPinBackward, GPIO.OUT)
GPIO.setup(LightPinFront, GPIO.OUT)
GPIO.setup(LightPinBack, GPIO.OUT)




def resetGpio():
    GPIO.output(StepLeftPinForward, GPIO.LOW)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)
    GPIO.output(StepRightPinForward, GPIO.LOW)
    GPIO.output(StepRightPinBackward, GPIO.LOW)
    GPIO.output(LightPinFront, GPIO.LOW)
    GPIO.output(LightPinBack, GPIO.LOW)


def forward():
    GPIO.output(StepLeftPinForward, GPIO.HIGH)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)
    GPIO.output(StepRightPinForward, GPIO.HIGH)
    GPIO.output(StepRightPinBackward, GPIO.LOW)


def backward():
    GPIO.output(StepLeftPinBackward, GPIO.HIGH)
    GPIO.output(StepLeftPinForward, GPIO.LOW)
    GPIO.output(StepRightPinBackward, GPIO.HIGH)
    GPIO.output(StepRightPinForward, GPIO.LOW)
    GPIO.output(LightPinBack, GPIO.HIGH)
    print "backwarding"


def spinRight():
    GPIO.output(StepLeftPinForward, GPIO.HIGH)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)
    GPIO.output(StepRightPinBackward, GPIO.HIGH)
    GPIO.output(StepRightPinForward, GPIO.LOW)


def spinLeft():
    GPIO.output(StepRightPinForward, GPIO.HIGH)
    GPIO.output(StepRightPinBackward, GPIO.LOW)
    GPIO.output(StepLeftPinBackward, GPIO.HIGH)
    GPIO.output(StepLeftPinForward, GPIO.LOW)


def stop():
    print "stop"
    GPIO.output(StepRightPinForward, GPIO.LOW)
    GPIO.output(StepRightPinBackward, GPIO.LOW)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)
    GPIO.output(StepLeftPinForward, GPIO.LOW)
    GPIO.output(LightPinBack, GPIO.LOW)


def lightFront():
    global light
    if light == 0:
        GPIO.output(LightPinFront, GPIO.HIGH)
        light=1
    else:
        GPIO.output(LightPinFront, GPIO.LOW)
        light=0


resetGpio()












pygame.init()


title = "Hello!"
width = 100
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption(title)


pygame.key.set_repeat(100, 100)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print 'go forward'
		forward()
            if event.key == pygame.K_DOWN:
                print 'go backward'
		backward()
            if event.key == pygame.K_LEFT:
                print 'go left'
		spinLeft()
            if event.key == pygame.K_RIGHT:
                print 'go right'
		spinRight()	
            if event.key == pygame.K_a:
                print 'lights'
		lightFront()
            if event.key == pygame.K_q:
                print 'quit'
		goto .end
        if event.type == pygame.KEYUP:
            stop()            
            print 'stop'


label .end
resetGpio()
GPIO.cleanup()