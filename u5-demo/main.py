# from sample import *

# out = open("sample44kHz.c", "w+")

# counter = 0

# for elem in DATA:
#     out.write(str(int(elem * 32767 / 30)) + ",\n")
#     counter += 1
# for idx in range(9591 - 1, len(DATA) - 1):
#     out.write(str(int(DATA[idx] * 32767 / 30)) + ",\n") 
#     counter += 1
    
# print(counter)

import wave, os

# inp = open)
inw = wave.open("../sample_22kHz.wav", "r")
outw = open("out.txt", "wb+")
N = inw.getnframes()
frames = inw.readframes(N)
outw.write(frames)
# data = list(frames)
# for x in data:
    # outw.write(str(x) + ",\n")
