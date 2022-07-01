#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void random_V(char *str,int len) {
    int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
    fprintf(fp,"%lf\n",((-2)*log(1 - (double)rand()/RAND_MAX)));
}
fclose(fp);
 
}

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Generating samples for V
random_V("log_V.dat",1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}