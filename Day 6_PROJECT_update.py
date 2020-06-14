#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Fashion Store

products = {"Shirts": [300, 6], "Trousers": [500, 3],
            "Body Cream": [250, 7], "Jewelries": [400, 5],
            "Ladies Shoes": [700, 3], "Sunglasses": [600, 2],
            "Leather Belt": [450, 0], "Make Up kit": [1300,4],
            "Handbags": [900, 6], "Perfume": [1000, 2]}


# In[ ]:


# User data

print("Please provide your details below!")

f_name = input("First name: ").upper()
l_name = input("Last name: ").upper()
age = int(input("Age: "))
phone = input("Telephone number: ")
print()


# In[ ]:


count = 1
item_count = 0


if age < 18:
    print(f"Hi {f_name}, We are sorry you can't shop with us.")
    print("You need a guardian to come with you!!!")
else:
    print(f"Welcome {f_name},It is good to have you!")
    
    items = list(products.keys())
    
    
    print("Make you selection from the items display below:")
    print()
    print("S/N \t PRODUCTS \t PRICES \t QUANTITY")
    
    for i in list(products.values()):
        print(count, "\t", items[item_count], "\t", i[0], "\t\t", i[1])
        count += 1
        item_count += 1
        
    print()
    
        
    product = input("Product: ").title()
    qty = int(input("Quantity: "))
    
    
    if product in products:
        if (products[product][1] == 0):
            print("Sorry, the product is current not available!")
        elif (qty <= products[product][1]):
                total =  products[product][0] * qty
                print(f"Total Payable: {total}")
        else:
            print("We do not have up to that quantity!")
    else:
        print("No such Product!")
            


# In[ ]:


print(f"THANK YOU FOR PATRONIZING US, {l_name}. \nWe hope to see you again soon!")


# In[ ]:


print("You can enter more than one products and qty separated with comma!")

product = input("Product: ").title()
product = list(product.split(","))
print(product)

qty = input("Quantity: ")
qty = list(qty.split(","))
print(qty)

sum_total = 0
count = 0

for i in range(len(product)):
    if product[i] in products:
        if (products[product[i]][1] == 0):
            print(f"Product: {product[i]}\t Quantity: {qty[i]}\t = Not Available")
            
        elif (int(qty[i]) <= products[product[i]][1]):
            total =  products[product[i]][0] * int(qty[i])
            print(f"Product: {product[i]}\t Quantity: {qty[i]}\t = ${total}")
            
            sum_total += total
            
        else:
            print(f"Product: {product[i]}\t Quantity: {qty[i]}\t = Not Enough Quantity")
            
    else:
        print(f"Product: {product[i]}\t Quantity: {qty[i]}\t = No Such Product")
        
   
              
print(f"Total Payable: ${sum_total}")


# In[ ]:




