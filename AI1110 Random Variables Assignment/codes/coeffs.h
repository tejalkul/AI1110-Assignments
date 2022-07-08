#include <math.h>


//Function declaration
double **createMat(int m,int n);
void readMat(double **p, int m,int n);
void print(double **p,int m,int n);
double **loadtxt(char *str,int m,int n);
double linalg_norm(double **a, int m);
double **linalg_sub(double **a, double **b, int m, int n);
double **linalg_inv(double **mat, int m);
double **matmul(double **a, double **b, int m, int n, int p);
double **transpose(double **a,  int m, int n);
void uniform(char *str, int len);
void gaussian(char *str, int len);
double mean(char *str);
//End function declaration


//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


//Defining the function for reading matrix 
void readMat(double **p, int m,int n)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix

//Read  matrix from file
double **loadtxt(char *str,int m,int n)
{
FILE *fp;
double **a;
int i,j;


a = createMat(m,n);
fp = fopen(str, "r");

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   fscanf(fp,"%lf",&a[i][j]);
  }
 }
//End function for reading matrix from file

fclose(fp);
 return a;

}


//Defining the function for printing
void print(double **p, int m,int n)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf ",p[i][j]);
 printf("\n");
 }
}
//End function for printing

//Defining the function for norm

double linalg_norm(double **a, int m)
{
int i;
double norm=0.0;

 for(i=0;i<m;i++)
 {
norm = norm + a[i][0]*a[i][0];
}
return sqrt(norm);

}
//End function for norm

//Defining the function for difference of matrices

double **linalg_sub(double **a, double **b, int m, int n)
{
int i, j;
double **c;
c = createMat(m,n);

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
c[i][j]= a[i][j]-b[i][j];
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for inverse of 2x2 matrix


double **linalg_inv(double **mat, int m)
{
double **c, det;
c = createMat(m,m);

det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];

c[0][0] = mat[1][1]/det;
c[0][1] = -mat[1][0]/det;
c[1][0] = -mat[0][1]/det;
c[1][1] = mat[0][0]/det;

return c;

}
// End  function for inverse of 2x2 matrix


//Defining the function for difference of matrices

