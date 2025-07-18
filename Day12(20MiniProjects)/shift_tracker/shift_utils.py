# shift_utils.py

# Available shift types
available_shifts = {"Morning", "Afternoon", "Night"}

# Dictionary to track shift assignment with (employee ID) as key
shift_schedule = {}

# Set to track all unique shifts assigned
assigned_shifts = set()

def assign_shift(emp_id, name, shift_type):
    if shift_type not in available_shifts:
        print(f"Invalid shift type: {shift_type}")
        return

    if emp_id in shift_schedule:
        print(f"Employee {name} already assigned to a shift.")
        return

    shift_schedule[emp_id] = {
        "name": name,
        "shift": shift_type
    }
    assigned_shifts.add(shift_type)
    print(f"Shift '{shift_type}' assigned to employee '{name}'.")

def display_shifts():
    print("\nShift Assignments:")
    for emp_id, details in shift_schedule.items():
        print(f"Employee ID: {emp_id}, Name: {details['name']}, Shift: {details['shift']}")
    
    print("\nUnique shifts assigned:", assigned_shifts)
