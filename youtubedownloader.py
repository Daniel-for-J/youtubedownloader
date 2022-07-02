from pytube import YouTube

# Danny codes

counter = input('How many videos do you want to download? ')


for i in range(0, int(counter)):
    while True:
        try:
          url = input("Type in url ")
          video = YouTube(url)
          videoDownloader = video.streams.get_highest_resolution()
          print("Download In Progress...") 
          videoDownloader.download()
          print("Download successful")
          break
        except:
          pass
