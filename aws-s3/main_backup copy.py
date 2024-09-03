from PIL import Image

input_image_path = "./idol.jpg"
output_image_path = "./resized_idol.jpg"

def resize_image(input_path, output_path, size = (300, 300)):
    with Image.open(input_path) as img:
        img_resized = img.resize(size)
        img_resized.save(output_path)

resize_image(input_image_path, output_image_path)