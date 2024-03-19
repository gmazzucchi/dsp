[audio_content, sampl_freq] = audioread("sample_44kH.wav");
semitone_ration = 1.059463094;
L = length(audio_content);
loop_point_44kH = 9591;

% generare la quinta con signal reconstruction
% il risultato e' molto buono in realta' considerando che c'e' solamente
% un signal reconstruction algorithm stupidissimo senza filtri ne niente

fifth_ratio = semitone_ration ^ 5;
% test 1: semplice lookup table
fifth_chord = zeros(1, L);
for idx = 1:L
    i = (idx * fifth_ratio);
    if i > loop_point_44kH
        i = mod(i, L - loop_point_44kH) + (loop_point_44kH);
    end
    fifth_chord(idx) = audio_content(round(i));
end

audiowrite("signal_reconstruction_experiment/fifth.wav", fifth_chord, sampl_freq);

% resampling a 12kHz
% ok questo fa una cosa diversa
% resampled = resample(fifth_chord, sampl_freq, 12000);
% audiowrite("signal_reconstruction_experiment/fifth_resampled.wav", resampled, ...
    % 12000);

