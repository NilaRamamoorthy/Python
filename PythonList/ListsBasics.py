# List Creation & Basic Operations (Tasks 1–10)

#1 Create a list of 5 student names and print it.
students_list=["priya","maya","meera","lia"]
print(students_list)

#2 Create a list with mixed data types (int, float, string, bool) and display each element.
mix_list=["Apple",11,18.89,True]
print(mix_list)

#3 Write a program to accept 5 numbers from the user and store them in a list.
numbers=[input("Enter a number: ") for i in range(5)]
print(numbers)

#4 Create an empty list and dynamically append 3 user inputs.
new_list=[]
new_list.append("apple")
new_list.append("orange")
new_list.append("grapes")
print(new_list)

#5 Write a program to create a list of 10 even numbers using a for loop.
numbers=[]
for num in range(19):
    if num%2==0:
        numbers.append(num)
print(numbers)
        
#6 Create two lists, one with integers and one with strings, then print them together.
number_list=[2,3,4,5,6]
string_list=["Apple","Orange","Grapes","Banana"]
print(number_list+string_list)

#7 Create a list of fruits and print only the first and last items using indexing.
fruits=["Apple","Orange","Grapes","Banana","Pineapple"]
print(f"First item in the list: {fruits[0]}")
print(f"Last item in the list: {fruits[-1]}")

#8 Use negative indexing to print the second-last item in a list.
print(f"Second last item in the list: {fruits[-2]}")

#9 Write a program to count the total number of elements in a list using len().
print(f"Number of items in the list is: {len(fruits)}")

#10 Check and print the data type of a created list.
print(f"Data Type of the list: {type(fruits)}")

# -------------------------------------------------------------------------------------------#
# Accessing & Indexing Tasks (11–15)


#11 Access and print each element of a list using a for loop with indexing.
fruits=["Apple","Orange","Banana","Grapes","Pineapple"]
for num in range(len(fruits)):
    print(fruits[num])

#12 Print every alternate item from a list using slicing.


#13 Create a list of cities and print the third character of the second city.

#14 Write a program to reverse a list using slicing.

#15 Access the last element of a list using both positive and negative indexing.


