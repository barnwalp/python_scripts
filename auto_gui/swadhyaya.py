import pyautogui, time


# get the size of primary monitor
# screen_width, screen_height = pyautogui.size()

# # get the x, y position of the mouse
# current_mouse_x, current_mouse_y = pyautogui.position()
# print(screen_width, screen_height)
# print(current_mouse_x, current_mouse_y)

# get the x, y value in terminal when mouse position is changed
# pyautogui.displayMousePosition()

# x = 1866, y=1048
# x = 1370, y=930
mouse_x = 1370;
mouse_y = 930;
while True:
    # pyautogui.moveTo(1593, 1037)
    pyautogui.moveTo(mouse_x, mouse_y)
    time.sleep(5)
    pyautogui.click()
