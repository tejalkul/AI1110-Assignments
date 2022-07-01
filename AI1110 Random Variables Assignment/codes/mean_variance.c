#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

double mean_U2(char *str) {
    int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x*x;
}
fclose(fp);
temp = temp/(i-1);
return temp; 
}

double variance(char *str) {
    double var = mean_U2(str) - mean(str)*mean(str);
    return var;
}

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