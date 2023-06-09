import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# 새로운 폴더 생성
output_folder = 'AI_SIWON'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 음원 파일 경로
audio_path = 'AI_siwon.wav'

# 오디오 파일 로드
audio = AudioSegment.from_wav(audio_path)

# 음원 파일의 공백 부분 삭제
non_silence_audio = AudioSegment.empty()
silences = split_on_silence(audio, min_silence_len=1000, silence_thresh=-60, keep_silence=1000)
for silence_segment in silences:
    non_silence_audio += silence_segment

# ?초 간격으로 음원 파일 자르고 저장
interval = 1000
for i in range(0, len(non_silence_audio) - interval, interval):
    output_path = os.path.join(output_folder, f'AIS_{i // interval}.wav')
    segment = non_silence_audio[i:i + interval]
    
    # 음원 파일 변환 및 저장
    segment = segment.set_frame_rate(44100)  # 44.1kHz로 설정
    segment = segment.set_sample_width(2)  # 16비트로 설정
    segment = segment.set_channels(1)  # 모노채널로 설정
    segment.export(output_path, format='wav')

