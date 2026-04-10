from PIL import Image


def jpeg_to_png(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGB")
        img.save(output_path, "PNG")
        return True, output_path
    except Exception as e:
        return False, str(e)


def png_to_jpeg(input_path, output_path, quality=95):
    try:
        img = Image.open(input_path).convert("RGB")
        img.save(output_path, "JPEG", quality=quality)
        return True, output_path
    except Exception as e:
        return False, str(e)


def load_preview(image_path, max_size=(200, 200)):
    try:
        img = Image.open(image_path)
        img.thumbnail(max_size)
        return True, img
    except Exception as e:
        return False, str(e)