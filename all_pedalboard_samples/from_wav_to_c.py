import wave, os

if __name__ == "__main__":
    files = os.listdir()    
    for file in files:
        if file.endswith(".wav"):
            wavobj: wave.Wave_read = wave.open(file, "r")
            nchannels = wavobj.getnchannels()
            nframes = wavobj.getnframes()
            frames = wavobj.readframes(nframes=nframes)
            framerate = wavobj.getframerate()
            print(file, nchannels, nframes, framerate)
            wavobj.close()

