# Currency Converter

# Step 1: Ask the user for an amount in USD
usd = input("Enter amount in USD: ")

# Step 2: Show the type before conversion
print(f"\nBefore conversion: {usd} (Type: {type(usd)})")

# Step 3: Convert to float and apply the conversion rate
usd = float(usd)
inr = usd * 83  # Fixed rate: 1 USD = 83 INR

# Step 4: Print the result using an f-string
print(f"\n{usd} USD is equal to {inr} INR.")

# Step 5: Show the type after conversion
print(f"Type of inr: {type(inr)}")
