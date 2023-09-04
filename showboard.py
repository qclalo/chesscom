import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to your image file
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_image(image_path):
    # Load and display the image
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')  # Turn off axis labels and ticks
    plt.show()

if __name__ == "__main__":
    # Path to your image file
    image_path = "path_to_your_image.jpg"
    display_image(image_path)
