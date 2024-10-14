import os
from datetime import datetime
from tkinter import Tk, filedialog
from PIL import Image

def save_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Resize the image while maintaining aspect ratio
        img.thumbnail(size, Image.LANCZOS)

        # Save the image in JPG format with compression
        img.save(output_path, "JPEG", quality=80)

# Initialize Tkinter root
root = Tk()
root.withdraw()  # Hide the root window
root.attributes('-topmost', True)  # Bring window to front
root.lift()  # Lift the window above others
root.focus_force()  # Focus on the window

# Open file dialog to select image file
file_path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
)

root.destroy()  # Close the Tkinter root window

# Get the directory of the input image file
input_directory = os.path.dirname(file_path)

# Get the current date in the required format
current_date = datetime.now().strftime("%d.%m.%Y")

# Output file names
output_filename_1 = f"{current_date}_1080.jpg"
output_filename_2 = f"{current_date}_720.jpg"

# Construct the full file paths for the output images in the same directory as the input file
output_path_1 = os.path.join(input_directory, output_filename_1)
output_path_2 = os.path.join(input_directory, output_filename_2)

# Save the images with the specified sizes
save_image(file_path, output_path_1, size=(1920, 1080))
save_image(file_path, output_path_2, size=(1280, 720))

print(f"Saved images to:\n{output_path_1}\n{output_path_2}")

