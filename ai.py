from pathlib import Path
from openai import OpenAI
from time import time
import csv
import os
from dotenv import load_dotenv

load_dotenv()

SZO="""Test"""
start_time = time()

client = OpenAI(api_key=os.getenv("OPENAPIKEY"))

speech_file_path = Path(__file__).parent / f"speech{len(SZO)}.mp3"
with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input=SZO,
) as response:
    response.stream_to_file(speech_file_path)

end_time = time()
elapsed_time = end_time - start_time

with open('data.csv', 'a', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([SZO,len(SZO),elapsed_time])

print("A kód futási ideje:", elapsed_time, "másodperc")
