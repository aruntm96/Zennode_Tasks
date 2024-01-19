# If cart total exceeds $200, apply a flat $10 discount on the cart total.
def flat_10_discount():
    return cartTotal - 10

def bulk_5_discount(priceofProduct):
    return priceofProduct * (5 / 100)
     
def bulk_10_discount():
    bill = cartTotal * (10 / 100)
    return bill

def tiered_50_discount():
    bill = price * (50/100)
    return bill

def applyDiscount():
    # rule 1
    if cartTotal > 200:
        discountName = "flat_10_discount"
        flat_10_discount_bill = flat_10_discount()
        print(f"flat_10_discount_bill: {flat_10_discount_bill}")
    # rule 2
    if(quantityOfProductA > 10) or (quantityOfProductB > 10) or (quantityOfProductC > 10):
        discountName = "bulk_5_discount"
        bulk_5_discount_billA = 0
        bulk_5_discount_billB = 0
        bulk_5_discount_billC = 0
        if(quantityOfProductA > 10):
            bulk_5_discount_billA = bulk_5_discount(totalAmountOfA)
        if(quantityOfProductB > 10):
            bulk_5_discount_billB = bulk_5_discount(totalAmountOfB)
        if(quantityOfProductC > 10):
            bulk_5_discount_billC = bulk_5_discount(totalAmountOfC)
        bulk_5_discount_bill = totalAmountOfA + totalAmountOfB + totalAmountOfC - bulk_5_discount_billA - bulk_5_discount_billB - bulk_5_discount_billC 
        print(bulk_5_discount_bill)

    # if(totalQuantity > 20):
    #     bulk_10_discount()
    # elif(totalQuantity > 30):
    #     if(quantityOfProductA > 15):
    #         tiered_50_discount()
    #     if(quantityOfProductB > 15):
    #         tiered_50_discount()
    #     if(quantityOfProductC > 15):
    #         tiered_50_discount()
    

def display():
    print("\nProduct Name\tQuantity\tTotal Amount of that Product")
    print(f"Product A\t{quantityOfProductA}\t\t{totalAmountOfA}")
    print(f"Product B\t{quantityOfProductB}\t\t{totalAmountOfB}")
    print(f"Product C\t{quantityOfProductC}\t\t{totalAmountOfC}")

# ------------------------------------------------------------------------------------------------
# Defining a dictionary of catalog "Product Name : Price"
catalog = {
    "Product A" : 20,
    "Product B" : 40,
    "Product C" : 50
}

print("\nProducts and their Price\n")

for product, price in catalog.items():
    print(f"{product} : ${price}")

while(True):
    quantityOfProductA = int(input("Enter the quantity of product 'Product A': "))
    quantityOfProductB = int(input("Enter the quantity of product 'Product B': "))
    quantityOfProductC = int(input("Enter the quantity of product 'Product C': "))

    isWrapped = input("Want to wrap as gift (yes / no)? ")

    if (quantityOfProductA > 0 and quantityOfProductB > 0 and quantityOfProductC > 0) and (isWrapped == 'yes' or isWrapped == 'no'):
        break
    else:
        print("Invalid inputs. Try again!")

totalAmountOfA = catalog.get("Product A") * quantityOfProductA
totalAmountOfB = catalog.get("Product B") * quantityOfProductB
totalAmountOfC = catalog.get("Product C") * quantityOfProductC

# total amount in cart
cartTotal = totalAmountOfA + totalAmountOfB + totalAmountOfC
print(f"cart total : {cartTotal}")
billWithDiscount = applyDiscount()
# display()
