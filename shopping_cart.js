// Import propt-sync for User-Input
const prompt = require("prompt-sync")();

// declaring the discount amount to null
let flat_10_discount_amount = null;
let bulk_5_discount_amount = null;
let bulk_10_discount_amount = null;
let tiered_50_discount_amount = null;

//  discount 1 - flat_10_discount
const flat_10_discount = () => {
    return 10.0;
};
// discount 2 - bulk_5_discount
const bulk_5_discount = (priceOfProduct) => {
    return parseFloat(priceOfProduct * (5 / 100));
};
// discount 3 - bulk_10_discount
const bulk_10_discount = (cartTotal) => {
    return parseFloat(cartTotal * (10 / 100));
};
// discount 4 - tiered_50_discount
const tiered_50_discount = (priceOfDiscountProduct) => {
    return parseFloat(priceOfDiscountProduct * (50/100));
};

const applyDiscount = () => {
    const discountAmounts = new Map();
    //  check flat_10_discount
    if (cartTotal > 200){
        flat_10_discount_amount = flat_10_discount();
        discountAmounts.set("flat_10_discount",flat_10_discount_amount);
    }
    // check bulk_5_discount
    if((quantityOfProductA > 10) || (quantityOfProductB > 10) || (quantityOfProductC > 10)){
        let bulk_5_discount_amount_A = null;
        let bulk_5_discount_amount_B = null;
        let bulk_5_discount_amount_C = null;
        if(quantityOfProductA > 10){
            bulk_5_discount_amount_A = bulk_5_discount(totalAmountOfProductA);
        }
        if(quantityOfProductB > 10){
            bulk_5_discount_amount_B = bulk_5_discount(totalAmountOfProductB);
        }
        if(quantityOfProductC > 10){
            bulk_5_discount_amount_C = bulk_5_discount(totalAmountOfProductC);
        }
        bulk_5_discount_amount = bulk_5_discount_amount_A + bulk_5_discount_amount_B + bulk_5_discount_amount_C;
        discountAmounts.set("bulk_5_discount", bulk_5_discount_amount);
    }
    // check bulk_10_discount
    if(totalQuantity > 20){
        bulk_10_discount_amount = bulk_10_discount(cartTotal);
        discountAmounts.set("bulk_10_discount", bulk_10_discount_amount);
    }
    // check tiered_50_discount
    if(totalQuantity > 30){
        let tiered_50_discount_amount_A = null;
        let tiered_50_discount_amount_B = null;
        let tiered_50_discount_amount_C = null;
        if(quantityOfProductA > 15){
            let remainingQuantity = quantityOfProductA - 15;
            tiered_50_discount_amount_A = (remainingQuantity * catalog.get("Product A")) - tiered_50_discount(remainingQuantity * catalog.get("Product A"));
        }
        if(quantityOfProductB > 15){
            let remainingQuantity = quantityOfProductB - 15;
            tiered_50_discount_amount_B = (remainingQuantity * catalog.get("Product B")) - tiered_50_discount(remainingQuantity * catalog.get("Product B"));
        }
        if(quantityOfProductC > 15){
            let remainingQuantity = quantityOfProductC - 15;
            tiered_50_discount_amount_C = (remainingQuantity * catalog.get("Product C")) - tiered_50_discount(remainingQuantity * catalog.get("Product C"));
        }
        tiered_50_discount_amount = tiered_50_discount_amount_A + tiered_50_discount_amount_B + tiered_50_discount_amount_C;
        discountAmounts.set("tiered_50_discount" ,tiered_50_discount_amount);
    }
    return discountAmounts;
};

// Minimum Discount amount is beneficial to the customer
const findBeneficialDiscount = (discountAmounts) => {
    let maxPrice = 0;
    let discountNameOfmaxPrice = null;
    for(const [name, price] of discountAmounts){
        if(price > maxPrice){
            maxPrice = price;
            discountNameOfmaxPrice = name;
        }
    }
    return {discountName : discountNameOfmaxPrice, discountPrice : maxPrice};
}

const shipping = () => {
    // 10units = 1 package
    let unitsPerPackage = 10
    let package = Math.floor(totalQuantity / unitsPerPackage);
    let remainingUnits = totalQuantity % unitsPerPackage;
    if((remainingUnits > 0) && (remainingUnits <= unitsPerPackage)){
        package = package + 1
    }
    let shippingFee = package * 5.0
    return shippingFee
};

const giftWrap = () => {
    if(isWrapped == "yes"){
        wrapAmount = totalQuantity * 1.0;
    }
    else if(isWrapped == "no"){
        wrapAmount = 0.0;
    }
    return wrapAmount
};

const display = (discountAmounts) => {
    console.log("\nProduct Name\tQuantity\tTotal Amount");
    console.log(`Product A\t${quantityOfProductA}\t\t$${totalAmountOfProductA.toFixed(2)}`);
    console.log(`Product B\t${quantityOfProductB}\t\t$${totalAmountOfProductB.toFixed(2)}`);
    console.log(`Product C\t${quantityOfProductC}\t\t$${totalAmountOfProductC.toFixed(2)}`);
    console.log(`\nSubTotal                : $${cartTotal.toFixed(2)}`);
    const beneficialDiscount = findBeneficialDiscount(discountAmounts);
    console.log(`Discount Name Appliced  : ${beneficialDiscount.discountName}`);
    console.log(`Discount Amount         : $${beneficialDiscount.discountPrice.toFixed(2)}`);
    const shipFee = shipping();
    const giftWrapFee = giftWrap();
    console.log(`Shipping Fee            : $${shipFee.toFixed(2)}`);
    console.log(`Gift Wrap Fee           : $${giftWrapFee.toFixed(2)}`);
    const totalAmount = cartTotal - beneficialDiscount.discountPrice + shipFee + giftWrapFee
    console.log(`Total                   : $${totalAmount.toFixed(2)}`)
};

// Defining a map for Product and its price
const catalog = new Map([
    ["Product A" , 20],
    ["Product B" , 40],
    ["Product C" , 50]
]);
    
console.log("\nProducts and their Price")

for(const [product, price] of catalog){
    console.log(`${product} : $${(price.toFixed(2))}`);
}

while(true){
    var quantityOfProductA = parseInt(prompt("Enter the quantity of product 'Product A': "));
    var quantityOfProductB = parseInt(prompt("Enter the quantity of product 'Product B': "));
    var quantityOfProductC = parseInt(prompt("Enter the quantity of product 'Product C': "));
    var isWrapped = prompt("Want to wrap as gift (yes / no)? ");

    // Validating the inputs so that negative values are not valid
    if ((quantityOfProductA >= 0 && quantityOfProductB >= 0 && quantityOfProductC >= 0) && (isWrapped.toLowerCase() == 'yes' || isWrapped.toLowerCase() == 'no')){
        break
    }
    else{
        console.log("Invalid inputs. Try again!")
    }  
}

const totalAmountOfProductA = catalog.get("Product A") * quantityOfProductA;
const totalAmountOfProductB = catalog.get("Product B") * quantityOfProductB;
const totalAmountOfProductC = catalog.get("Product C") * quantityOfProductC;

//  total amount in cart
const cartTotal = totalAmountOfProductA + totalAmountOfProductB + totalAmountOfProductC
//  total quantity of products
const totalQuantity = quantityOfProductA + quantityOfProductB + quantityOfProductC

const discountAmounts = applyDiscount();
// display the invoice
console.log("\nInvoice:")
display(discountAmounts)
