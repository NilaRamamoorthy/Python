#16. Slug Generator for Blog Titles
str=input("Enter your blog title: ").strip().lower()
# str="Python  Basics for Beginners".lower().strip()
updated=str.replace(" ","-")
updated=updated.replace("--","-")
print(f"Generated Slug: {updated}")