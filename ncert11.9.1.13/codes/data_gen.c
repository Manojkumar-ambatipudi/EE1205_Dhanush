#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x(n)\n");

    // Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
    for (int n = -10; n <= 10; n++) {
        // Calculate values
        int u_n = n >= 0 ? 1 : 0;
        int u_n_minus_1 = (n - 1) >= 0 ? 1 : 0;
        int result = 2 * u_n + (1 - n) * u_n_minus_1;

        // Write to file
        fprintf(file, "%d     %d\n", n, result);
    }

    fclose(file);

    return 0;
}
