% Given parameters 
s1 = -0.1907 + -1.0322i ;
s2 = -0.4604 + -0.4276i ;
s3 = -0.4604 + 0.4276i ;
s4 =-0.1907 + 1.0322i ;
epsilon = 0.3;
Omega_Lp = 1;

% Generate the denominator polynomial
den = poly([s1 s2 s3 s4]);
num = 1;
s = 1i*1; %use \Omega = 1
H = num ./ polyval(den, s);

req = 1/sqrt(1+epsilon^2) ;

Gain_LP = req/abs(H);
disp(Gain_LP);