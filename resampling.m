%{
    Obiettivo:
    caricare sample a 12 kHz e poi fare il resampling per generare tutte le
    note della scala cromatica

    Vedere poi come si puo per fare in C questa cosa

    Come spiegato in main.py questa cosa non e' possibile per vari motivi,
    bisogna per forza filtrare roba.
%}

[audio_content, sampl_freq] = audioread("sample_12kH.wav");

% poi in c questa tabella sara' preallocata e fine
frequency_table = zeros(1, 25);
for idx = -24:0
    frequency_table(24 + idx + 1) = nthroot(2, 12) ^ idx;
end

[deep_note, sf_0] = audioread("samples/00.wav");
[base_note, sf_1] = audioread("samples/12.wav");
[fifth_note, sf_2] = audioread("samples/19.wav");
assert((sf_0 == sf_1) && (sf_1 == sf_2));

res_note = (base_note + fifth_note + deep_note) / 3;
L=length(res_note);

% x_axys = (ones(1, length(res_note))) ./ (1:length(res_note));
% x_axys = 1:L;
% plot(x_axys, fifth_note);

audiowrite("samples/empty_chord.wav", res_note, sf_1);

audio_freq_domain = fftshift(fft(fifth_note));
dF = sf_0/L;
x_axys_fft = -sf_0/2:dF:sf_0/2-dF;
plot(x_axys_fft,abs(audio_freq_domain) / L,"LineWidth",3);
title("Complex Magnitude of fft Spectrum")
xlabel("f (Hz)")
ylabel("|fft(X)|")

