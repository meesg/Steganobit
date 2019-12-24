import math
import json

from PIL import Image

with open('settings.json') as json_file:
    settings = json.load(json_file)

original = Image.open(settings["inputImage"])
encrypted = Image.open(settings["outputImage"])

width, height = original.size
totalPixels = width * height

if original.size != encrypted.size:
    raise Exception('Given images are not the same size!')

data = 'Original data: '
x = 0
y = 0
for i in range(math.floor(totalPixels / 8)):
    charCode = 0

    for j in range(8):
        charCode = charCode << 1
        if original.getpixel((x, y)) != encrypted.getpixel((x, y)):
            charCode += 1
        x += 1
        if x >= width:
            x = 0
            y += 1
    if charCode != 0:
        data += chr(charCode)

print(data)
