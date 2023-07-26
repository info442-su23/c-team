from big_chungus import split_text_into_chunks
from agents import label, summarize, table_of_contents
from utils.file_converters import *
from utils.speech_2_text import *
import asyncio

def main():
    with open('../transcripts/text.txt', 'r') as file:
        text = file.read()
        file.close()
        chunks = split_text_into_chunks(text)
        labels = label(chunks)
        print(f"Labels:\n {labels}")
        print(f"Table of contents: f{table_of_contents(labels)}")
        print(f"Summaries: f{summarize(chunks)}")

async def transcription_main():
    print("Running")

    loop = asyncio.get_running_loop()

    #await loop.run_in_executor(None, lambda: extract_audio_from_video("../video", "../audio"))
    await transcribe_directory("../audio", "../transcripts")

    print("Done")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(transcription_main())

    loop.close()