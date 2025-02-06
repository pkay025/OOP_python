from Doctor import Doctor
from Nurse import Nurse
from HospitalManagementSystem import HospitalManagementSystem

# Create Staff Members
doctor1 = Doctor("S001", "Dr. Smith", "Cardiology", "Cardiology", 15)
doctor2 = Doctor("S002", "Dr. Lee", "Neurology", "Neurology", 8)
nurse1 = Nurse("S003", "Nurse Kelly", "Emergency", "Night", 5)

# Register and Display Staff Details
hms = HospitalManagementSystem()
hms.register_doctor(doctor1)
hms.register_doctor(doctor2)
hms.register_nurse(nurse1)