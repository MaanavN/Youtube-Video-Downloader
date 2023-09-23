#!/bin/python3

import pytube
import sys
import time

try:
	def get_ytvid():
		while True:
			try:
				url = input("YouTube video URL: ")
				yt = pytube.YouTube(url)
				break
			except:
				loop_back = ""
		
		return yt



	def download_vid(yt):
		stream = yt.streams.filter(progressive=True)
		stream_str = str(stream)
		
		stream_list = stream_str.split("\"")
		itag = stream_list[1]
		
		stream = yt.streams.get_by_itag(itag)
		try:
			print("\n")
			print("-" * 50)
			print("Starting Download")
			print("-" * 50)
			stream.download("/downloaded_vids")
		except PermissionError:
			print("\nLacking privilages to download in the designated folder. Will now attempt to download in current directory")
			time.sleep(3)
			print("\n")
			print("-" * 50)
			print("Starting Download")
			print("-" * 50)
			stream.download()
		
		print("\nDownload Complete")



	yt = get_ytvid()
	download_vid(yt)
	
except KeyboardInterrupt:
	sys.exit()
