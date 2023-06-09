from pydub import AudioSegment
import os

folder_path = '20'
audio_files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]

combined_audio = AudioSegment.empty()

for file in audio_files:
    audio = AudioSegment.from_file(os.path.join(folder_path, file))
    combined_audio += audio

combined_audio.export('AI_siwon_Test2.wav', format='wav')
