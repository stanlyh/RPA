from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Manejar versiones de Chrome: python -m pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui as robot
import pyperclip
import time

# Variables

name = 'Celeste Kat'
number = '123987000'
age = '5'