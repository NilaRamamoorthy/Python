# Book collections at different branches
branch_A_books = {"Python Basics", "Data Science 101", "Machine Learning", "AI Fundamentals"}
branch_B_books = {"AI Fundamentals", "Java Essentials", "Python Basics", "Cloud Computing"}
branch_C_books = {"Cyber Security", "Java Essentials", "Python Basics", "AI Fundamentals"}

# All available books across all branches (union)
all_books = branch_A_books.union(branch_B_books, branch_C_books)
print("All Available Books:", all_books)

# Common books in all branches (intersection)
common_books = branch_A_books.intersection(branch_B_books, branch_C_books)
print("Common Books in All Branches:", common_books)

# Books only in Branch A (not in B or C)
exclusive_to_A = branch_A_books.difference(branch_B_books.union(branch_C_books))
print("Books Only in Branch A:", exclusive_to_A)
