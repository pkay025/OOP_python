class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization

    @property
    def doctor_id(self):
        return self.__doctor_id
    @property
    def doctor_id(self):
        return self.__doctor_id

    @property
    def name(self):
        return self.__name

    @property
    def specialization(self):
        return self.__specialization
    
    def treat_patient(self, patient):
        print(f"Patient {patient.patient_id} treated for {patient.diagnosis} successfully.")
    





























