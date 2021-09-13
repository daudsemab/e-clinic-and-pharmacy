# required data imported from utilities
from utilities import Person, Date, Time, Diagnosis, input_integer


class Doctor(Person):
    appointments = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']
        self.language = "English"
        self.speciality = kwargs['speciality']
        self.location = kwargs['location']
        self.contact = kwargs['contact']
        self.working_hrs = kwargs['working_hrs']
        self.rating = kwargs['rating']
        self.fee = kwargs['fee']

    def diagnosis(self, list_name, numb1):
        disease = list_name[numb1][1]
        return disease

    def check_patient(self):
        common_symptoms = ["Flu", "Headache", "Blurry vision", "Chest tightness"]
        print(common_symptoms)
        first_symptom = input_integer("Which symptom do you have i.e, 0, 1, 2, 3 ")
        (flue, head_ache, blurry_vision, chest_tightness) = Diagnosis.disease_and_symptoms_data()  # unpacking tuple
        disease = None
        if first_symptom == 0:
            for symptoms in flue:
                print(symptoms[0][0])
            specific_symptoms = input_integer("Enter the pair which contain your symptoms i.e, 0,1,2")
            disease = self.diagnosis(flue, specific_symptoms) # calling function
        elif first_symptom == 1:
            for symptoms in head_ache:
                print(symptoms[0][0])
            specific_symptoms = input_integer("Enter the pair which contain your symptoms i.e, 0,1,2")
            disease = self.diagnosis(head_ache, specific_symptoms)
        elif first_symptom == 2:
            for symptoms in blurry_vision:
                print(symptoms[0][0])
            specific_symptoms = input_integer("Enter the pair which contain your symptoms i.e, 0,1,2")
            disease = self.diagnosis(blurry_vision, specific_symptoms)
        elif first_symptom == 3:
            for symptoms in chest_tightness:
                print(symptoms[0][0])
            specific_symptoms = input_integer("Enter the pair which contain your symptoms i.e, 0,1,2")
            disease = self.diagnosis(chest_tightness, specific_symptoms)
        return disease
    """This method will check for the symptoms and will return the name of disease"""

    def write_prescription(self):
        """
        """
        pass


class Patient(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prescription = [kwargs['prescription']]
        self.sickness = kwargs['sickness']
        self.family_code = kwargs['family_code']
        self.acc_amount = kwargs['acc_amount']

    def get_checkup(self):
        print('Remainder!!! Appointment for check up')
    """
    When the time of checkup arrives the patient will get the remainder of his appointment in accordance
    with the date and time he/she entered while taking appointment
    """

    @classmethod
    def get_appointment(cls):
        date = Date.add_date()
        time = Time()
        appointment_details = []
        condition = None
        for dates in Doctor.appointments[0]:
            if dates.day == date.day and dates.month == date.month and dates.year == date.year:
                condition = "check time"
        if condition == "check time":
            for times in Doctor.appointments[1]:
                if times.hour == time.hour and times.minute == time.minute:
                    return False
        else:
            appointment_details.append(date)
            appointment_details.append(time)
            Doctor.appointments.append(appointment_details)

    """
    The method "get_appointment" will check the validity of the new appointment's date and time to avoid 
    any type of conflict
    """

    def buy_medicines(self):
        """
        """
        pass

