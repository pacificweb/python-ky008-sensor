#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import logging
import time
from datetime import datetime
from gpiozero import LED

log = logging.getLogger(__name__)

def main(args=None):

    _filename=datetime.now().strftime('%Y%m%d.log')
    logging.basicConfig(filename=_filename,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s;%(message)s',level=logging.DEBUG)


    laser = LED(20)
    #laser.on()
    laser.blink()

    try:
        while True:
            #laser.toggle()
            time.sleep(1)
    except (KeyboardInterrupt):
        laser.off()
    finally:
        sys.exit()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
