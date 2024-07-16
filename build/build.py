import json
import time
import os
import subprocess

import os


appdata_path = os.getenv('APPDATA')
directory_path = os.path.join(appdata_path, 'AutoCry', 'AutoTreoBSN')
list_id_path = os.path.join(directory_path, 'id_list.txt')
list_password_path = os.path.join(directory_path, 'password.txt')
config_path = os.path.join(directory_path, 'config.txt')

with open(list_id_path, "r") as id_read:
    id_list = [line.strip() for line in id_read]
    print(id_list)
with open(list_password_path, "r") as password_read:
    password_list = [line.strip() for line in password_read]
    print(password_list)
with open(config_path, "r") as config_read:
    config = [line.strip() for line in config_read]
    print(config)

istart = int(config[0])
os.system('powershell.exe taskkill /f /im phidoi.atm')
os.system('powershell.exe taskkill /f /im launcher.atm')

while True:

    doubleClick("1678028639493.png")
    sleep(15)
    doubleClick(Pattern("1713041355001.png").targetOffset(95,281))
    
    type(id_list[istart])
    sleep(1)
    doubleClick(Pattern("1713041422090.png").targetOffset(93,295))
    sleep(1)
    type(password_list[istart])
    sleep(1)
    type(Key.ENTER)
    sleep(1)
    while True:
        try:
            wait("1718326827374.png",60)
            break
        except:
            doubleClick(Pattern("1713041355001.png").targetOffset(95,281))
    
            type(id_list[istart])
            sleep(1)
            doubleClick(Pattern("1713041422090.png").targetOffset(90,303))
            sleep(1)
            print(password_list[istart],"asdfsaf")
            type(password_list[istart])
            sleep(1)
            type(Key.ENTER)
            sleep(1)
    sleep(1)
    click(Pattern("1677172226775-1.png").targetOffset(-81,7))
    wait("1683220127017.png",30)

    sleep(3600)
        
    os.system('powershell.exe taskkill /f /im phidoi.atm')
    os.system('powershell.exe taskkill /f /im launcher.atm')
    istart = istart + 1