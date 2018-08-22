
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


def random_char():
    return chr(random.randint(65, 90))


def random_color():
    return random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)


def random_color2():
    return random.randint(32, 100), random.randint(32, 100), random.randint(32, 100)

width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(random_color()))

font = ImageFont.truetype('Arial.ttf', 36)

for t in range(4):
    draw.text((10+60*t, 10), random_char(), font=font, fill=(random_color2()))

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'JPEG')
