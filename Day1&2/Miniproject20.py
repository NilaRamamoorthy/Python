# Data Type Explorer

# Step 1: Ask the user to enter any value
value = input("Enter any value: ")

# Step 2: Print the value and its data type
print(f"\nYou entered: {value}")
print(f"Original type: {type(value)}")

# Step 3: Ask the user for the type to convert to
convert_type = input("\nConvert to which type? (int, float, bool, str): ")

# Step 4: Attempt to convert the value and show the result and new type
try:
    if convert_type == "int":
        converted = int(value)
    elif convert_type == "float":
        converted = float(value)
    elif convert_type == "bool":
        # Convert to bool (any non-empty string is True)
        converted = bool(value)
    elif convert_type == "str":
        converted = str(value)
    else:
        print("Invalid type selected.")
        converted = None

    # Step 5: Show the converted value and new type if conversion was successful
    if converted is not None:
        print(f"\nConverted value: {converted}")
        print(f"New type: {type(converted)}")

except ValueError as e:
    print(f"\nConversion failed: {e}")
