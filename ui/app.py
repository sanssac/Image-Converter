from PIL import Image
from customtkinter import CTkImage
import os
import customtkinter as ctk

from core.converter import jpeg_to_png, png_to_jpeg
from utils.file_handler import choose_file
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
selected_file = None
preview_image = None
def select_file():
    global selected_file, preview_image

    selected_file = choose_file()

    if selected_file:
        status_label.configure(text=f"Selected: {selected_file}")

        # Load + resize preview
        img = Image.open(selected_file)
        img.thumbnail((200, 200))

        w, h = img.size
        preview_image = CTkImage(light_image=img, dark_image=img, size=(w, h))
        preview_label.configure(image=preview_image, text="")
    else:
        status_label.configure(text="❌ No file selected")


def convert_to_png():
    if not selected_file:
        status_label.configure(text="❌ No file selected")
        return

    if os.path.exists(selected_file):
        jpeg_to_png(selected_file)
    else:
        status_label.configure(text="❌ File not found!")


def convert_to_jpeg():
    if not selected_file:
        status_label.configure(text="❌ No file selected")
        return

    if os.path.exists(selected_file):
        png_to_jpeg(selected_file)
    else:
        status_label.configure(text="❌ File not found!")


# 🔹 MAIN GUI
app = ctk.CTk()
app.title("Image Converter")
app.geometry("450x400")

# Title
ctk.CTkLabel(app, text="Image Converter", font=("Arial", 18)).pack(pady=10)

# Buttons
ctk.CTkButton(app, text="Select Image", command=select_file).pack(pady=10)
ctk.CTkButton(app, text="Convert JPEG → PNG", command=convert_to_png).pack(pady=5)
ctk.CTkButton(app, text="Convert PNG → JPEG", command=convert_to_jpeg).pack(pady=5)

# Status
status_label = ctk.CTkLabel(app, text="No file selected", wraplength=400)
status_label.pack(pady=15)

# Preview
preview_label = ctk.CTkLabel(app, text="")
preview_label.pack(pady=10)

app.mainloop()