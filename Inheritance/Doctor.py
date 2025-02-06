from Staff import Staff

class Doctor(Staff):
    def __init__(self, staff_id: str, name: str, department: str, specialization: str, years_of_experience: int):
        super().__init__(staff_id, name, department)
        self.specialization = specialization
        self.years_of_experience = years_of_experience

    def display_details(self):
        print(f"Doctor ID: {self.staff_id}, Name: {self.name}, Department: {self.department}, "
              f"Specialization: {self.specialization}, Experience: {self.years_of_experience} years")