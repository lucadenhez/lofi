import os

path = "C:/Users/lucad/Documents/LofiWebsite/music"
files = os.listdir(path)

for i in range (len(files)):
    os.rename(path + '/' + files[i], path + '/' + str(i) + ".mp3")
