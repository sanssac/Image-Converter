from PIL import Image
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.converter import jpeg_to_png, png_to_jpeg


def create_test_image(path, format="RGB"):
    """Creates a simple test image."""
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    img.save(path)


def test_jpeg_to_png():
    """Test JPEG to PNG conversion creates output file."""
    create_test_image("tests/test_input.jpg")
    success, result = jpeg_to_png("tests/test_input.jpg", "tests/test_output.png")
    assert success is True
    assert os.path.exists("tests/test_output.png")
    os.remove("tests/test_input.jpg")
    os.remove("tests/test_output.png")


def test_png_to_jpeg():
    """Test PNG to JPEG conversion creates output file."""
    create_test_image("tests/test_input.png")
    success, result = png_to_jpeg("tests/test_input.png", "tests/test_output.jpg")
    assert success is True
    assert os.path.exists("tests/test_output.jpg")
    os.remove("tests/test_input.png")
    os.remove("tests/test_output.jpg")


def test_invalid_file():
    """Test that converter handles a bad file path gracefully."""
    success, result = jpeg_to_png("fake_file.jpg", "output.png")
    assert success is False