from Encapsulation import Patient
from Encapsulation import Doctor

patient = Patient(patient_id="P001", name="John Smith", age=45, diagnosis="Fever")

doctor = Doctor(doctor_id="D101", name="Dr. Alice", specialization="General Medicine")

patient.diagnosis = "Flu"

doctor.treat_patient(patient)








