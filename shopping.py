# If cart total exceeds $200, apply a flat $10 discount on the cart total.
def flat_10_discount(cartTotal):
    return cartTotal - 10.0

# If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
def bulk_5_discount(priceofProduct):
    return priceofProduct * (5 / 100)

# If total quantity exceeds 20 units, apply a 10% discount on the cart total.
def bulk_10_discount(cartTotal):
    return cartTotal * (10 / 100)

# If total quantity exceeds 30 units & any single product quantity greater than 15, 
# then apply a 50% discount on products which are above  15 quantity.
# The first 15 quantities have the original price and units above 15 will get a 50% discount.
def tiered_50_discount(priceofDiscountProduct):
    return priceofDiscountProduct * (50/100)

def applyDiscount():
    # dictionary to store the discount values with its discount name. {discount name : discount price}
    discount = {}

    # rule 1
    if cartTotal > 200:
        flat_10_discount_bill = flat_10_discount(cartTotal)
        discount["flat_10_discount"] = flat_10_discount_bill
    # rule 2
    if(quantityOfProductA > 10) or (quantityOfProductB > 10) or (quantityOfProductC > 10):
        bulk_5_discount_bill_A = 0
        bulk_5_discount_bill_B = 0
        bulk_5_discount_bill_C = 0
        if(quantityOfProductA > 10):
            bulk_5_discount_bill_A = bulk_5_discount(totalAmountOfA)
        if(quantityOfProductB > 10):
            bulk_5_discount_bill_B = bulk_5_discount(totalAmountOfB)
        if(quantityOfProductC > 10):
            bulk_5_discount_bill_C = bulk_5_discount(totalAmountOfC)
        bulk_5_discount_bill = cartTotal - bulk_5_discount_bill_A - bulk_5_discount_bill_B - bulk_5_discount_bill_C
        discount["bulk_5_discount"] = bulk_5_discount_bill
    # rule 3
    if(totalQuantity > 20):
        bulk_10_discount_bill = cartTotal - bulk_10_discount(cartTotal)
        discount["bulk_10_discount"] = bulk_10_discount_bill
    # rule 4
    if(totalQuantity > 30):
        tiered_50_discount_amount_A = 0
        tiered_50_discount_amount_B = 0 
        tiered_50_discount_amount_C = 0
        if(quantityOfProductA > 15):
            remainingQuantity = quantityOfProductA - 15
            costOf15ProductA = 15 * catalog.get("Product A")
            tiered_50_discount_amount_A = (remainingQuantity * catalog.get("Product A")) - tiered_50_discount(remainingQuantity * catalog.get("Product A"))
            tiered_50_discount_bill_A = costOf15ProductA + tiered_50_discount_amount_A
        else:
            tiered_50_discount_bill_A = quantityOfProductA * catalog.get("Product A")
        if(quantityOfProductB > 15):
            remainingQuantity = quantityOfProductB - 15
            costOf15ProductB = 15 * catalog.get("Product B")
            tiered_50_discount_amount_B = (remainingQuantity * catalog.get("Product B")) - tiered_50_discount(remainingQuantity * catalog.get("Product B"))
            tiered_50_discount_bill_B = costOf15ProductB + tiered_50_discount_amount_B
        else:
            tiered_50_discount_bill_B = quantityOfProductB * catalog.get("Product B")
        if(quantityOfProductC > 15):
            remainingQuantity = quantityOfProductC - 15
            costOf15ProductC = 15 * catalog.get("Product C")
            tiered_50_discount_amount_C = (remainingQuantity * catalog.get("Product C")) - tiered_50_discount(remainingQuantity * catalog.get("Product C"))
            tiered_50_discount_bill_C = costOf15ProductC + tiered_50_discount_amount_C
        else:
            tiered_50_discount_bill_C = quantityOfProductC * catalog.get("Product C")
        tiered_50_discount_bill = tiered_50_discount_bill_A + tiered_50_discount_bill_B + tiered_50_discount_bill_C
        discount["tiered_50_discount"] = tiered_50_discount_bill
        print(discount)
    return discount

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

def display(discount):
    print("\nProduct Name\tQuantity\tTotal Amount of that Product")
    print(f"Product A\t{quantityOfProductA}\t\t${totalAmountOfA}")
    print(f"Product B\t{quantityOfProductB}\t\t${totalAmountOfB}")
    print(f"Product C\t{quantityOfProductC}\t\t${totalAmountOfC}")
    print(f"\nSubTotal              : ${cartTotal}")
    # Minimum Bill is beneficial to the customer
    beneficialDiscount = min(discount, key = discount.get)
    print(f"Discount Name Applied : {beneficialDiscount}")
    print(f"Discount Amount       : ${cartTotal - discount[beneficialDiscount]}")
    print(f"Amount after discount : ${discount[beneficialDiscount]}")
    shipFee = shipping()
    giftWrapFee = giftWrap()
    print(f"Shipping Fee          : ${shipFee}")
    print(f"Gift Wrap Fee         : ${giftWrapFee}")
    totalAmount = discount[beneficialDiscount] + shipFee + giftWrapFee
    print(f"Total                 : ${totalAmount}")

# ------------------------------------------------------------------------------------------------
# Defining a dictionary of catalog "Product Name : Price"
catalog = {
    "Product A" : 20.0,
    "Product B" : 40.0,
    "Product C" : 50.0
}

print("\nProducts and their Price")

for product, price in catalog.items():
    print(f"{product} : ${price}")

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

totalAmountOfA = catalog.get("Product A") * quantityOfProductA
totalAmountOfB = catalog.get("Product B") * quantityOfProductB
totalAmountOfC = catalog.get("Product C") * quantityOfProductC

# total amount in cart
cartTotal = totalAmountOfA + totalAmountOfB + totalAmountOfC

# total quantity of products
totalQuantity = quantityOfProductA + quantityOfProductB + quantityOfProductC
discount = applyDiscount()

# display the bill
print("\nBill:")
display(discount)
