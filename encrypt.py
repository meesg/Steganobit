import math
import json

from PIL import Image

with open('settings.json') as json_file:
    settings = json.load(json_file)

im = Image.open(settings["inputImage"])
width, height = im.size
totalPixels = width * height

offset = (settings["offset"][0], settings["offset"][1], settings["offset"][2])

f = open(settings["data"], "r")
data = f.read()

if len(data) > totalPixels / 8:
    raise Exception('Given image is not big enough to fit the text')

for i, c in enumerate(data):
    charCode = ord(c)
    for j in range(8):
        pixelNumber = i * 8 + j
        x = pixelNumber % width
        y = math.floor(pixelNumber / width)

        shift = 7 - j
        if (charCode >> shift) % 2 != 0:
            pixelData = im.getpixel((x, y))
            newPixelData = list(map(sum, zip(pixelData, offset)))
            if settings["overflow"]:
                for k in range(3):
                    if newPixelData[k] > 255: newPixelData[k] -= 255
                    if newPixelData[k] < 0: newPixelData[k] += 255

            im.putpixel((x, y), tuple(newPixelData))

im.save(settings["outputImage"])
