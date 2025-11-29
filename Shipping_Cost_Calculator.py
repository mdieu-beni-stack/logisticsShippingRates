# Shipping cost Calculator

## Input package weight and shipping rate
weight = float(input("enter the package weight in kilograms:"))
rate = float(input('enter the shipping rate per kilogram:"))

## Calculae shipping cost
shipping_cost = weight*rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
