import os
import PyPDF2
from moviepy.editor import *

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)  # Changed to PdfReader

        text = ""

        for page in reader.pages:  # Iterating directly over the pages
            text += page.extract_text()

    return text

def extract_audio_from_video(video_folder, audio_folder):
    print("We made it")
    for file_name in os.listdir(video_folder):
    # Check if the file is a video by checking its extension
    # You can add more video formats to the list if needed
        if file_name.endswith((".mp4", ".mkv", ".avi", ".flv", ".mov", ".wmv")):
            # Build the input video file path
            input_video_file = os.path.join(video_folder, file_name)

            # Create the output audio file name by replacing the video extension with .mp3
            output_audio_file_name = os.path.splitext(file_name)[0] + ".mp3"

            # Build the output audio file path
            output_audio_file = os.path.join(audio_folder, output_audio_file_name)

            # Load the video file
            video = VideoFileClip(input_video_file)

            # Extract audio from the video
            audio = video.audio

            # Save the audio as an .mp3 file
            audio.write_audiofile(output_audio_file)

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Usage example
if __name__ == "__main__":
    pdf_path = '/home/dust_60/repos/lectern/file.pdf'
    output_path = '/home/dust_60/repos/lectern/file.txt'
    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(extracted_text, output_path)
