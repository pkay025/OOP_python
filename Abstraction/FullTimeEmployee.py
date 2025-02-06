from Employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: str, salary: float):
        super().__init__(name, employee_id)
        self._salary = salary

    def get_salary(self) -> float:
        return self._salary

    def calculate_pay(self) -> str:
        return f"FullTimeEmployee Pay: {self._salary}"

#instance of FullTimeEmployee object
if __name__ == "__main__":
    ft_employee = FullTimeEmployee("Paakow Emma", "FT025", 90000)
    print(ft_employee.calculate_pay())
