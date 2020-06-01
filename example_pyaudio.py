import okhound
import pyaudio


CHUNKSIZE = 1024

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNKSIZE)

okhound.setThreshold(0.4)

while True:
	try:
		audio = stream.read(CHUNKSIZE)
	except IOError:
		print("Skipped frame")
		continue

	phraseSpotted = okhound.processSamples(audio)
	if phraseSpotted: break


print("'Ok Hound' spotted! Sensitivity: {0}".format(okhound.getThreshold()))
