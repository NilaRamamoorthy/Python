# Define roles
admin_users = {"Alice", "Bob", "Charlie"}
editor_users = {"Bob", "Charlie"}
viewer_users = {"David", "Eve"}

# Check if all editors are also admins
if editor_users.issubset(admin_users):
    print("All editors are admins.")
else:
    print("Some editors are not admins.")

# Check if admin group contains all editor permissions
if admin_users.issuperset(editor_users):
    print("Admin has all editor access.")
else:
    print("Admin lacks some editor permissions.")

# Check if viewer and editor roles are disjoint (no overlaps)
if viewer_users.isdisjoint(editor_users):
    print("Viewers and editors are completely separate.")
else:
    print("There are users with both viewer and editor roles.")

# Add a conflicting user to both editor and viewer
editor_users.add("Eve")
print("\nUpdated Editor Users:", editor_users)
print("Updated Viewer Users:", viewer_users)

# Check disjoint status again
if viewer_users.isdisjoint(editor_users):
    print("Still disjoint.")
else:
    print("Conflict: Some users have both viewer and editor roles.")
