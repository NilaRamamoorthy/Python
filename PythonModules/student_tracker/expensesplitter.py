from expensesplitter.members import add_member, update_expense
from expensesplitter.report import display_report

def main():
    people = int(input("Enter number of people: "))
    for _ in range(people):
        name = input("Enter member name: ")
        add_member(name)

    print("Enter expenses (type 'done' to finish):")
    while True:
        name = input("Name: ")
        if name.lower() == 'done':
            break
        amount = float(input("Amount spent: ₹"))
        update_expense(name, amount)

    display_report()

if __name__ == "__main__":
    main()
