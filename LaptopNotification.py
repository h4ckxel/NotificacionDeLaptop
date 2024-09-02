# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:37:30 2024

@author: h4ckxel
"""

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10
            )
        time.sleep(3600)
        
#https://github.com/h4ckxel

