import json
import time
import requests
import mbotclient
import os

bot = mbotclient.mBot()

if input('Have nothing plugged in right now! Continue? y/n') == 'y':
    print(os.system('/dev/ls tty*'))
if input('Plug in the mBot now! Continue? y/n') == 'y':
    print(os.system('/dev/ls tty*'))

bot.startWithSerial(input("Enter Serial Port that has not been in the first console log: "))

while True:
    response = json.loads(requests.get('192.168.46.89:4444').text)
    print(response['left'], response['right'], response['delay'])
    bot.doMove(response['left'], response['right'])
    time.sleep(response['delay'])
