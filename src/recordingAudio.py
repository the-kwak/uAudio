import pyaudio
import sys
import wave
import audioop

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 4

p = pyaudio.PyAudio()
print 'total number of audio devices:'
print p.get_device_count()
print 'getting info of all the devices...'
for i in range(p.get_device_count()):
    print p.get_device_info_by_index(i)

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk
)

print "****recording*****"
frames = []
print frames
for i in range(0, RATE/chunk*RECORD_SECONDS):
    data = stream.read(chunk)
    maxofchunk = audioop.max(data,2)
    #print maxofchunk
    frames.append(data)
print "finished recording";
#print frames

stream.stop_stream()
stream.close()
p.terminate()

wavF = wave.open('../recordings/test_record.wav','wb')
wavF.setnchannels(CHANNELS)
wavF.setsampwidth(p.get_sample_size(FORMAT))
wavF.setframerate(RATE)
wavF.writeframes(b''.join(frames))
wavF.close()
