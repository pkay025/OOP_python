from Encapsulation import Patient
from Encapsulation import Doctor

if __name__ == "__main__":
    patient = Patient("P001", "John Smith", 45, "Fever")

    doctor = Doctor("D101", "Dr. Alice", "General Medicine")

    
    patient.update_diagnosis("Flu")
    
    doctor.treat_patient(patient)



























