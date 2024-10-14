import os
from datetime import datetime
from tkinter import Tk, filedialog
from PIL import Image

def select_image_file():
    # Initialize Tkinter root
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select image file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    root.destroy()  # Close the Tkinter root window
    return file_path

def save_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Resize the image while maintaining aspect ratio
        img.thumbnail(size, Image.ANTIALIAS)
        
        # Save the image in JPG format with compression
        img.save(output_path, "JPEG", quality=85)

def main():
    file_path = select_image_file()
    if not file_path:
        print("No file selected.")
        return

    # Get the current date in the required format
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Output file names
    output_filename_1080 = f"{current_date}_1080.jpg"
    output_filename_720 = f"{current_date}_720.jpg"

    # Define output sizes
    size_1080 = (1920, 1080)
    size_720 = (1280, 720)

    # Save the images with the specified sizes
    save_image(file_path, output_filename_1080, size=(1920, 1080))
    save_image(file_path, output_filename_720, size=(1280, 720))

    print(f"Saved images: {output_filename_1080} and {output_filename_720}")

if name == "main":
    main()
