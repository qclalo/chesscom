import cv2
import numpy as np
import pyautogui
from board_to_fen.predict import get_fen_from_image

# Capture a screenshot of the screen
screenshot = pyautogui.screenshot()

# Convert the screenshot to a NumPy array (OpenCV format)
screenshot_np = np.array(screenshot)

# Convert the BGR image to RGB
screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

# Use OpenCV to find the chessboard pattern in the screenshot
# Define the number of rows and columns in the chessboard
rows = 8
cols = 8

# Find the chessboard corners in the screenshot
ret, corners = cv2.findChessboardCorners(screenshot_rgb, (rows, cols), None)

# If the chessboard is found, draw the corners and display the image
if ret:
    # Draw the corners on the image
    cv2.drawChessboardCorners(screenshot_rgb, (rows, cols), corners, ret)
    
    # Display the image with corners
    cv2.imshow('Chessboard', screenshot_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Chessboard not found in the screenshot.")
