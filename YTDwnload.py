try:
	from pytube import YouTube 
except:
	print ('Эй бастард, напиши: pip install pytube3')

import os, sys

SAVE_PATH = "/" 

os.system ('mkdir Vidosiki')
SAVE_PATH = "Vidosiki/"

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')


def main():

	print ('''

Наш уютный Телеграм канал: @Termuxtop
 ▄· ▄▌▄▄▄▄▄·▄▄▄▄  ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄  
▐█▪██▌•██  ██▪ ██ ██· █▌▐█•█▌▐███•  ▪     ▐█ ▀█ ██▪ ██ 
▐█▌▐█▪ ▐█.▪▐█· ▐█▌██▪▐█▐▐▌▐█▐▐▌██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌
 ▐█▀·. ▐█▌·██. ██ ▐█▌██▐█▌██▐█▌▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ 
  ▀ •  ▀▀▀ ▀▀▀▀▀•  ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀• 

[1] -> Загрузить одно видео
[2] -> Загрузить много видео

	''')

	
	task = input ('Сколько видео вы желаете загрузить:')

	if task == '1':

		video = input ('Введите ссылку на видео:')

		try:
			yt = YouTube(video)

			mp4files = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution").last()

			mp4files.download (SAVE_PATH)

		except:
			print('Неприавльная ссылка')

	if task == '2':

		videoFile = input ('Введите ссылку на файл с видео:')
			
		with open(videoFile, 'r') as file:
			vidos = file.read().splitlines()

		for video in vidos:

			try:
				yt = YouTube(video)
				
				mp4files = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution").last()

				mp4files.download (SAVE_PATH)

			except:
				print ('Непривильная ссылка')
				continue


if __name__ == '__main__':
	clear()
	main()
