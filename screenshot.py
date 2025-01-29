import pyautogui
import time

### Screenshot ###
#time.sleep(2)
#screen = pyautogui.screenshot()
#screen.show()  # Revisar no funciono pide import pyscreeze

time.sleep(1)
pyautogui.hotkey('win','d')
time.sleep(1)

# screen2 = pyautogui.screenshot('example.png')

# screen3 = pyautogui.screenshot('example2.png', region=(500,500,500,500)) # (x0, y0, ancho, alto)

#initial_position = 8,7
#final_position = 796,991
#region = initial_position[0], initial_position[1], final_position[0] - initial_position[0], final_position[1] - initial_position[1]
#
#screen4 = pyautogui.screenshot('example3.png', region=region)


### Locate On Screen ###

#file = 'capture_example.png'  ##dirección donde esta la imagen
#
#a = pyautogui.locateOnScreen(file)
#
#time_start = time.time()
#time_end = time.time()
#
#while a == None and time_end-time_start <= 5:
#    time_end = time.time()
#    a = pyautogui.locateAllOnScreen(file)
#
#if a != None:
#    print('Imagen encontrada')
#else:
#    print('Imagen No encontrada en el tiempo establecido')


### Locate Center On Screen ###

#file = 'capture_example.png'
#x,y = pyautogui.locateCenterOnScreen(file)
#pyautogui.moveTo(x,y,4)


### Locate Center On Screen ###

#file = 'capture_example.png'

#a = pyautogui.locateAllOnScreen(file, confidence=0.93)
#for position in a:
#    print(position[0],position[1])
