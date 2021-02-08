import sys
import os
from PIL import Image

input_folder = f'./{sys.argv[1]}'
output_folder = f'./{sys.argv[2]}'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for img in os.listdir(input_folder):
    img_name = img.replace('.jpg', '')
    opened_img = Image.open(f'./{input_folder}/{img}')
    converter_img = opened_img.save(f'{output_folder}/{img_name}.png', 'png')
