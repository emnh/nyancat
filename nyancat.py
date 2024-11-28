#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re


import os
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Define the Nyan Cat and Rainbow frames
NYAN_CAT = r"""
   ／l、
（ﾟ､ ｡ ７
   l、 ~ヽ
   じしf_,)ノ
"""

RAINBOW = [
    f"{Back.RED}   ",
    f"{Back.YELLOW}   ",
    f"{Back.GREEN}   ",
    f"{Back.BLUE}   ",
    f"{Back.MAGENTA}   ",
]

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_nyan_cat():
    """Animates Nyan Cat with a rainbow trail."""
    trail_length = 10
    rainbow_index = 0
    position = 0

    try:
        while True:
            clear_console()

            # Create a moving rainbow trail
            trail = "".join(RAINBOW[(rainbow_index + i) % len(RAINBOW)] for i in range(trail_length))
            rainbow_index = (rainbow_index + 1) % len(RAINBOW)

            # Print the trail and Nyan Cat
            print(trail + NYAN_CAT.replace("\n", f"\n{' ' * len(trail)}"))

            # Simulate movement
            position += 1
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nNyan cat animation stopped!")

animate_nyan_cat()
