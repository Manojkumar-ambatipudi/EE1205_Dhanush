% Read pole data from the txt file
data = dlmread('poles.txt', ',', 1, 0);

% Separate real and imaginary parts
real_parts = data(:, 1);
imaginary_parts = data(:, 2);

% Identify poles on the left side of the complex plane
left_poles_indices = real_parts < 0;
left_real_parts = real_parts(left_poles_indices);
left_imaginary_parts = imaginary_parts(left_poles_indices);

% Plot poles as red crosses ('x')
scatter(real_parts(~left_poles_indices), imaginary_parts(~left_poles_indices), 'rx', 'MarkerEdgeColor', 'r', 'LineWidth', 1.5); % Poles not on the left side
hold on;
scatter(left_real_parts, left_imaginary_parts, 'bx', 'MarkerEdgeColor', 'b', 'LineWidth', 1.5); % Poles on the left side

% Add labels and title
xlabel('Real Part');
ylabel('Imaginary Part');
title('Pole-Zero Plot');

% Set aspect ratio to equal
axis equal;

% Draw real and imaginary axes
plot([0 0], ylim * 1.2, 'k--'); % Vertical line for the imaginary axis, extending ylim by 20%
plot(xlim, [0 0], 'g--'); % Horizontal line for the real axis

% Add legend
legend('Poles (Right)', 'Poles (Left)', 'Location', 'northwest');

% Display the plot
hold off;
