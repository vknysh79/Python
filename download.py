from pytube import YouTube
from pytube import Playlist


def download_video_list(youtube_link):

    #input = array
    #for the length of the array you feed in.
    for x in range(len(youtube_link)):
        
        #we will use a try statement because we don't want the code to stop if a youtube video is unsuccessfully downloaded.
        try:
            #place link to video you want.
            url = YouTube(str(youtube_link[x]))

            #than we add a variable called streams, set are download with path.
            #if you want video, streams = url.streams.filter(only_audio=True).all()
            #else you want audio only. streams = url.streams.filter(only_audio=True).get_by_itag('x')
            streams = url.streams.filter(only_audio=True)

            #part of video
            streams = url.streams.first()

            #destination of where you are saving the video on your system.
            streams.download("file_path_here_folder")

            #print statement will appear in ide to confirm when and if it downloaded the video starting from 0 to len(youtube_links)
            print("done "+str(x))

        #this except handles and problems that occur if the file does not download correctly letting you know.    
        except:
            print("file corrupt "+str(x))
            continue
    #close the ide when finished.
    exit()

#creating a list of all the youtube links you want to download from your url_links.txt file.

#empty list.
youtube_link = []

#open text file with links.
file_txt = open("file_path_here_.txt","r")

#for loop to iterate over the text file and append the strings to youtube_link array.
for line in file_txt:

    #seperate by a new line.    
    line = line.rstrip("\n")
    #append each line to array.
    youtube_link.append(line)

#close txt file at the end of loop.
file_txt.close()


#run above function feeding in the list you created.
download_video_list(youtube_link)
