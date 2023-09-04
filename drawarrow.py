import cv2
import numpy as np

# Load the chessboard image
chessboard_image = cv2.imread('captured_screenshot.png')

# Define the chessboard square size and color for drawing the arrow
square_size = chessboard_image.shape[0] // 8  # Assuming an 8x8 chessboard
arrow_color = (0, 0, 255)  # Red color

# Parse the move string (e.g., "g1g3")
from_square, to_square = "g1", "g3"

# Calculate the pixel coordinates for the 'from' and 'to' squares
from_col, from_row = ord(from_square[0]) - ord('a'), int(from_square[1]) - 1
to_col, to_row = ord(to_square[0]) - ord('a'), int(to_square[1]) - 1
from_x = from_col * square_size + square_size // 2
from_y = from_row * square_size + square_size // 2
to_x = to_col * square_size + square_size // 2
to_y = to_row * square_size + square_size // 2

# Draw the arrow on the image
arrow_thickness = 2
chessboard_with_arrow = chessboard_image.copy()
cv2.arrowedLine(chessboard_with_arrow, (from_x, from_y), (to_x, to_y), arrow_color, arrow_thickness)

# Save or display the resulting image
cv2.imwrite('chessboard_with_arrow.jpg', chessboard_with_arrow)
cv2.imshow('Chessboard with Arrow', chessboard_with_arrow)
cv2.waitKey(0)
cv2.destroyAllWindows()
