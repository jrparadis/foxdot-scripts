import string
import random

#import FoxDot
#run print(FoxDot.SynthDefs) to get a new list, but that command resets voices in FoxDot so you can't use it live

synths = ['loop', 'stretch', 'play1', 'play2', 'audioin', 'noise', 'dab', 'varsaw', 'lazer', 'growl', 'bass', 'dirt', 'crunch', 'rave', 'scatter', 'charm', 'bell', 'gong', 'soprano', 'dub', 'viola', 'scratch', 'klank', 'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip', 'ripple', 'creep', 'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick', 'twang', 'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star', 'jbass', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 'dbass', 'sinepad']
common = [1/64,1/32,1/16,1/10, 1/8,1/5, 1/4,1/3,1/2,1/2,1,1,2,3,4]
def genrvar():
    return f'{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_lowercase)}'

def genrvoice():
    dur = [random.choice(common) for x in range(1,random.randrange(2,11))]
    varname = genrvar()
    return f'{varname} >> {random.choice(synths)}(oct={random.randrange(1,8)}, dur={dur})\n\n{varname}.stop()\n'

def rpattern():
    return f''


#auto copy output to paste
print(genrvoice())



'''
(weird reverb)

#coily
lr >> soprano(P[6,8,11,15], oct=TimeVar([1,8],1), dur=[0.2, 0.1, 0.5, 0.5, 0.2, 1, 0.5, 0.25, 0.125], room=15, mix=.3,formant=P[:3]).every(4,'stutter').every(8, 'offadd',3)

lr.stop()



xt >> varsaw(oct=TimeVar([1,8],1), dur=[1, 1, 0.5, 0.125, 0.2, 3, 4], glide=2,formant=P[:9]).accompany(lr)

xt.stop()


mh >> pulse(oct=TimeVar([3,8],.5), dur=[0.3333333333333333, 0.015625, 0.1], formant=P[:7])

mh.stop()


vm >> zap(P[6,8,11,15,5], oct=5, dur=[0.03125, 0.015625, 0.03125, 3, 0.2, 0.3333333333333333], formant=P[:4]).every(6, 'offadd',3)

vm.stop()

mh >> pulse(oct=TimeVar([3,8],.5), dur=[0.3333333333333333, 0.015625, 0.1], formant=P[:3]).accompany(vm)

mh.stop()
'''
