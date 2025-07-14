# Social Media Post Scheduler

# List of post titles
posts = ["Morning Motivation", "Workout Tips", "Healthy Recipes"]

# Insert a priority post at the top
priority_post = input("Enter a priority post to insert at the top: ")
posts.insert(0, priority_post)

# Remove a posted item
posted = input("Enter the title of the post you've already posted: ")
if posted in posts:
    posts.remove(posted)
else:
    print("Post not found in the list.")

# Display all scheduled posts
print("\nScheduled Posts:")
for i, post in enumerate(posts):
    print(f"{i+1}. {post}")
