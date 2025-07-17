# SKU list from warehouse (may contain duplicates)
sku_list = ["SKU001", "SKU002", "SKU003", "SKU002", "SKU004", "SKU005", "SKU003"]

# Convert to set to remove duplicates
unique_skus = set(sku_list)

# Check if duplicates exist by comparing lengths
if len(sku_list) != len(unique_skus):
    print("Duplicate SKUs found.")
    # Find duplicates manually
    seen = set()
    duplicates = set()
    for sku in sku_list:
        if sku in seen:
            duplicates.add(sku)
        else:
            seen.add(sku)
    print("Duplicate SKUs:", duplicates)
else:
    print("No duplicates in SKU list.")

# Final clean SKU list (no duplicates)
clean_skus = list(unique_skus)
print("Cleaned SKU List:", clean_skus)
