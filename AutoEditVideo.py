from moviepy.editor import *
import glob

SoundToEdit = glob.glob('Sound/*')
VideoToEdit = glob.glob('Sources/*')

audio_clip = AudioFileClip(f'{SoundToEdit[0]}')

count = 1

while True:
    try:
        video_clip = VideoFileClip(VideoToEdit[0])

        final_clip = video_clip.set_audio(audio_clip)

        final_clip = final_clip.set_duration(AudioFileClip(SoundToEdit[0]).duration)

        final_clip.write_videofile(f'Successfully/{count}.mp4')

        count += 1

        VideoToEdit.remove(VideoToEdit[0])
    except:
        print("Все видео успешно отредактированы!")
        exit()
