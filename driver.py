import pafy
import os

def convertwebmToMp3(url):
    # Download the video from youtube
    video = pafy.new(url)
    # Get the best audio
    bestaudio = video.getbestaudio()
    # Get the best audio file
    bestaudio.download()
    # Get the file name
    fileNameOld = bestaudio.filename
    # Remove the file extension
    fileName = fileNameOld[0:len(fileNameOld)-5]
    # Convert the file to mp3
    arg = "ffmpeg -i \"" + fileNameOld +"\" \""+ fileName + ".mp3\" -y"
    os.system(arg)
    # Delete the original file
    os.system("Del \"" + fileNameOld + "\" -y")
    # Return the file name
    return fileName + ".mp3"

def parseUrls():
    ''' 
    loop through each line in urls.txt in which 
    each line is a url and convert it to mp3
    '''
    with open("urls.txt", "r") as f:
        for line in f:
            convertwebmToMp3(line)

parseUrls()