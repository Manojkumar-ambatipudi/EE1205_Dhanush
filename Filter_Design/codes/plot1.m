% Given parameters
epsilons = [0.278,0.45, 0.55, 0.61]; 
Omega_Lp = 1; 

% Range of Omega_L values
Omega_L_values = 0:0.01:2;

%Value of oder of filter 
N =4;
% Tolerance for passband and stopband
passband_tolerance = 0.15;
stopband_tolerance = 0.15;

% Calculate Ha(jOmega_L) for different Omega_L values
Ha_values = zeros(length(epsilons), length(Omega_L_values));
for j = 1:length(epsilons)
    epsilon = epsilons(j);
    for i = 1:length(Omega_L_values)
        Omega_L = Omega_L_values(i);
        x = Omega_L / Omega_Lp;
        
        c_N = cos(N * acos(x));
        
        Ha_values(j, i) = 1 / sqrt(1 + epsilon^2 * c_N^2);
    end
end

% Plotting
figure;
hold on;
for j = 1:length(epsilons)
    plot(Omega_L_values, abs(Ha_values(j, :)), 'DisplayName', ['Epsilon = ', num2str(epsilons(j))]);
end

% Draw passband and stopband
passband_lower_limit = 1 - passband_tolerance;
stopband_upper_limit = stopband_tolerance;

% Passband
passband_x = [0, 1, 1, 0];
passband_y = [passband_lower_limit, passband_lower_limit, 1, 1];
fill(passband_x, passband_y, 'g', 'FaceAlpha', 0.3, 'EdgeColor', 'none');

% Stopband
stopband_x = [1.502, 2, 2, 1.502];
stopband_y = [0, 0, stopband_upper_limit, stopband_upper_limit];
fill(stopband_x, stopband_y, 'r', 'FaceAlpha', 0.3, 'EdgeColor', 'none');

hold off;

xlabel('\Omega_L');
ylabel('|Ha LP(jΩ_L)|');
legend('Epsilon = 0.278', 'Epsilon = 0.45', 'Epsilon = 0.55', 'Epsilon = 0.61', 'Passband', 'Stopband', 'Location', 'best');
grid on;

