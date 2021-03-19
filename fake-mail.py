#!/usr/bin/env python

#imports
import os
import sys
import time
from os import system
from time import sleep

try:
    import requests
except ImportError:
    os.system('pip install requests')

try:
    request = requests.get("https://www.google.com", timeout=3)
except (requests.ConnectionError, request.Timeout) as exception:
    print("[!] No Internet Connection [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
