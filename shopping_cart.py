# discount 1 - flat_10_discount
def flat_10_discount():
    return 10.0

# discount 2 - bulk_5_discount
def bulk_5_discount(priceOfProduct):
    return priceOfProduct * (5 / 100)

# discount 3 - bulk_10_discount
def bulk_10_discount(cartTotal):
    return cartTotal * (10 / 100)

# discount 4 - tiered_50_discount
def tiered_50_discount(priceOfDiscountProduct):
    return priceOfDiscountProduct * (50/100)

def applyDiscount():
    # dictionary to store the discount values with its discount name. {discount name : discount price}
    discountAmounts = {}

    # check flat_10_discount
    if cartTotal > 200:
        flat_10_discount_amount = flat_10_discount()
        discountAmounts["flat_10_discount"] = flat_10_discount_amount
    # check bulk_5_discount
    if(quantityOfProductA > 10) or (quantityOfProductB > 10) or (quantityOfProductC > 10):
        bulk_5_discount_amount_A = 0
        bulk_5_discount_amount_B = 0
        bulk_5_discount_amount_C = 0
        if(quantityOfProductA > 10):
            bulk_5_discount_amount_A = bulk_5_discount(totalAmountOfProductA)
        if(quantityOfProductB > 10):
            bulk_5_discount_amount_B = bulk_5_discount(totalAmountOfProductB)
        if(quantityOfProductC > 10):
            bulk_5_discount_amount_C = bulk_5_discount(totalAmountOfProductC)
        bulk_5_discount_amount = bulk_5_discount_amount_A + bulk_5_discount_amount_B + bulk_5_discount_amount_C
        discountAmounts["bulk_5_discount"] = bulk_5_discount_amount
    # check bulk_10_discount
    if(totalQuantity > 20):
        bulk_10_discount_amount = bulk_10_discount(cartTotal)
        discountAmounts["bulk_10_discount"] = bulk_10_discount_amount
    # check tiered_50_discount
    if(totalQuantity > 30):
        tiered_50_discount_amount_A = 0
        tiered_50_discount_amount_B = 0 
        tiered_50_discount_amount_C = 0
        if(quantityOfProductA > 15):
            remainingQuantity = quantityOfProductA - 15
            tiered_50_discount_amount_A = (remainingQuantity * catalog.get("Product A")) - tiered_50_discount(remainingQuantity * catalog.get("Product A"))
        if(quantityOfProductB > 15):
            remainingQuantity = quantityOfProductB - 15
            tiered_50_discount_amount_B = (remainingQuantity * catalog.get("Product B")) - tiered_50_discount(remainingQuantity * catalog.get("Product B"))
        if(quantityOfProductC > 15):
            remainingQuantity = quantityOfProductC - 15
            tiered_50_discount_amount_C = (remainingQuantity * catalog.get("Product C")) - tiered_50_discount(remainingQuantity * catalog.get("Product C"))
        tiered_50_discount_amount = tiered_50_discount_amount_A + tiered_50_discount_amount_B + tiered_50_discount_amount_C
        discountAmounts["tiered_50_discount"] = tiered_50_discount_amount
    return discountAmounts

def giftWrap():
    if(isWrapped == "yes"):
        wrapAmount = totalQuantity * 1.0
    elif(isWrapped == "no"):
        wrapAmount = 0.0   
    return wrapAmount

def shipping():
    # 10units = 1 package
    unitsPerPackage = 10
    package = totalQuantity // unitsPerPackage
    remainingUnits = totalQuantity % unitsPerPackage
    if remainingUnits > 0 and remainingUnits <= unitsPerPackage:
        package = package + 1
    shippingFee = package * 5.0
    return shippingFee

def display(discountAmounts):
    print("\nProduct Name\tQuantity\tTotal Amount of that Product")
    print(f"Product A\t{quantityOfProductA}\t\t${totalAmountOfProductA:.2f}")
    print(f"Product B\t{quantityOfProductB}\t\t${totalAmountOfProductB:.2f}")
    print(f"Product C\t{quantityOfProductC}\t\t${totalAmountOfProductC:.2f}")
    print(f"\nSubTotal              : ${cartTotal:.2f}")
    # Minimum discount amount is beneficial to the customer
    beneficialDiscount = max(discountAmounts, key = discountAmounts.get)
    print(f"Discount Name Applied : {beneficialDiscount}")
    print(f"Discount Amount       : ${discountAmounts[beneficialDiscount]:.2f}")
    shipFee = shipping()
    giftWrapFee = giftWrap()
    print(f"Shipping Fee          : ${shipFee:.2f}")
    print(f"Gift Wrap Fee         : ${giftWrapFee:.2f}")
    totalAmount = cartTotal - discountAmounts[beneficialDiscount] + shipFee + giftWrapFee
    print(f"Total                 : ${totalAmount:.2f}")

# Defining a dictionary of catalog "Product Name : Price"
catalog = {
    "Product A" : 20.0,
    "Product B" : 40.0,
    "Product C" : 50.0
}

print("\nProducts and their Price")

for product, price in catalog.items():
    print(f"{product} : ${price:.2f}")

while(True):
    quantityOfProductA = int(input("Enter the quantity of product 'Product A': "))
    quantityOfProductB = int(input("Enter the quantity of product 'Product B': "))
    quantityOfProductC = int(input("Enter the quantity of product 'Product C': "))
    isWrapped = input("Want to wrap as gift (yes / no)? ")
    # Validating the inputs so that negative values are not valid
    if (quantityOfProductA >= 0 and quantityOfProductB >= 0 and quantityOfProductC >= 0) and (isWrapped.lower() == 'yes' or isWrapped.lower() == 'no'):
        break
    else:
        print("Invalid inputs. Try again!")

totalAmountOfProductA = catalog.get("Product A") * quantityOfProductA
totalAmountOfProductB = catalog.get("Product B") * quantityOfProductB
totalAmountOfProductC = catalog.get("Product C") * quantityOfProductC

# total amount in cart
cartTotal = totalAmountOfProductA + totalAmountOfProductB + totalAmountOfProductC

# total quantity of products
totalQuantity = quantityOfProductA + quantityOfProductB + quantityOfProductC
discountAmounts = applyDiscount()

# display the invoice
print("\nInvoice:")
display(discountAmounts)
