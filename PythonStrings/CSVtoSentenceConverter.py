#20. CSV to Sentence Converter
user_list=input("Enter 3 grocery items(seperated by comma): ").strip()
new_list=user_list.split(",")
print(f"You bought {new_list[0]}, {new_list[1]} and {new_list[2]}.")