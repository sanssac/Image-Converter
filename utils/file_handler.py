from tkinter import filedialog
def choose_file():
    return filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
