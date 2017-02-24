#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import yaml
import os
 
# Read configuration
with open("MotionDetector.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
gpio_pin = os.getenv('GPIO_PIN', cfg['gpio']['pin'])
mqtt_host = os.getenv('MQTT_HOST', cfg['mqtt']['host'])
mqtt_port = os.getenv('MQTT_PORT', cfg['mqtt']['port'])
mqtt_topic = os.getenv('MQTT_TOPIC', cfg['mqtt']['topic'])
mqtt_message = os.getenv('MQTT_MESSAGE', cfg['mqtt']['message'])

# Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN)

# Init MQTT
client = mqtt.Client()
client.connect(mqtt_host, mqtt_port, 60)
client.loop_start()

# Detect motion
def motion_detected(channel):
    print('Es gab eine Bewegung!')
    client.publish(mqtt_topic, mqtt_message)

# Detection loop
try:
    GPIO.add_event_detect(gpio_pin, GPIO.RISING, callback=motion_detected)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print "Beende..."
GPIO.cleanup()
