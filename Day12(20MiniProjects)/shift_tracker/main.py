# main.py

from shift_utils import assign_shift, display_shifts

# Assign shifts to employees
assign_shift((201,), "Alice", "Morning")
assign_shift((202,), "Bob", "Night")
assign_shift((203,), "Charlie", "Evening")  # Invalid shift
assign_shift((201,), "Alice", "Afternoon")  # Duplicate employee

# Display assigned shifts
display_shifts()
