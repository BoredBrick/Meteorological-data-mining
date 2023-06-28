import os

from PIL import Image

max_size = 1 * 1024 * 1024  # 1 megabyte


def compress_image(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=95)


def decompress_image(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path)


def compress_until_smaller_than_one_mb(input_path, output_path, quality=75):
    image = Image.open(input_path)
    while os.path.getsize(input_path) > max_size:
        print(os.path.getsize(input_path))
        image.save(output_path, format='JPEG', quality=quality)
        quality -= 5
        if quality < 10:
            break
    return image
