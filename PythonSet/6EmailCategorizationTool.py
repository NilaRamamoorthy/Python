# Sample email content with repeated tags
email_content = """
Hey team, please check the #projectupdate and #meetingnotes.
Make sure the #projectupdate is completed before the #deadline.
Don't forget the #teamwork and #collaboration!
"""

# Extract words starting with '#' using set comprehension
unique_tags = {word for word in email_content.split() if word.startswith('#')}

print("Unique Tags Found:", unique_tags)

# Display tags as a comma-separated string
tag_string = ", ".join(unique_tags)
print("Formatted Tag List:", tag_string)
