# Identity Operators Tasks (27–30)

# Task 27
list1 = [1, 2, 3]
list2 = list1  
print("list1 is list2:", list1 is list2)  
print("-" * 40)

# Task 28
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print("list3 == list4:", list3 == list4)      
print("list3 is not list4:", list3 is not list4)  
print("-" * 40)

# Task 29
a = 10
b = 10
print("a == b:", a == b)     
print("a is b:", a is b)      
a = "hello"
b = "hello"
print("a == b (str):", a == b)  
print("a is b (str):", a is b)  
print("-" * 40)

# Task 30
x = [5, 6, 7]
y = x
z = [5, 6, 7]

print("x is y:", x is y)       
print("x is z:", x is z)        
print("y is not z:", y is not z)  # True
print("-" * 40)
