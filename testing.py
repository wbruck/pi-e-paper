#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
font_dir = '/home/pi/soft/e-Paper/RaspberryPi_JetsonNano/python'
picdir = os.path.join(font_dir, 'pic')
libdir = os.path.join(font_dir, 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

from gpiozero import Button
from signal import pause

logging.basicConfig(level=logging.DEBUG)

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

def print_to_display(msg):
    logging.info("epd2in7 Demo")   
    epd = epd2in7.EPD()
    
    '''2Gray(Black and white) display'''
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the fra>
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'this is some text', font = font24, fill = 0)
    draw.text((10, 30), str(msg), font = font24, fill = 0)
    epd.display(epd.getbuffer(Himage))

   # except IOError as e:  
   #  logging.info(e)
   # 
   # except KeyboardInterrupt:    
   #     logging.info("ctrl + c:")
   #     epd2in7.epdconfig.module_exit()
   #     exit()

#epd2in7.epdconfig.module_exit()
#exit()

def handle_btn_press(btn):
    pin_num = btn.pin.number

    msg = pin_num
    if pin_num == 19:
        logging.warning("remove image in 3 sec")
        logging.info("Clear...")
        logging.info("Clear...")
        epd = epd2in7.EPD()
        epd.Clear(0xFF)
        logging.info("Goto Sleep...")
        epd.sleep()
    else:
        print_to_display(msg)


btn1.when_pressed = handle_btn_press
btn2.when_pressed = handle_btn_press
btn3.when_pressed = handle_btn_press
btn4.when_pressed = handle_btn_press

pause()
