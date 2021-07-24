from utilities import Person


class Doctor(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']
        self.language = "English"
        self.speciality = kwargs['speciality']
        self.location = kwargs['location']
        self.contact = kwargs['contact']
        self.working_hrs = kwargs['working_hrs']
        self.rating = kwargs['rating']  # how can a doctor rate himself
        self.fee = kwargs['fee']

    def check_patient(self):
        """
        """
        pass

    def write_prescription(self):
        """
        """
        pass


class Prescription:
    def __init__(self, **kwargs):
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
        """
        availability of patient
        """
        pass

    def get_appointment(self):
        """
        """
        pass

    def buy_medicines(self):
        """
        """
        pass
