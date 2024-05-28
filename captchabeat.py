import pyautogui
import time

def find_and_click_color(color_hex, pixel_coordinates):
    for x, y in pixel_coordinates:
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        print(f"Checking pixel at ({x}, {y}) - Color: {pixel_color}")
        if pixel_color == color_hex:
            print("Color found!")
            pyautogui.click(x, y)
            return True
    return False

color_hex = (124, 134, 104)  # (7c8668) in RGB
pixel_coordinates = [(740, 430), (800, 430), (850, 430), (910, 430), 
                     (960, 430), (1015, 430), (1070, 430), (1120, 430), (1180, 430)]

while True:
    if find_and_click_color(color_hex, pixel_coordinates):
        print("Color found and clicked!")
    else:
        print("Color not found on the screen.")
    # time.sleep(1)  # Wait for 1 second before searching again


# Ways to improve this code:
# 1. Scan only a single pixel for either the red or green values
# 2. If it's green, then click it
# 3. Otherwise, scan the remaining 9 pixels for green or red and click the green one as soon as it is found
