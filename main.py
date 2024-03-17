'''
Risultati studio mattina 17 marzo:
lavorare direttamente con il segnale per aggiustare il pitch non puo' funzionare: se hai rapporti finiti lo puoi anche fare e hai una approssimazione (tra il resto modificando parecchio il suono perche' stai tirando via roba), bisogna necessariamente "interpolare" in qualche modo e fare un resampling fatto bene. Il principio e' che dovresti re-immaginare l'audio digitale come segnale continuo e poi prenderti i samples a partire da quello, non puoi lavorare direttamente in digitale. Forse si puo' fare qualcosa con la fft (quasi sicuramente), portando tutto in dominio frequenza e poi tagliando roba direttamente da li, ma bisogna vedere come fare.

Tutto e' comunque complicato da portare in un micro A MENO CHE non si riesca ad elaborare un filtro FIR o IIR che faccia sia pitch che magari accordi e poi si puo' esportare tutto su micro usando il DSP core.
In ogni caso servono almeno 100kByte di flash e di RAM per tenere il primo sampling a 44 kHz. A meno che gia' con quello a 12 o a 20 non vada gia' bene, in tal caso puo' bastare di meno.
'''

import wave, os

SEMITONE_RATIO = 196/185

frequency_table = []
for sem_idx in range(-24, 0):
     frequency_table.append(2 ** (sem_idx / 12)) 

def nskipping_elem(sem: int):
     return (1 - sem) / sem

def build_new_frames(frames: list, nframes: int, loop_point_sample_44khz: int, sem: float):
     new_frames = []
     return new_frames

if __name__ == '__main__':

     print(frequency_table)
     # print(len(frequency_table))
     loop_point_sample_44khz = 9591
     
     wave_file = wave.open('sample_44kH.wav', 'r')
     assert(wave_file.getframerate() == 44100)
     assert(wave_file.getnchannels() == 1)
     assert(wave_file.getsampwidth() == 2)
     nframes = wave_file.getnframes()
     frames = wave_file.readframes(nframes)

     idx = 0     
     for sem in frequency_table:
          new_frames = build_new_frames(frames, nframes, loop_point_sample_44khz, sem)
          output_wave_file = wave.open(os.path.join("samples", "" + str(idx).zfill(2) + ".wav"), 'w')
          idx += 1
          output_wave_file.setframerate(12000)
          output_wave_file.setnchannels(1)
          output_wave_file.setsampwidth(2)
          output_wave_file.setnframes(new_frames)
          output_wave_file.close()


