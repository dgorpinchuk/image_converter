import os
from datetime import datetime
import wx
from PIL import Image

def save_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            # Resize the image while maintaining aspect ratio
            img.thumbnail(size, Image.Resampling.LANCZOS)

            # Save the image in JPG format with compression
            img.save(output_path, "JPEG", quality=80)

    except Exception as e:
        print(f"Failed to process the image: {e}")

class MyApp(wx.App):
    def OnInit(self):
        # Create a wx FileDialog for image file selection
        dialog = wx.FileDialog(
            None, message="Choose an image file",
            wildcard="Image files (*.jpg;*.jpeg;*.png;*.bmp;*.gif)|*.jpg;*.jpeg;*.png;*.bmp;*.gif",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )

        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            self.process_image(file_path)
        else:
            print("No file selected.")

        dialog.Destroy()  # Clean up the dialog
        return False  # Exit the app after the dialog

    def process_image(self, file_path):
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

if __name__ == "__main__":
    # Initialize and run the wx App
    app = MyApp(False)
    app.MainLoop()
