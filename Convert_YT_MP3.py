# Convertendo vídeo do youtube para música mp3


import pytube
import moviepy
##################################################################
from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input('Digite o Link do Vídeo que deseja converter: ')
path = input('Coloque o caminho que deseja salvar o áudio: ')
yt = YouTube(link)
##################################################################
#  Baixando o áudio
print('Baixando...')
ys = yt.streams.filter(only_audio=True).first().download(path)
print('Download Completo')

###################################################################
# Convertendo mp4 para mp3
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucesso!')
