import os
import envoy
# assign directory
directory = '/run/media/alexr/New Volume/Music'
 
# iterate over files in music, look for wma files
# convert wma to mp3, replaceing the wma files
random=0
for filename in os.listdir(directory):
    band = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(band):
        random+=1
    # if it is a band, go in and look for files again
    else:
        for filename2 in os.listdir(band):
            album = os.path.join(band, filename2)
            # checking if it is a file
            if os.path.isfile(album):
                random+=1
            #albums
            else:
                with open(album+'/wma2mp3.sh', 'w') as f:
                    f.write('#!/bin/bash\n')
                    f.write('for x in *.wma ; do mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader "$x" ; lame -m s audiodump.wav -o "${x%wma}mp3" ; rm audiodump.wav ; rm "$x"; done')
                envoy.run('./wma2mp3.sh', cwd=album)
                os.remove(album+'/wma2mp3.sh')
                  
print("done")