import pyautogui as robot
import time

time.sleep(4)
robot.write('texto cualquiera')

robot.press('tab')

time.sleep(1)
robot.press('X')
time.sleep(0.25)
robot.press('X')
time.sleep(0.25)
robot.press('0')
time.sleep(0.25)
robot.press('0')
time.sleep(0.25)
robot.press('2')
time.sleep(0.25)
robot.press('0')
time.sleep(0.25)
robot.press('$')
time.sleep(0.25)
robot.press('*')

time.sleep(0.25)
robot.press('tab')

time.sleep(0.25)
robot.press('enter')


### HotKey ###

#robot.hotkey('ctrl','alt','q')  # @
#
#robot.hotkey('alt','tab')
#
#robot.hotkey('ctrl','e')
#
#robot.hotkey('alt','space')
#
#robot.hotkey('win','e')  # abrir explorador de archivos
#
#robot.write('n')

### copiar y pegar ###
#import pyperclip
#
#pyperclip.copy('Hola, cómo te va??')
#robot.hotkey('ctrl','v')