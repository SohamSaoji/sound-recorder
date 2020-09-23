# pip install sounddevice
# pip install scipy

# import required libraries
import sounddevice as sd
from scripy.io.wavfile import write

# sampling frequency
freq = 44100

# recording duration
duration = 5

# start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate, channels=2)

# record audio for the given number of seconds
sd.wait()

# this will convert the NumPy array to an audio
# file with the given sampling frequency
write('recording0.wav', freq, recording)

# convert the NumPy array to audio file
wv.write("recording0.wav", recording, freq,sampwidth=2)
