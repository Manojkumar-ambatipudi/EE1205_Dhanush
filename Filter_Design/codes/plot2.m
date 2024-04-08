% Given parameters for epsilon = 0.5
s1 = -0.1907 + -1.0322i ;
s2 = -0.4604 + -0.4276i ;
s3 = -0.4604 + 0.4276i ;
s4 =-0.1907 + 1.0322i ;
epsilon = 0.3;
Omega_Lp = 1;

% Generate the denominator polynomial
den = poly([s1 s2 s3 s4]);

% Define frequency range
w = 0:0.01:2;

% Calculate c_N
x = w / Omega_Lp;
c_N = zeros(size(x));
for i = 1:length(x)
    
 c_N(i) = cos(4 * acos(x(i))); % N = 4
end

% Calculate |Ha(jOmega_L)|
Ha_values = 1 ./ sqrt(1 + epsilon^2 * c_N.^2);

% Plot magnitude response for epsilon = 0.5
figure;
plot(w, Ha_values,'-o');
hold on;

G_LP = 0.4166;
num = G_LP;
% Calculate magnitude response for epsilon = 0.5
s = 1i*w;
H = num ./ polyval(den, s);
magnitude = abs(H);

% Plot magnitude response for epsilon = 0.5
plot(w, magnitude);
title('Design vs Specifications');
xlabel('Analog Frequency (\Omega)');
ylabel('|H_{a,LP}(j\Omega)|');
legend('Design', 'Specification');
grid on;
ylim([0, 1.1]); % Set the y-axis limits from 0 to 2

hold off;
