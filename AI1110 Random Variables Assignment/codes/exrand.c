#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"



int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Generating samples for V
random_V("log_V.dat",1000000);

//Generating samples for triangular random numbers
triangular("tria.dat",1000000);

//Chi random numbers
chi("chi.dat",1000000);

//Root_V 
root_V("root_V.dat",1000000);

//Bernoulli
bernoulli("bernoulli.dat",1000000);

//Y_gen
Y_gen("Y_gen.dat",1000000,0.5);

//X_cap_gen
X_cap_gen("X_cap_gen.dat",1000000);

Err_gen(1000000);

//Prob_err("prob_err.dat",10);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}