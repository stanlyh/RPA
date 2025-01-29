import pyautogui
import time

### Evaluate current position ####

# x,y = pyautogui.position()
# print(x)
# print(y)
# print(pyautogui.position())


### Live mouse position ###

# pyautogui.displayMousePosition()


### Move mouse position ###

# x,y = 1500,200
# pyautogui.moveTo(x,y)
# 
# p_start = x-500,y+300
# pyautogui.moveTo(p_start,duration=2)


### Clicks ####

# pyautogui.click()
# pyautogui.click(380,200)
# 
# pyautogui.click(1806,10,clicks=2)
# pyautogui.doubleClick(1806,10)


### DragTo ###

# time.sleep(3)
# pyautogui.moveTo(1389,11)
# time.sleep(2)
# pyautogui.dragTo(1500,200,0.75, button='left')

### Scroll ###

# pyautogui.scroll(1800)
# pyautogui.scroll(-1500)# 