# 14. Text Highlighter
paragraph=input("Enter the paragraph: ").strip()
keyword=input("Enter the keyword: ").lower()
count=paragraph.count(keyword)
paragraph=paragraph.replace(keyword,keyword.upper())
print(paragraph)
print(f"The keyword has appeared {count} times")
