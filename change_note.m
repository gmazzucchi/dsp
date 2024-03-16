%{ 
RIASSUNTO STUDIO 16 MARZO 2024:

A partire da un soundfont ho ricavato un wav singolo. Da questo ho provato
a cambiare la sua frequenza base per ricavare gli altri. Ho provato a
lavorare nel dominio frequenza ma senza eccellenti risultati. Il tentativo
e' stato quello di aumentare o diminuire lo spazio vuoto della dft ma
comunque mi sembra un lavoro abbastanza sporco, bisognerebbe secondo me
direttamente lavorare in dominio frequenza togliendo samples o facendo il x
tot e poi se serve pulire dopo con un filtro leggero. Come 

A un sampling rate altissimo (190kHz) ogni nota pesa circa 450KB, il che
risulta assai complesso per un sistema embedded, tuttavia la frequenza e'
totalmente irrealistica.

Tuttavia forse si puo' fare SE si riduce la frequenza a tipo 12kHz, in tal
caso la memoria necessaria sarebbe:
(27 kilobytes) x 24 = 648 kB
che comunque sarebbe importante per una mcu.
A meno che non si carichi quello base e a runtime si calcoli gli altri, ma
comunque la RAM sarebbe il bootleneck.

Riassunto
%}

% [original_audio_content, frequency_sampling] = audioread("pipe_organ_base_sound.wav");
[original_audio_content, frequency_sampling] = audioread("sample_190kH.wav");

loop_point_44kH = 9591;
loop_point_190kH = 41756;

for idx = -10:10
    audiowrite(strcat("note_", string(idx), ".wav"), original_audio_content, up_semitones(frequency_sampling, idx));
end

% major chord

audiowrite("major_chord.wav", original_audio_content, up_semitones(frequency_sampling, 12));

% the formula for changing note is Fs: (throot(2, 12) ^ nsemitones)

% take the fourier transform of the signal and then
L=length(original_audio_content);
audio_freq_domain = fft(original_audio_content);

% plot(frequency_sampling/L*(0:L-1),abs(audio_freq_domain),"LineWidth",3);
% title("Complex Magnitude of fft Spectrum")
% xlabel("f (Hz)")
% ylabel("|fft(X)|")

x_axys = frequency_sampling/L*(-L/2:L/2-1);
% plot(x_axys,abs(fftshift(audio_freq_domain)),"LineWidth",3)
% title("fft Spectrum in the Positive and Negative Frequencies")
% xlabel("f (Hz)")
% ylabel("|fft(X)|")

% OK in dominio frequenza non sono esattamente simmetrici tuttavia anche
% togliendo la parte immaginaria del complesso comunque ci sta, non c'e'
% troppa distorsione, e' un po' piu' meccanico il suono ma sempre nei
% limiti.
reverse_fft = ifft(real(audio_freq_domain));
audiowrite("test5.wav", reverse_fft, frequency_sampling);

% prova da chatgpt: bisogna paddare non inserire in mezzo!!!
% Half the frequency by zero-padding the FFT
fft_original = audio_freq_domain;
doubled_fft = zeros(1, 2 * length(fft_original));
doubled_fft(1:length(fft_original)/2) = fft_original(1:length(fft_original)/2);
doubled_fft(end-length(fft_original)/2+1:end) = flip(fft_original(1:length(fft_original)/2));
doubled_signal = ifft(doubled_fft);

% vediamo se comprimendo e lasciando sempre N di lunghezza funziona
% test_dfft = zeros(1, length(fft_original));
% test_dfft(1:length(fft_original)/4) = fft_original(1:length(fft_original)/2);

% plot(x_axys, fft_original);
L2 = length(doubled_fft);
% plot(frequency_sampling/L*(-L2/2:L2/2-1), doubled_fft);
% title("fft spectrum for doubled signal")
% xlabel("f (Hz)")
% ylabel("|fft(X)|")
audiowrite("test6_ottava_sotto.wav", real(doubled_signal), frequency_sampling);

% stessa cosa ma il contrario non va...
half_fft = fft_original(1:length(fft_original/2));
half_signal = ifft(half_fft);
audiowrite("test6_ottava_sopra.wav", real(half_fft), frequency_sampling);

% test_doppia_ottava = original_audio_content + doubled_signal;
% audiowrite("test9.wav", real(test_doppia_ottava), frequency_sampling);

% raddoppiamo la frequenza direttamente nel dominio frequenza
% Questo non fa cambiare assolutamente nulla
half_freq = audio_freq_domain(2:2:end);
reverse_fft2 = real(ifft((half_freq)));
audiowrite("test6.wav", reverse_fft2, frequency_sampling);

function new_sampling_frequency = up_semitones(base_freq, nsemitones)
    new_sampling_frequency = round(base_freq * (nthroot(2, 12) ^ nsemitones));
end

