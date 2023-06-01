import convertImages
import convertVideos
from time import time

print('\n Made with ♥ by LeBeaufort \n \n \n')
print('Type "help" for more information')
while True:
    choice = input('>')

    if 'help' in choice:
        print("""
        ---Help---
        help:                       give information about commands
        exit:                       close the application
        convertImageToAscii :       convert an image to asciiArt (file text). Usage : convertImageToAscii <path of the image> <name of the output text file:optional>
        convertTextToImage :        convert an asciiArt file text to an black and white image. Usage : convertTextToImage <path of the text file> <name of the output image:optional>
        convertImageToAsciiImage:   create an image with ascii art. Usage : convertImageToAsciiImage <path of the image> <name of output:optional> <charsize:optional>
        convertVideo :              create an ascii art video. Usage : convertVideo <path of the image> <name of output:optional> <charsize:optional>
        """)
    elif choice == 'exit':
        exit()

    elif choice.lower().startswith('convertimagetoascii'):
        start = time()

        if len(choice.split()) == 3:
            convertImages.toAscii(choice.split()[1], choice.split()[2])
        elif len(choice.split()) == 2:
            convertImages.toAscii(choice.split()[1])
        else:
            print('Incorrects settings, type "help" for more info')
        print(f'Runned in {time() - start}s')

    elif choice.lower().startswith('converttexttoimage'):
        start = time()
        if len(choice.split()) == 3:
            convertImages.toImage(choice.split()[1], choice.split()[2])
        elif len(choice.split()) == 2:
            convertImages.toImage(choice.split()[1])
        else:
            print('Incorrects settings, type "help" for more info')
        print(f'Runned in {time() - start}s')

    elif choice.lower().startswith('convertimagetoasciiimage'):
        start = time()
        if len(choice.split()) == 4:
            convertImages.toAsciiImage(choice.split()[1], choice.split()[2], choice.split()[3])
        elif len(choice.split()) == 3:
            convertImages.toAsciiImage(choice.split()[1], choice.split()[2])
        elif len(choice.split()) == 2:
            convertImages.toAsciiImage(choice.split()[1])
        else:
            print('Incorrects settings, type "help" for more info')
        print(f'Runned in {time() - start}s')

    elif choice.lower().startswith('convertvideo'):
        start = time()
        if len(choice.split()) == 4:
            convertVideos.main(choice.split()[1], choice.split()[2], choice.split()[3])
        elif len(choice.split()) == 3:
            convertVideos.main(choice.split()[1], choice.split()[2])
        elif len(choice.split()) == 2:
            convertVideos.main(choice.split()[1])
        else:
            print('Incorrects settings, type "help" for more info')
        print(f'Runned in {time() - start}s')

    else:
        print('Unknow command ! type "help" for more information')

    start = 0
