# Members of two book clubs
fiction_club = {"Alice", "Bob", "Charlie", "David"}
nonfiction_club = {"Charlie", "David", "Eva", "Frank"}

# Find members who are in both clubs
both_clubs = fiction_club.intersection(nonfiction_club)
print("Members in both clubs:", both_clubs)

# Members in only one of the two clubs
exclusive_members = fiction_club.symmetric_difference(nonfiction_club)
print("Members exclusive to one club:", exclusive_members)

# All book club members combined
all_members = fiction_club.union(nonfiction_club)
print("All book club members:", all_members)
