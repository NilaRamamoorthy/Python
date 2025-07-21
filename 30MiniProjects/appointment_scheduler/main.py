from scheduler import add_appointment, edit_appointment, remove_appointment, display_schedule, appointments, people
from notifier import notify_upcoming

# Add sample appointments
add_appointment("2025-07-22", "10:00", "Dr. Smith", "Dental Checkup")
add_appointment("2025-07-22", "15:00", "John Doe", "Team Meeting")
add_appointment("2025-07-23", "09:30", "Anna Lee", "Interview")

# Display all
print("Current Appointments:")
display_schedule()

# Edit example
edit_appointment("2025-07-22", "15:00", new_time="16:00")

# Remove one
remove_appointment("2025-07-23", "09:30")

# Display again
print("\nUpdated Appointments:")
display_schedule()

# Notify today
notify_upcoming(appointments, "2025-07-22")

# Show people involved
print("\nPeople involved:", people)
