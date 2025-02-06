from Staff import Staff

class Nurse(Staff):
    def __init__(self, staff_id: str, name: str, department: str, shift: str, patients_assigned: int):
        super().__init__(staff_id, name, department)
        self.shift = shift
        self.patients_assigned = patients_assigned

    def display_details(self):
        print(f"Nurse ID: {self.staff_id}, Name: {self.name}, Department: {self.department}, "
              f"Shift: {self.shift}, Patients Assigned: {self.patients_assigned}")