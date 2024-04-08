% Given parameters
N = 4; 
epsilon = 0.3;
Omega_LP = 1;

% Calculate B_k coefficient
B_k = asinh(1 ./ epsilon) ./ N;

% Initialize an array to store the poles
poles = zeros(2*N, 1);

% Compute and display poles in Re + jIm format
disp('Poles:');
for k = 1:2*N
    A_k = (2*k + 1) * pi / (2 * N);
    poles(k) = 1i * Omega_LP * cos(A_k + 1i * B_k);
    fprintf('Pole %d: %.4f + j%.4f\n', k, real(poles(k)), imag(poles(k)));
end

% Save poles to a .dat file
fileID = fopen('poles.txt', 'w');
fprintf(fileID, 'Real Part, Imaginary Part\n');
for k = 1:2*N
    fprintf(fileID, '%.4f, %.4f\n', real(poles(k)), imag(poles(k)));
end
fclose(fileID);
disp('Poles saved to poles.txt file.');
