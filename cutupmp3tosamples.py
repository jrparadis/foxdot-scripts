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
filename = 'kebabtraume.mp3'
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
    newAudio.export(f'{os.getcwd()}/{filenamenoext}/temp/myfile{each}.wav', format='wav')
    outputfiles.append(f'{os.getcwd()}/{filenamenoext}/temp/myfile{each}.wav')

random.shuffle(outputfiles)
randomfiles = [random.choice(outputfiles) for x in range(0,48)]
print(randomfiles)

allchars = string.ascii_lowercase

for each in allchars:
    os.mkdir(f'{cwd}/{filenamenoext}/' + each)
    os.mkdir(f'{cwd}/{filenamenoext}/' + each + '/lower')
    os.mkdir(f'{cwd}/{filenamenoext}/' + each + '/upper')
    shutil.move(outputfiles[0],f'{os.getcwd()}/{filenamenoext}/' + each + '/lower')
    outputfiles.pop(0)
    shutil.move(outputfiles[0],f'{os.getcwd()}/{filenamenoext}/' + each + '/upper')
    outputfiles.pop(0)

shutil.rmtree(f'{os.getcwd()}/{filenamenoext}/temp')

#run this to load folder of samples, play them all with play('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'python3 -m FoxDot --dir {os.getcwd()}/{filenamenoext}')

    
