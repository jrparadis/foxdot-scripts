#requires python3 for fstrings
#cuts up an mp3 into small fragments, chooses random fragments and makes a directory for use with FoxDot

import random
import string
from pydub import AudioSegment
import os
import shutil

#time in ms
sampletime = 250
#could change this to a kwarg, just put the mp3 file in the same folder as the script for now
#this seems to have issues with ffmpeg on windows at times, I just use linux instead
filename = 'example.mp3'
filenamenoext = filename.split('.')[0]
sound = AudioSegment.from_file(filename, format='mp3')
outputfiles = []
cwd = os.getcwd()
print(f'{cwd}')
try:
    shutil.rmtree(f'{cwd}/{filenamenoext}')
except:
    print(f'dir {filenamenoext} does not exist')
os.mkdir(f'{cwd}/{filenamenoext}')
os.mkdir(f'{cwd}/{filenamenoext}/temp')
for each in range(0,len(sound),sampletime):
    newAudio = sound[each:each+sampletime]
    newAudio.export(f'{cwd}/{filenamenoext}/temp/{each}.wav', format='wav')
    outputfiles.append(f'{cwd}/{filenamenoext}/temp/{each}.wav')

random.shuffle(outputfiles)
randomfiles = [random.choice(outputfiles) for x in range(0,48)]
print(randomfiles)

allchars = string.ascii_lowercase

key = 'z' #key to use for sampling if you enable line 48

for each in allchars:
    os.mkdir(f'{cwd}/{filenamenoext}/' + each)
    os.mkdir(f'{cwd}/{filenamenoext}/' + each + '/lower')
    os.mkdir(f'{cwd}/{filenamenoext}/' + each + '/upper')
    shutil.move(outputfiles[0],f'{cwd}/{filenamenoext}/' + each + '/lower')
    outputfiles.pop(0)
    shutil.move(outputfiles[0],f'{cwd}/{filenamenoext}/' + each + '/upper')
    outputfiles.pop(0)
    
    #version for moving to a certain folder with default samples available, default foxdot samples need to be in a folder named snd in the same directory
    #shutil.move(each,f'{os.getcwd()}/snd/' + key + '/upper')
shutil.rmtree(f'{cwd}/{filenamenoext}/temp')

#run this to load folder of samples, play them all with play('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'python3 -m FoxDot --dir {cwd}/{filenamenoext}')

    
