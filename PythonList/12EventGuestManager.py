# Event Guest List Manager

# Initial guest list
guest_list = ["Anjali", "Ravi", "Priya"]

# Add a new guest
new_guest = input("Enter a guest name to add: ").strip().title()
guest_list.append(new_guest)

# Remove a guest
remove_guest = input("Enter a guest name to remove: ").strip().title()
if remove_guest in guest_list:
    guest_list.remove(remove_guest)
else:
    print(f"{remove_guest} is not in the guest list.")

# Print total guests
print(f"\nTotal Guests: {len(guest_list)}")

# Check if a guest is invited
check_guest = input("Enter a name to check invitation: ").strip().title()
if check_guest in guest_list:
    print(f"{check_guest} is invited.")
else:
    print(f"{check_guest} is not on the guest list.")

# Final guest list
print("\nFinal Guest List:")
for guest in guest_list:
    print(guest)
