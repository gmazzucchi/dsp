%{
    Obiettivo:
    caricare sample a 12 kHz e poi fare il resampling per generare tutte le
    note della scala cromatica

    Vedere poi come si puo per fare in C questa cosa
%}

[audio_content, sampl_freq] = audioread("sample_12kH.wav");

% poi in c questa tabella sara' preallocata e fine
frequency_table = zeros(1, 25);
for idx = -24:0
    frequency_table(24 + idx + 1) = nthroot(2, 12) ^ idx;
end

