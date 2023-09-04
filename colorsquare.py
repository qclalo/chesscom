from PIL import Image, ImageDraw

# Open the chessboard image
chessboard_image = Image.open("captured_screenshot.png")  # Replace with your image path

# Define the size of a square and the coordinates of the square to outline
square_size = chessboard_image.width // 8  # Assuming an 8x8 chessboard
top_left = (square_size * 3, square_size * 4)  # Example: Coordinates of the e5 square
bottom_right = (square_size * 4, square_size * 5)

# Create a drawing object
draw = ImageDraw.Draw(chessboard_image)

# Define the outline color (green)
outline_color = (0, 255, 0, 255)  # RGBA color (R, G, B, A)

# Draw a green outline (border) around the specified square
draw.rectangle([top_left, bottom_right], outline=outline_color, width=3)

# Save or display the modified image
chessboard_image.save("outlined_chessboard.png")  # Save the modified image
chessboard_image.show()  # Display the modified image

# Close the image when you're done
chessboard_image.close()
