import json
import os

# Decorator to convert units
def unit_converter(func):
    def wrapper(self, *args, **kwargs):
        if self.unit == 'imperial':
            self.weight = self.weight * 0.453592  # Convert pounds to kilograms
            self.height = self.height * 0.0254  # Convert inches to meters
        result = func(self, *args, **kwargs)
        return result
    return wrapper

# Person class
class Person:
    def __init__(self, name, weight, height, unit='metric'):
        self.name = name
        self.weight = weight
        self.height = height
        self.unit = unit

    @unit_converter
    def calculate_bmi(self):
        if self.weight <= 0 or self.height <= 0:
            raise ValueError("Weight and height must be positive values.")
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def classify_bmi(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Normal weight'
        elif 25 <= bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obese'

    def health_risk(self):
        bmi_category = self.classify_bmi()
        if bmi_category == 'Underweight':
            return 'Malnutrition risk'
        elif bmi_category == 'Normal weight':
            return 'Low risk'
        elif bmi_category == 'Overweight':
            return 'Enhanced risk'
        else:
            return 'High risk'

    def to_dict(self):
        return {
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'unit': self.unit,
            'bmi': self.calculate_bmi(),
            'bmi_category': self.classify_bmi(),
            'health_risk': self.health_risk()
        }

# File handling functions
def save_bmi_history(people, filename='bmi_history.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append([person.to_dict() for person in people])

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_bmi_history(filename='bmi_history.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

# Generator to yield people in 'Obese' category
def obese_people(people):
    for person in people:
        if person.classify_bmi() == 'Obese':
            yield person

# Example usage
if __name__ == "__main__":
    # Create Person instances
    alice = Person('Alice', 70, 1.75)  # Metric units
    bob = Person('Bob', 154, 70, unit='imperial')  # Imperial units

    # List of people
    people = [alice, bob]

    # Save BMI history
    save_bmi_history(people)

    # Load and display BMI history
    history = load_bmi_history()
    for record in history:
        for person_data in record:
            print(person_data)

    # Display obese people
    print("\nObese individuals:")
    for person in obese_people(people):
        print(person.name)
