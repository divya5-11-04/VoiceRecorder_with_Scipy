import sounddevice
from scipy.io.wavfile import write
def divyavoice_recorder(seconds,file):
    print("Recording Started.....")
    divyarecording = sounddevice.rec((seconds*44100),
                                     samplerate = 44100,
                                     channels =2)
    sounddevice.wait()
    write(file,44100,divyarecording)
    print("Recording is finished")

divyavoice_recorder(10,"recordsave.wav")