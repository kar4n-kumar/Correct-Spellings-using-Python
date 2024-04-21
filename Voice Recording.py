# pip install sounddevice,wavio,scipy


"""
RECORD YOUR VOICE

Python can be used to perform a variety of tasks.
One of them is creating a voice recorder.
We can use python’s sound device module to record and play audio.
This module along with the wavio or the scipy module provides
a way to save recorded audio.

"""
print("start recording")
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frq=44100
duration=20 #in seconds
reccorging=sd.rec(int(duration*frq),samplerate=frq,channels=2)
sd.wait()
write('recordings1.wav',frq,reccorging)
