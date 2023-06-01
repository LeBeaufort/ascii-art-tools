import os
from moviepy.editor import *
from moviepy.audio.io.AudioFileClip import AudioFileClip
from convertImages import toAsciiImage
from imageio import imwrite


def createTempDirectory():
    name = 'cache'
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)
    f = open('info.txt', 'w')
    f.write('This is a test folder, if it is not removed at the end of process, tou can removed if')
    return name

def deleteTempDirectory():
    os.chdir('..')
    os.rmdir('cache')

def saveVideoFrames(filepath):
    video = VideoFileClip(f'..\{filepath}')
    frames = video.iter_frames()
    for index, frame in enumerate(frames):
        imwrite(f'imageN{index}.png', frame)

    return index, video

def main(filepath, output='output.mp4', charsize=10):
    if input('[ConvertVideos] This function will write a lot of image on your disk, this could be dangerous for it, type "yes" to continue: ') != 'yes':
        return
    if not os._exists(filepath):
        print(f'[ConvertVideos] file {filepath} not found')
        return
    print('[ConvertVideos] starting...')
    namef = createTempDirectory()
    print('[ConvertVideos] temp directory created...')
    savedVideoFrame = saveVideoFrames(filepath)
    nframes, video = savedVideoFrame[0], savedVideoFrame[1]
    print(f'[ConvertVideos] {nframes} saved in {namef}')
    print(f'[ConvertVideos] converting frames to ascii...')
    for i in range(nframes + 1):
        toAsciiImage(f'imageN{i}.png', f'imageN{i}.png', info=False, charsize=charsize)
    print(f'[ConvertVideos] frames converted !')
    print('[ConvertVideos] creating new video...')
    images = [f"imageN{i}.png" for i in range(nframes)]
    clip = ImageSequenceClip(images, fps=video.fps)
    deleteTempDirectory()
    audio = AudioFileClip(filepath)
    clip = clip.set_audio(audio)
    clip.write_videofile(output)
    print('[ConvertVideos] creating new video... Done')
    print('[ConvertVideos] temp directory deleted')





if __name__ == "__main__":
    os.chdir('test_folder')
    main('testVideo2.mp4')



