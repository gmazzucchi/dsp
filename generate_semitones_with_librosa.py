'''
Ok questo fa il suo mestiere, tuttavia portarlo su un micro la vedo assai dura... A me serve un algoritmo semplice. Comunque per un buon risultato comunque bisogna dargli un passa basso di qualche tipo, perche' ci sono frequenze alte li in mezzo abbastanza fastidiose
'''

import librosa, soundfile, os

y, sr = librosa.load('sample_44kH.wav') # y is a numpy array of the wav file, sr = sample rate

for sem in range(-24, 0):
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=sem)
    # Write out audio as 24bit PCM WAV
    soundfile.write(os.path.join("samples", str(sem+24).zfill(2) + ".wav"), y_shifted, sr, subtype='PCM_16')

