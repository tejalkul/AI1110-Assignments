/*
Name : Tejal Kulkarni
Roll Number:CS21BTECH11058
Date: 29/03/2022

C code to find VAT paid by shopkeeper to government and total amount paid by customer(including tax) 
given marked price,discount for shopkeeper,discount for customer and sales tax
*/ 

#include<stdio.h>

//Finds the result to find percent of a number given percentage
int Percentage(int number,int percent)
{
    int result;
    result = (number*percent)/100;
    return result;
}

//Verification to get VAT paid by shopkeeper to government and amount paid by customer(including tax)
void Verification(int marked_price,int sales_tax,int disc_shopkeeper,int disc_customer)
{
    int selling_price_shopkeeper;
    int selling_price_customer;
    int discamount_shopkeeper;
    int discamount_customer;
    int tax_shopkeeper;
    int tax_customer;
    int VAT;
    int Amount_customer;

    discamount_shopkeeper = Percentage(marked_price,disc_shopkeeper);
    selling_price_shopkeeper = marked_price - discamount_shopkeeper;
    tax_shopkeeper = Percentage(selling_price_shopkeeper,sales_tax);

    discamount_customer = Percentage(marked_price,disc_customer);
    selling_price_customer = marked_price - discamount_customer;
    tax_customer = Percentage(selling_price_customer,sales_tax);

    VAT = tax_customer - tax_shopkeeper;
    printf("VAT paid to government by shopkeeper = Rs.%d\n",VAT);    //output

    Amount_customer = selling_price_customer + tax_customer;
    printf("Amount paid by customer inclusive of tax = Rs.%d\n",Amount_customer);    //output
    return;

}

int main()
{
      //input
      int marked_price = 45000;
      int sales_tax = 12;
      int disc_shopkeeper = 10;
      int disc_customer = 5;  

      Verification(marked_price,sales_tax,disc_shopkeeper,disc_customer);
      return 0;
}
