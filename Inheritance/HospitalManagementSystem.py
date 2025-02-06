from Doctor import Doctor
from Nurse import Nurse

class HospitalManagementSystem:
    def register_doctor(self, doctor: Doctor):
        doctor.display_details()

    def register_nurse(self, nurse: Nurse):
        nurse.display_details()