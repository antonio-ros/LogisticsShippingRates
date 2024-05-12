1. # Shipping Cost Calculator
2. ## Input package weight and shipping rate
3. weight = float(input("Enter the package weight in kilograms: "))
4. rate = float(input("Enter the shipping rate per kilogram: "))
5. ## Calculate shipping cost
6. shipping_cost = weight * rate
7. ## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
