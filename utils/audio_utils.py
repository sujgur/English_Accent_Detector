import os
import requests
import imageio_ffmpeg

# Ensure moviepy can find ffmpeg on Streamlit Cloud
os.environ["IMAGEIO_FFMPEG_EXE"] = imageio_ffmpeg.get_ffmpeg_exe()

from moviepy.editor import VideoFileClip

def download_video(url, output_path="input_video.mp4"):
    r = requests.get(url, stream=True)
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    return output_path

def extract_audio(video_path, audio_path="audio.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, codec="pcm_s16le")
    clip.close()
    return audio_path
