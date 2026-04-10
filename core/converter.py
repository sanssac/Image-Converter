from PIL import Image
from tkinter import filedialog
def choose_save_location(default_ext):
    return filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )


def jpeg_to_png(input_path):
    img = Image.open(input_path).convert("RGB")

    output_path = choose_save_location(".png")
    if not output_path:
        status_label.configure(text="❌ Save cancelled")
        return

    img.save(output_path, "PNG")
    status_label.configure(text=f"✅ Saved: {output_path}")

def png_to_jpeg(input_path):
    img = Image.open(input_path).convert("RGB")

    output_path = choose_save_location(".jpg")
    if not output_path:
        status_label.configure(text="❌ Save cancelled")
        return

    img.save(output_path, "JPEG")
    status_label.configure(text=f"✅ Saved: {output_path}")