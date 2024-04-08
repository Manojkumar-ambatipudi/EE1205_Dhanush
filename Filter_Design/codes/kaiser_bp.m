% Define filter parameters
fs = 48000;          % Sampling frequency
fc = 0.0553/2;       % Cutoff frequency
N = 48;              % Filter length (odd for Type I FIR filters)
beta = 0;            % Kaiser window beta parameter

% Design the filter using the Kaiser window method
h = fir1(N-1, fc/(fs/2), 'low', kaiser(N, beta));

% Compute the frequency response
[H, f] = freqz(h, 1, 1024, fs);

% Plot the magnitude response
plot(f, 20*log10(abs(H)));  % Convert frequency to kHz
title('Magnitude Response of Kaiser Window Lowpass Filter');
xlabel('Frequency (Hz)');         % Label as Hz
ylabel('Magnitude (dB)');
grid on;


xlim([0, 10000]);
ylim([-50,0]);
