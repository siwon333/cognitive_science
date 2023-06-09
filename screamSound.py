from selenium import webdriver 
import time
import os
from pytube import YouTube

# path = r"C:\Users\siwon\Desktop\인지과학과제\chromedriver.exe" #그롬 드라이버 위치
# driver = webdriver.Chrome(path)
# driver.get(r"https://www.youtube.com/results?search_query=scream+sound") # 드라이버가 제어할 사이트
# time.sleep(1) #1초 대기 -> 사이트가 다 로딩 되기 전에 뒤에 명령어가 실행되면 X

# links = []
# i=1

# thumbnails = driver.find_elements_by_id('thumbnail')
# href_list = [thumbnail.get_attribute('href') for thumbnail in thumbnails]

# for href in href_list:
#         links.append(href)
#         i=i+1
#         if(i==10000):
#             break

# driver.quit()

# links = [value for value in links if value is not None]
# print(links)

# for link in links:
    # yt = YouTube()
    
    # stream = yt.streams.filter(only_audio=True).first()
    # filePath = stream.download()
    # folderPath = os.path.join(os.path.dirname(filePath), 'mp3_files')
    # os.makedirs(folderPath, exist_ok=True)
    # mp3FilePath = os.path.join(folderPath, os.path.basename(filePath).replace('mp4', 'wav'))
    # os.rename(filePath, mp3FilePath)
    # print(f'mp3FilePath = {mp3FilePath}')

import os
from pytube import YouTube
link = "https://youtu.be/aIIdSVIFJFc"
yt = YouTube(link)
filePath = yt.streams.filter(only_audio=True).first().download()
mp3FilePath = filePath.replace('mp4', 'mp3')
os.rename(filePath, mp3FilePath)
print(f'mp3FilePath = {mp3FilePath}')