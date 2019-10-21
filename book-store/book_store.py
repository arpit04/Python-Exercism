#Popular books on the book store
#Each book price is $8
books = ['book1','book2','book3','book4','book5']

#===> Sets for customer <===
set1 = ['book1','book2','book3','book4','book5']
set2 = ['book1','book2','book3']

#discount list for set 1
discount1 = []
no_discount1 = []

#discount list for set 2
discount2 = []
no_discount2 = []

#===> algorithm for set 1 <===
for i in range(len(set1)):
    if set1[i] not in discount1:
        discount1.append(set1[i])
    else:
        no_discount1.append(set1[i]) 
print(discount1)

if len(discount1)==5:
    x = (25*8)/100
    price = 5*(8-x)
    print(price)

elif len(discount1)==4:
    x = (20*8)/100
    price = 4*(8-x)
    print(price)

elif len(discount1)==3:
    x = (10*8)/100
    price = 3*(8-x)
    print(price)

elif len(discount1)==2:
    x = (5*8)/100
    price = 2*(8-x)
    print(price)

print(no_discount1)
y = len(set1) - len(discount1)
price2 = 8 * y
print(price2)

final = price + price2
print("Total price of your book sets is :",final)

#===> algorithm for set 2 <===
for i in range(len(set2)):
    if set2[i] not in discount2:
        discount2.append(set2[i])
    else:
        no_discount2.append(set2[i]) 
print(discount2)

if len(discount2)==5:
    x = (25*8)/100
    price = 5*(8-x)
    print(price)

elif len(discount2)==4:
    x = (20*8)/100
    price = 4*(8-x)
    print(price)

elif len(discount2)==3:
    x = (10*8)/100
    price = 3*(8-x)
    print(price)

elif len(discount2)==2:
    x = (5*8)/100
    price = 2*(8-x)
    print(price)

print(no_discount2)
y = len(set2) - len(discount2)
price2 = 8 * y
print(price2)

final = price + price2
print("Total price of your book sets is :",final)