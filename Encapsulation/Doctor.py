class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization

    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        if isinstance(value, str):
            self.__doctor_id = value
        else:
            raise ValueError("Doctor ID must be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string")

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        if isinstance(value, str):
            self.__specialization = value
        else:
            raise ValueError("Specialization must be a string")
    
    def treat_patient(self, patient):
        print(f"Patient {patient.patient_id} treated for {patient.diagnosis} successfully.")
        



