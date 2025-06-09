# pi-NAS-Meter (c. 2020)
![vlkd9bO](https://github.com/user-attachments/assets/680efa4e-fba7-4526-ad42-e2cb0cdefccf)

A simple I2C LCD Raspberry Pi display for NAS statistics

This was designed for a 20 character x 4 line I2C LCD. You can easily modify it to fit another LCD, but you will likely be hard pressed for space.

Prerequisites:

-Create a directory for each SMB share to be mounted against

-Enable I2C on the Pi via **sudo raspi-config**

-Install i2c-tools, Python, Python-pip, and Python-smbus via **sudo apt-get install i2c-tools python python-pip python-smbus**

-A momentary button wired between GND and GPIO 21 to serve as a graceful shutdown option when needed

-LCD can be wired to the I2C bus of the Pi, details can be found here: http://wiki.sunfounder.cc/index.php?title=I2C_LCD2004

-Need to run "sudo python NAS_METER.py" on boot, via crontab. Add "@reboot sudo python /home/pi/NAS_METER.py" to the end. I do this via **sudo crontab -e** and leveraging Nano.

-Need the I2CBUS defined per the Pi version (line 19 of I2C_LCD_driver.py)

-Need the LCD I2C address defined (line 23 of I2C_LCD_driver.py; this can be found by running the commmand "i2cdetect -y 1" (where 1 is the I2CBUS number))

-----------------------------------------------------------------------------

The crux of this little project is to have a simple display to place on your desk, in your computer chassis, or in some manner of rackmounted form factor that will cycle through your network shares and show usage statistics. I should note that this project makes use of hardcoded credentials in plaintext: this is generally a TERRIBLE ideal and should be avoided. My mitigation measures were in using a service account whose access was limited on the NAS itself, such that if the password were compromised it could only be used, inside the firewall, to traverse a directory structure but NOT to read any files.

The I2C LCD driver was sourced from this page: https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

