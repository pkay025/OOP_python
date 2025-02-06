class Staff:
    def __init__(self, staff_id: str, name: str, department: str):
        self.staff_id = staff_id
        self.name = name
        self.department = department

    def display_details(self):
        print(f"Staff ID: {self.staff_id}, Name: {self.name}, Department: {self.department}")