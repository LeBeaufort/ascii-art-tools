from PIL import Image, ImageDraw
from os import _exists

def toAscii(ImagePath, textFilePath='output.txt'):
    if not _exists(ImagePath):
        print(f'[ConvertToAscii] file {ImagePath} not found')
        return
    print('[ConvertToAscii] starting...')
    char = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    output = str()
    image = Image.open(ImagePath)
    for y in range(image.height):
        for x in range(image.width):
            output += char[sum(image.getpixel((x,y)))//3 * 9 //255]
        output += '\n'

    print('[ConvertToAscii] conversion...   Done')
    print(f'[ConvertToAscii] writing in {textFilePath}...')
    with open(textFilePath, 'w') as f:
        f.write(output)
    print('[ConvertToAscii] writing...   Done')



def toAsciiImage(ImagePath, outputName='output.png', charsize=10, info=True):
    if not _exists(ImagePath):
        print(f'[ConvertToAscii] file {ImagePath} not found')
        return
    if info:
        print('[ConvertToAscii(Image)] starting...')
    char = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    text = str()
    index = 0
    image = Image.open(ImagePath)
    for y in range(image.height):
        for x in range(image.width):
            text += char[sum(image.getpixel((x, y))) // 3 * 9 // 255]
    if info:
        print('[ConvertToAscii(Image)] conversion...   Done')
        print('[ConvertToAscii(Image)] starting to draw the image...   ')
    img = Image.new("RGB", (image.width * charsize, image.height * charsize), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for y in range(image.height):
        for x in range(image.width):
            pos = x * charsize, y * charsize
            draw.text(pos, text[index], fill=(0,0,0))
            index += 1

    if info:
        print('[ConvertToAscii(Image)] drawing image...   Done')
        print('[ConvertToAscii(Image)] saving...   ')
    img.save(outputName)
    if info:
        print('[ConvertToAscii(Image)] saving...    Done')




def toImage(textFilePath, output='output.png'):
    if not _exists(textFilePath):
        print(f'[ConvertToAscii] file {textFilePath} not found')
        return
    print('[ConvertToImage] starting...')
    equivalents = {' ': 25, '.': 50, ':': 75, '-': 100, '=': 125, '+': 150, '*': 175, '#': 200, '%': 225, '@': 250}
    index = 0
    content = open(textFilePath, 'r').read()
    yLen = len(content.split('\n')) - 1
    xLen = len(content.split('\n')[0])
    img = Image.new("RGB", (xLen, yLen))
    for y in range(yLen):

        for x in range(xLen):
            if content[index] != '\n':
                color =  equivalents[content[index]]
                img.putpixel((x, y), (color, color, color))
            index += 1

        index += 1
    print('[ConvertToImage] conversion...   Done')
    print(f'[ConvertToImage] writing in {output}...')
    img.save(output)
    print('[ConvertToImage] writing...   Done')
