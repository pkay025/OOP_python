class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
     self.__patient_id = patient_id
     self.__name = name
     self.__age = age
     self.__diagnosis = diagnosis

    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    @property
    def name(self):
        return self.__name

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        if diagnosis and diagnosis.strip():
            self.__diagnosis = diagnosis
        else:
            print("Diagnosis cannot be empty")

    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis
        if new_diagnosis and new_diagnosis.strip():
            print(f"Diagnosis updated successfully to: {new_diagnosis}")











