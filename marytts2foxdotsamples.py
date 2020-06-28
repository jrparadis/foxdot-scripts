import os
import requests
import time
import string
import shutil
import random
#uses the synesthesiam/marytts docker image for MaryTTS, a text to speech platform that generates speech as wav files
#http://mary.dfki.de/ for more information

englishvoices = ['cmu-bdl-hsmm en_US male hmm', 'dfki-spike-hsmm en_GB male hmm', 'dfki-prudence-hsmm en_GB female hmm', 'dfki-poppy-hsmm en_GB female hmm', 'dfki-obadiah-hsmm en_GB male hmm', 'cmu-slt-hsmm en_US female hmm', 'cmu-rms-hsmm en_US male hmm']


foldername = 'thisisatest' #ultimate folder name

text = 'this is just a big old test, I don\'t know what to say other than that. cabbage rhubarb onion garlic thyme blue cheese'

listofwavs = []
tempdir = 'temp'
os.mkdir(tempdir)

for each in text.split(' '):
    inputtext = each.strip()
    voicepick = random.choice(englishvoices)
    propervoiceformats = [voicepick, voicepick.split(' ')[0], voicepick.split(' ')[1]]
    url = f"""http://192.168.0.6:59125/process?INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&INPUT_TEXT={inputtext}&VOICE_SELECTIONS={propervoiceformats[0].replace(' ','%20')}&LOCALE={propervoiceformats[2]}&VOICE={propervoiceformats[1]}&AUDIO=WAVE_FILE"""
    print(url)
    open(f'{tempdir}/{each}.wav', 'wb').write(requests.get(url).content)
    listofwavs.append(f'{each}.wav')
cwd = os.getcwd()

allchars = string.ascii_lowercase
os.mkdir(f'{cwd}\{foldername}')
lenoflist = len(listofwavs)
try:
    for each in allchars:
            os.mkdir(f'{cwd}/{foldername}/' + each)
            os.mkdir(f'{cwd}/{foldername}/' + each + '/lower')
            os.mkdir(f'{cwd}/{foldername}/' + each + '/upper')
            shutil.move(f'{tempdir}/' + listofwavs[0],f'{cwd}/{foldername}/' + each + '/lower')
            listofwavs.pop(0)
            shutil.move(f'{tempdir}/' + listofwavs[0],f'{cwd}/{foldername}/' + each + '/upper')
            listofwavs.pop(0)
except Exception as e:
    print(f'error, {lenoflist}/52 samples - probably not enough - {e}')

print(f'python -m FoxDot --dir {cwd}\{foldername}')
print("run p1 >> play('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ') to test samples")
shutil.rmtree(f'{tempdir}', ignore_errors=True)
