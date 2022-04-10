#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 10/04/2022

#Python code to find VAT paid by shopkeeper to government and total amount paid by customer(including tax) 
#given marked price,discount for shopkeeper,discount for customer and sales tax
 
def percentage(number,percent):
    result = number*percent/100
    return result


def verification(marked_price,sales_tax,disc_shopkeeper,disc_customer):
    discamount_shopkeeper = percentage(marked_price,disc_shopkeeper)      
    selling_price_shopkeeper = marked_price - discamount_shopkeeper           
    tax_shopkeeper = percentage(selling_price_shopkeeper,sales_tax)

    discamount_customer = percentage(marked_price,disc_customer)
    selling_price_customer = marked_price - discamount_customer
    tax_customer = percentage(selling_price_customer,sales_tax)

    VAT = tax_customer - tax_shopkeeper
    print(f"VAT paid to government by shopkeeper = Rs.{int(VAT)}")    #output

    Amount_customer = selling_price_customer + tax_customer
    print(f"Amount paid by customer inclusive of tax = Rs.{int(Amount_customer)}")    #output



#input
marked_price = 45000
sales_tax = 12
disc_shopkeeper = 10      #Discount for shopkeeper
disc_customer = 5         #Discount for customer

verification(marked_price,sales_tax,disc_shopkeeper,disc_customer)
