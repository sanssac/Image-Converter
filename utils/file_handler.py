from tkinter import filedialog


def choose_file():
    return filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )


def choose_save_location(default_ext):
    return filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )