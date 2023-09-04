from PIL import ImageGrab

def capture_screenshot(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        # Calculate the bounding box from the given coordinates
        left = min(x1, x2, x3, x4)
        top = min(y1, y2, y3, y4)
        right = max(x1, x2, x3, x4)
        bottom = max(y1, y2, y3, y4)

        # Capture the screenshot using the bounding box
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

        # Save the screenshot as an image file
        screenshot.save("captured_screenshot.png")
        print("Screenshot saved as 'captured_screenshot.png'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace these coordinates with the actual coordinates of the corners
    x1, y1 = 320, 175
    x2, y2 = 1070, 175
    x3, y3 = 320, 925
    x4, y4 = 1070, 925
    
    capture_screenshot(x1, y1, x2, y2, x3, y3, x4, y4)
