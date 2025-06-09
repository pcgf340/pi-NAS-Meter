# -*- coding: utf-8 -*-
import I2C_LCD_driver
from time import *
import RPi.GPIO as GPIO
mylcd = I2C_LCD_driver.lcd()
import os
import commands
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
mylcd.lcd_clear()
sleep(10)
os.system('sudo mount.cifs //10.0.0.18/Data_Archive /home/pi/data_archive -o user=srvNASMeter,password=GenericCredential1863,vers=1.0,ro && sudo mount.cifs //10.0.0.12/Odin /home/pi/odin -o user=srvNASMeter,password=GenericCredential1863,vers=2.0,ro && sudo mount.cifs //10.0.0.55/Pool_0/ /home/pi/ssdnas -o user=Alexander,password=AJF335fa6,vers=2.0,ro && sudo mount.cifs //10.0.0.18/8TB_Ext /home/pi/8tb -o user=srvNASMeter,password=GenericCredential1863,vers=1.0,ro')
while True:
 mylcd.lcd_display_string("Data_Archive"[:20].ljust(20),1)
 mylcd.lcd_display_string(" Size  Used Avail".ljust(20),2)
 mylcd.lcd_display_string("%s" %commands.getoutput("df -H /home/pi/data_archive --output=size,used,avail")[18:].ljust(20),3)
 sleep(5)
 if(GPIO.input(21) ==0):
  mylcd.lcd_clear()
  os.system('sudo umount /home/pi/odin/ && sudo umount /home/pi/data_archive && sudo umount /home/pi/ssdnas && sudo umount /home/pi/8tb')
  mylcd.lcd_display_string("Shutting down...",1)
  mylcd.lcd_display_string("Safe to power down",2)
  mylcd.lcd_display_string("once message clears.",3)
  os.system('sudo shutdown now')
 mylcd.lcd_display_string("Odin"[:20].ljust(20),1)
 mylcd.lcd_display_string(" Size  Used Avail".ljust(20),2)
 mylcd.lcd_display_string("%s" %commands.getoutput("df -H /home/pi/odin --output=size,used,avail")[18:].ljust(20),3)
 sleep(5)
 if(GPIO.input(21) ==0):
  mylcd.lcd_clear()
  os.system('sudo umount /home/pi/odin/ && sudo umount /home/pi/data_archive && sudo umount /home/pi/ssdnas && sudo umount /home/pi/8tb')
  mylcd.lcd_display_string("Shutting down...",1)
  mylcd.lcd_display_string("Safe to power down",2)
  mylcd.lcd_display_string("once message clears.",3)
  os.system('sudo shutdown now')
 mylcd.lcd_display_string("SSDNAS"[:20].ljust(20),1)
 mylcd.lcd_display_string(" Size  Used Avail".ljust(20),2)
 mylcd.lcd_display_string("%s" %commands.getoutput("df -H /home/pi/ssdnas --output=size,used,avail")[18:].ljust(20),3)
 sleep(5)
 if(GPIO.input(21) ==0):
  mylcd.lcd_clear()
  os.system('sudo umount /home/pi/odin/ && sudo umount /home/pi/data_archive && sudo umount /home/pi/ssdnas && sudo umount /home/pi/8tb')
  mylcd.lcd_display_string("Shutting down...",1)
  mylcd.lcd_display_string("Safe to power down",2)
  mylcd.lcd_display_string("once message clears.",3)
  os.system('sudo shutdown now')
 mylcd.lcd_display_string("8TB_Ext"[:20].ljust(20),1)
 mylcd.lcd_display_string(" Size  Used Avail".ljust(20),2)
 mylcd.lcd_display_string("%s" %commands.getoutput("df -H /home/pi/8tb --output=size,used,avail")[18:].ljust(20),3)
 sleep(5)
 if(GPIO.input(21) ==0):
  mylcd.lcd_clear()
  os.system('sudo umount /home/pi/odin/ && sudo umount /home/pi/data_archive && sudo umount /home/pi/ssdnas && sudo umount /home/pi/8tb')
  mylcd.lcd_display_string("Shutting down...",1)
  mylcd.lcd_display_string("Safe to power down",2)
  mylcd.lcd_display_string("once message clears.",3)
  os.system('sudo shutdown now')