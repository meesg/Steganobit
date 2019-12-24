# Steganobit

Two really simple python scripts to encrypt and decrypt data into images, by
translating a text file into ascii, translating the ascii into binary, using
every pixel as a binary value container and adding an offset to the pixels
which store a 1.

By configuring the script to use a high offset you make it possible to decrypt
messages based on only the result, by just use of eyesight and educated guesses
of which pixels should be 0's and which should be 1's. By configuring the script
to use a low offset, but still using an image where the original color isn't
obtainable (for example a totally black image), the image is decryptable with
some basic tools (color picker, another python script, etc). By configuring the
script to use a low offset and using some random picture, using some advanced
AI trained on the same type of pictures and iterating over different
possibilities it might still be possible to retrieve the message encrypted in
the image. Only by using random noise as an original image, you are certain
the original image is needed to be able to decrypt the message in the output
image.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Settings](#usage)
- [License](#license)

## Background

This project is a result of wanting to hide a little easter egg in icon of my
personal website (which is still under construction by the time of writing).
The name is simply a concatenation of steganograpy and bitmap, because at first
I was only planning to support bitmaps (but the pillow library is awesome).


## Install

1. Download and install [Python 3.6+](https://www.python.org/downloads/).
2. Install the [pillow library](https://github.com/python-pillow/Pillow/).
3. Clone this repository.

## Usage

1. Configure the settings.json to your liking.
2. Run encrypt.py to encrypt
3. (OPTIONAL) Run decrypt.py to decrypt messages in the obtained
output.

## Settings
`data`: The path to the txt file of the message to be encrypted.  
`inputImage`: The path to the input image.  
`outputImage`: The path to the output image.  
`offset`: The RGB offset for each pixel which stores a 1 (negative values are
	allowed).  
`overflow`: Allow overflow for RGB values. If true and the new R value is 256,
it will become 0, vice versa.  

## License

[MIT](LICENSE)
