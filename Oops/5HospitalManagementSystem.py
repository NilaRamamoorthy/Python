from abc import ABC, abstractmethod
from datetime import datetime

# Abstract base class
class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self._id = person_id  # encapsulated

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name} (ID: {self._id})"

# Doctor class
class Doctor(Person):
    def __init__(self, name, doctor_id, specialization):
        super().__init__(name, doctor_id)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

    def prescribe(self, patient, medicine):
        return Prescription(self, patient, medicine)

# Patient class
class Patient(Person):
    def __init__(self, name, patient_id, age):
        super().__init__(name, patient_id)
        self.age = age
        self.medical_history = []

    def get_role(self):
        return "Patient"

    def add_history(self, record):
        self.medical_history.append(record)

# Appointment class (aggregation)
class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment: {self.patient.name} with Dr. {self.doctor.name} on {self.date_time.strftime('%d-%m-%Y %H:%M')}"

# Prescription class
class Prescription:
    def __init__(self, doctor, patient, medicine):
        self.doctor = doctor
        self.patient = patient
        self.medicine = medicine
        self.date = datetime.now()

    def __str__(self):
        return (f"Prescription\n"
                f"Doctor   : {self.doctor.name} ({self.doctor.specialization})\n"
                f"Patient  : {self.patient.name}\n"
                f"Medicine : {self.medicine}\n"
                f"Date     : {self.date.strftime('%d-%m-%Y')}")

if __name__ == "__main__":
    # Create doctor and patient
    doc1 = Doctor("Dr. Aarthi", "D001", "Pediatrics")
    pat1 = Patient("Nila", "P001", 10)

    # Create an appointment
    appointment = Appointment(pat1, doc1, datetime(2025, 7, 23, 10, 30))

    # Doctor prescribes medicine
    prescription = doc1.prescribe(pat1, "Paracetamol 250mg")

    # Patient adds to medical history
    pat1.add_history("Visited on 23-Jul-2025 for fever.")

    # Display
    print(appointment)
    print("\n" + str(prescription))

    print("\nMedical History:")
    for record in pat1.medical_history:
        print("-", record)
