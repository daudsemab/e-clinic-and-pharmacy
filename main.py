class Person:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.age = kwargs['age']

    def update_name(self):
        """
        """
        pass

    def update_password(self):
        """
        """
        pass

    def login(self):
        """
        """
        pass

    def signup(self):
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


class Doctor(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']
        self.language = kwargs['language']
        self.speciality = kwargs['speciality']
        self.location = kwargs['location']
        self.contact = kwargs['contact']
        self.working_hrs = kwargs['working_hrs']
        self.rating = kwargs['rating']
        self.fee = kwargs['fee']

    def write_prescription(self):
        """
        """
        pass

    def check_patient(self):
        """
        """
        pass


class Pharmacist(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']


class Pharmay:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.license_num = kwargs['license_num']


class ABC:      # testing
    pass
