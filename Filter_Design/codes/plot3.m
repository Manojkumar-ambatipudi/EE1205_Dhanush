% Given parameters for epsilon = 0.5
s1 = -0.1907 + -1.0322i ;
s2 = -0.4604 + -0.4276i ;
s3 = -0.4604 + 0.4276i ;
s4 =-0.1907 + 1.0322i ;
epsilon = 0.3;
Omega_Lp = 1;

% Define denominator polynomial
den = poly([s1 s2 s3 s4]);

% Define frequency range
w = -2:0.01:2;

G_LP = 0.4166;
num = G_LP;

Omega_p1 = 0.5913;
Omega_p2 = 0.702;

Omega_s1 = 0.5662;
Omega_s2 = 0.7361;

% Define parameters for transformation
B = 0.1107;
Omega0 = 0.644;

% Perform transformation to get s_L
s_L = (1i*w).^2 + Omega0^2;
s_L = s_L ./ (B * (1i*w));

%Band pass gain
G_bp = 1.0370; 

% Substitute s = jw into H(s)
H =  G_bp*(num ./ polyval(den, s_L));

% Plot magnitude response for H(s)
figure;
plot(w, abs(H) , 'Linewidth' , 1);
title('Band Pass Filter');
xlabel('Analog Frequency (\Omega)');
ylabel('|H_{a,BP}(j\Omega)|');
grid on;
ylim([0, 1.2]);