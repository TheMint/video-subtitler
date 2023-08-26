"""
Usage:
  caption_mp4.py <input>

Options:
  -h --help     Show this help message and exit.

"""
from docopt import docopt
import moviepy.editor as mp
import speech_recognition as sr

OUTPUT_PATH = "output_video_with_captions.mp4"

def get_mp4_with_captions(input_file_path):
    # Extract audio from the video
    output_audio_path = "extracted_audio.wav"
    video = mp.VideoFileClip(input_file_path)
    video.audio.write_audiofile(output_audio_path)

    # Perform Speech-to-Text
    recognizer = sr.Recognizer()
    with sr.AudioFile(output_audio_path) as source:
        audio_text = recognizer.recognize_google(source)
    captions = audio_text

    # Add Captions to Video
    video_with_captions = mp.TextClip(captions, fontsize=20, color="white").set_duration(video.duration)
    final_video = mp.CompositeVideoClip([video.set_audio(None), video_with_captions.set_position(("center", "bottom"))])
    final_video.write_videofile(OUTPUT_PATH, codec="libx264")


def main():
    arguments = docopt(__doc__)
    input_file_path = arguments['<input>']
    composite_video = get_mp4_with_captions(input_file_path)
    output_file = composite_video.write_videofile("output.mp4", codec="libx264")
    print("Created captioned file from {}, new file is called {}".format(input_file_path, OUTPUT_PATH))
        

if __name__ == '__main__':
    main()