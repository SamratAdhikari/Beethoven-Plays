import pyautogui
import time
import keyboard
import random
import win32api, win32con



def print_mouse_coordinates():
    while True:
#     # Wait for the 's' key to be pressed
        if keyboard.is_pressed('s'):
            x, y = pyautogui.position()
            print(f'Mouse coordinates: ({x}, {y})')
            # Adding a short delay to avoid multiple prints on a single key press
            keyboard.wait('s', suppress=False)
        
        # Break the loop and exit if 'q' is pressed
        if keyboard.is_pressed('q'):
            break
    
    

(x1, y1) = (523, 466)
(x2, y2) = (632, 465)
(x3, y3) = (728, 466)
(x4, y4) = (817, 468)
    

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def main():
    while keyboard.is_pressed('q') == False:
        
        if pyautogui.pixel(x1, y1)[0] == 0:
            click(x1, y1)
        if pyautogui.pixel(x2, y2)[0] == 0:
            click(x2, y2)
        if pyautogui.pixel(x3, y3)[0] == 0:
            click(x3, y3)
        if pyautogui.pixel(x4, y4)[0] == 0:
            click(x4, y4)
        
        
if __name__ == '__main__':
    # print_mouse_coordinates()
    main()