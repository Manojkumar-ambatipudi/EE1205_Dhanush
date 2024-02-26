#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double trapezoidal_integration(double x[], double y[], int n) {
    double area = 0.0;
    for (int i = 1; i < n; ++i) {
        area += 0.5 * (x[i] - x[i - 1]) * (y[i] + y[i - 1]);
    }
    return area;
}

int main() {
    // Constants
    double R = 1.0;       // Resistance in ohms
    double L = 50e-6;     // Inductance in henrys
    double C = 50e-6;     // Capacitance in farads

    // Angular frequency and phase angle
    double angular_freq = 1 / sqrt(L * C);
    double phi = acos(2 / sqrt(5));

    double Q_o = 10e-3 / cos(phi);

    // Time parameters
    double t_start = 0;
    double t_end = 3e-3;
    int num_points = 1000;

    // Allocate memory for time, voltage, current, and power arrays
    double *time = malloc(num_points * sizeof(double));
    double *voltage = malloc(num_points * sizeof(double));
    double *current = malloc(num_points * sizeof(double));
    double *power = malloc(num_points * sizeof(double));

    // Calculate time, voltage, current, and power
    for (int i = 0; i < num_points; ++i) {
        time[i] = t_start + i * (t_end - t_start) / (num_points - 1);

        voltage[i] = (Q_o / C) * exp(-R * time[i] / (2 * L)) * cos(angular_freq * time[i] - phi);
        current[i] = (-Q_o * R / (2 * L)) * exp(-R * time[i] / (2 * L)) * cos(angular_freq * time[i] - phi) +
                     Q_o * exp(-R * time[i] / (2 * L)) * sin(angular_freq * time[i] - phi) * (-angular_freq);
        power[i] = pow(current[i], 2) * R;
    }

    // Calculate area under curve using trapezoidal rule which gives total energy dissipated
    double area_under_power_curve = trapezoidal_integration(time, power, num_points);
    printf("Area under the power curve: %.6lf Joules\n", area_under_power_curve);

    
    FILE *output_file = fopen("data_for_damping.txt", "w");
    if (output_file == NULL) {
        fprintf(stderr, "Error opening output file.\n");
        return 1;
    }

    // Append the calculated data to the file
    fprintf(output_file, "Time(s)\tVoltage(V)\tCurrent(A)\tPower(W)\n");
    for (int i = 0; i < num_points; ++i) {
        fprintf(output_file, "%.6lf   %.6lf   %.6lf    %.6lf\n", time[i], voltage[i], current[i], power[i]);
    }

    fclose(output_file);

    // Free allocated memory
    free(time);
    free(voltage);
    free(current);
    free(power);

    return 0;
}
