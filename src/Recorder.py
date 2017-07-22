import pyaudio
import audioop
import sys
import wave

p = pyaudio.PyAudio()

class Recorder:
    def __init__(self, channels=2, rate=44100,
                 frames_per_buffer=1024, record_seconds=5,
                 fname='record_file.wav'):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.format = pyaudio.paInt16
        self.record_seconds = record_seconds
        self.fname = fname,
        self.frames = [],
        self.stream = p.open(
            format = self.format,
            channels = self.channels,
            rate = self.rate,
            input = True,
            output = True,
            frames_per_buffer = self.frames_per_buffer
        )
    def record(self):
        print 'recording...'
        buf = []
        for i in range(0, self.rate/self.frames_per_buffer*self.record_seconds):
            data = self.stream.read(self.frames_per_buffer)
            buf.append(data)
        self.frames = buf
        print 'recording completed.'
        self.stream.stop_stream()
        self.stream.close()
        p.terminate()

        print 'creating audio file...'
        wavF = wave.open('../recordings/'+self.fname[0],'wb')
        wavF.setnchannels(self.channels)
        wavF.setsampwidth(p.get_sample_size(self.format))
        wavF.setframerate(self.rate)
        wavF.writeframes(b''.join(self.frames))
        wavF.close()
        print 'audio file created!'
