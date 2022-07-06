#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"



int main() {
    
    double u_mean = mean("uni.dat");
    double u_variance = variance("uni.dat");
    printf("%f\n",u_mean);
    printf("%f\n",u_variance);

    double g_mean = mean("gau.dat");
    double g_variance = variance("gau.dat");
    printf("%f\n",g_mean);
    printf("%f\n",g_variance);
    
    return 0;
}