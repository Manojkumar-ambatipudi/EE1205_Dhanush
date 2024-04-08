% Given parameters for epsilon = 0.3
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

num = 0.4166;


% Define parameters for transformation
B = 0.1107;
Omega0 = 0.644;

% Perform transformation to get s_L
s_L = (1i* 0.5913).^2 + Omega0^2;
s_L = s_L ./ (B * (1i* 0.5913));


H = num ./ polyval(den, s_L);
disp(1/abs(H));