double **matmul(double **a, double **b, int m, int n, int p)
{
int i, j, k;
double **c, temp =0;
c = createMat(m,p);

 for(i=0;i<m;i++)
 {
  for(k=0;k<p;k++)
  {
    for(j=0;j<n;j++)
    {
	temp= temp+a[i][j]*b[j][k];
    }
	c[i][k]=temp;
	temp = 0;
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for transpose of matrix

double **transpose(double **a,  int m, int n)
{
int i, j;
double **c;
//printf("I am here");
c = createMat(n,m);

 for(i=0;i<n;i++)
 {
  for(j=0;j<m;j++)
  {
c[i][j]= a[j][i];
//  printf("%lf ",c[i][j]);
  }
 }
return c;

}
//End function for transpose of matrix

//Defining the function for generating uniform random numbers
void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}
//End function for generating uniform random numbers

//Defining the function for calculating the mean of random numbers
double mean(char *str)
{
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
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}
//End function for calculating the mean of random numbers

//Defining the function for generating Gaussian random numbers
void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating Gaussian random numbers


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

//Defining the function for finding E(U^2)
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

//Defining the function for finding variance 
double variance(char *str) {
    double var = mean_U2(str) - mean(str)*mean(str);
    return var;
}

//Defining function to generate triangular random numbers
void triangular(char *str,int len) {
  int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
  double temp = 0;
  for(int j=0;j<2;j++) {
    temp = temp + (double)rand()/RAND_MAX;
  }
fprintf(fp,"%lf\n",temp);
}
fclose(fp);


}

//Defining function to generate bernoulli random variables
void bernoulli(char *str, int len) {
  int temp,val;
  FILE *fp;

  fp = fopen(str,"w");
  for(int i =0; i< len;i++) {
    temp = rand()%2;
    if(temp==0) {
      val = -1;
      fprintf(fp,"%d\n",val);
    }
    else {
      val = 1;
      fprintf(fp,"%d\n",val);
    }

  }

}

void Y_gen(char *str, int len,double a) {
  int i;
  FILE *fp;
  FILE *fp1;
  FILE *fp2;  
  double y,x,n;
  fp = fopen(str,"w");
  fp1 = fopen("gau.dat","r");
  fp2 = fopen("bernoulli.dat","r");

  //Generate numbers
  
  for(i=0;i<len;i++) {
      fscanf(fp1,"%lf",&n);
      fscanf(fp2,"%lf",&x);
      y = a*x + n;
      fprintf(fp,"%lf\n",y);
  }
    
  fclose(fp);
  fclose(fp1);
  fclose(fp2);

}

void X_cap_gen(char *str,int len) {
  int i;
  FILE *fp;
  FILE *fp1;
  FILE *fp2; 
  fp = fopen(str,"w");
  fp1 = fopen("Y_gen.dat","r");
  int val;
  double y;

    for(i=0;i<len;i++) {
    fscanf(fp1,"%lf",&y);

    if(y < 0) {
      val = -1;
      fprintf(fp,"%d\n", val);
    }
    else {
      val = 1;
      fprintf(fp,"%d\n", val);
    }
  }

  fclose(fp);
  fclose(fp1);


}

double Err_gen(int len) {
  int i;
  int counter1 = 0,counter2 = 0,counter3 = 0,counter4 = 0;
  int x,x_cap;
  FILE *fp1;
  FILE *fp2; 

  fp1 = fopen("bernoulli.dat","r");
  fp2 = fopen("X_cap_gen.dat","r");

  for(i=0;i<len;i++) {
    fscanf(fp1,"%d",&x);
    fscanf(fp2,"%d",&x_cap);

    if((x==1) && (x_cap==-1)) {
       counter1++;
       counter2++;
    }
    else if(x==1) {
      counter1++;
    }
    else if((x==-1)&&(x_cap==1)) {
       counter3++;
       counter4++;
    }
    else if(x==-1) {
      counter3++;
    }

  }

  //printf("%d %d %d %d\n",counter1,counter2,counter3,counter4);

  

  double prob_e_0 = counter2/(double)counter1;
  double prob_e_1 = counter4/(double)counter3;

  double ver = counter1 + counter3; 

  double prob_e = (prob_e_0 + prob_e_1)/2;

  printf("%lf\n",prob_e_0);
  printf("%lf\n",prob_e_1);
  //printf("%lf\n",prob_e);
  //printf("%lf\n",ver);

  fclose(fp1);
  fclose(fp2);

  return prob_e;

}

void Prob_err(char *str,int len) {
  FILE *fp;
  fp = fopen(str,"w");

  int i = 0;
  double a = 0.1;

  for(i=0;i<=len;i++) {
    Y_gen("Y_gen.dat",1000000,a*i);

    X_cap_gen("X_cap_gen.dat",1000000);

    double err = Err_gen(1000000);

    fprintf(fp,"%lf\n",err);

  }

}

//Defining function to generate sum of squares of gaussean random variables
void chi(char *str,int len) {
 int i,j;
double temp1,temp2;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
double temp1 = 0;
double temp2 = 0;
for (j = 0; j < 12; j++)
{
temp1 += (double)rand()/RAND_MAX;
temp2 += (double)rand()/RAND_MAX;
}
temp1-=6;
temp2-=6;
fprintf(fp,"%lf\n",(temp1*temp1 + temp2*temp2));
}
fclose(fp);


}

//Defining function to generate square root of V
void root_V(char *str,int len) {
 int i,j;
double temp1,temp2;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp1 = 0;
temp2 = 0;
for (j = 0; j < 12; j++)
{
temp1 += (double)rand()/RAND_MAX;
temp2 += (double)rand()/RAND_MAX;
}
temp1-=6;
temp2-=6;
fprintf(fp,"%lf\n",sqrt((temp1*temp1 + temp2*temp2)));
}
fclose(fp);


}


