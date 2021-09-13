from utilities import Family, Person, input_integer, input_alpha, generate_code
import custom_exceptions


class Disease:
    diseases = []
    diseases_data = [
        {
            'name': "corona",
            'symptoms': ["flue", "fever", "dry cough", "weakness"],
            'is_bacterial': False,
            'is_viral': True,
            'is_fungal': False,
        },
        {
            'name': "pneumonia",
            'symptoms': ["flue", "fever", "shortage of breath", "loss of appetite"],
            'is_bacterial': True,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "influenza",
            'symptoms': ["flue", "fever"],
            'is_bacterial': False,
            'is_viral': True,
            'is_fungal': False
        },
        {
            'name': "migraine",
            'symptoms': ["headache", "one sided headache", "blurry vision"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "cluster headache",
            'symptoms': ["headache", "pain behind the eyes", "eyelid droop", "eye redness", "tears"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "sinus headache",
            'symptoms': ["headache", "pain in cheek bone", "forehead pain", "bridge of nose"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "stroke",
            'symptoms': ["headache", "sudden weakness", "loss of balance"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "diabetes",
            'symptoms': ["frequent urination", "tingling limbs", "feeling hungary"],
            'is_bacterial': False,
            'is_viral': True,
            'is_fungal': False
        },
        {
            'name': "optic neuritis",
            'symptoms': ["vision losing one eye", "pain around eye"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "asthma",
            'symptoms': ["chest tightness", "shortness of breath", "coughing"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        },
        {
            'name': "muscle strain",
            'symptoms': ["chest tightness", "tenderness", "swelling"],
            'is_bacterial': False,
            'is_viral': False,
            'is_fungal': False
        }
    ]

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.symptoms = kwargs['symptoms']
        self.is_bacterial = kwargs['is_bacterial']
        self.is_viral = kwargs['is_viral']
        self.is_fungal = kwargs['is_fungal']

    @classmethod
    def add_disease(cls, name: str, symptoms: list, bacterial: bool, viral: bool, fungal: bool):
        """
        This method takes different disease related information, makes disease's object and then appends the object of disease in list diseases
        :param name, symptoms, bacterial, viral, fungal
        :return object: It returns the object of disease
        """
        disease = cls(name=name, symptoms=symptoms, is_bacterial=bacterial, is_viral=viral, is_fungal=fungal)
        Disease.diseases.append(disease)
        return disease

    @staticmethod
    def read_disease_data():
        """
        This method reads and passes information of each disease(which is stored in the form of dictionary) to above class method
        the add_disease
        :param
        :return
        """
        for disease in Disease.diseases_data:
            Disease.add_disease(disease['name'], disease['symptoms'], disease['is_bacterial'], disease['is_viral'],
                                disease['is_fungal'])


# -------------------- PATIENT --------------------


class Patient(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prescriptions = []  # list of prescriptions (objects)
        self.diseases = []  # list of diseases (objects)

    @classmethod
    def create_self(cls):
        name = input_alpha("Name", "Enter Your Name: ")
        gender = input_alpha("Gender", "Enter Your Gender: ")
        age = input_integer("Enter Your Age: ")
        family = Family()
        return cls(name=name, gender=gender, age=age, family=family)

    def add_prescription(self, prescription: object):
        """
        This method takes object of prescription and then appends the object list of prescriptions
        :param prescription: object
        :return
        """
        self.prescriptions.append(prescription)

    def add_disease(self, disease):
        """
        This method takes of object of disease and then appends it to the list of disease
        :param disease: object
        :return
        """
        self.diseases.append(disease)

    @staticmethod
    def rate_doctor(doctor):
        while True:
            try:
                rating = float(input("Rate Doctor 0 to 5: "))
                if rating < 0 or rating > 5:
                    raise custom_exceptions.AmountExceedError('WARNING! Invalid Rating.')
                doctor.ratings.append(rating)
                break
            except ValueError:
                print("WARNING! Invalid Rating.")
                continue
            except Exception as e:
                print(e)
                continue

    @staticmethod
    def see_available_doctors() -> int:
        """
        This method displays the names followed by their speciality in a number list form of available doctors.
        :returns integer, the doctor number to visit his profile / see his further details
        """
        if doctors := Doctor.doctors:
            print('AVAILABLE DOCTORS ARE LISTED BELOW!')
            for idx, doctor in enumerate(doctors):
                print(idx + 1, end=': ')    # 1: Prof. Dr. Tanker (Heart Specialist)\n
                doctor.display_short()
            doctor_num = input_integer("Enter the Doctor ID (i.e 1) to visit profile: ") - 1
            return doctors[doctor_num]  # Don't remove or change it.
        else:
            print('NO DOCTOR AVAILABLE!')
            return False

    def get_checkup(self):
        """
        This method calls the staticmethod diagnose from Doctor class
        :returns diagnosed disease
        """
        return Doctor.diagnose(self)

    def choose_prescription(self):
        """
        This method allows patient to choose one prescription out of the listed prescriptions
        :returns object: desired prescription
        """
        print("------\nCHOOSE PRESCRIPTION!\n------")
        for idx, prescription in enumerate(self.prescriptions):
            print(f'PRESCRIPTION NO. {idx + 1}', end='')
            prescription.display()
        choice = input_integer("Enter the Prescription No. to buy medicines: ") - 1
        return self.prescriptions[choice]


# -------------------- DOCTOR --------------------


class Doctor(Person):
    doctors_data = [{
        'name': 'Dr. Sana Younas',
        'age': 39,
        'gender': 'Female',
        'family_code': 'AB221ZX',
        'qualification': 'FCPS',
        'speciality': 'Dermatologist',
        'location': 'Street 3, G-12, Islamabad',
        'contact': '03474291559',
        'working_hrs': '8:00 AM - 2:30 PM',
        'fee': 2500
    }, {
        'name': 'Prof. Dr. Suhail Sarwar',
        'age': 55,
        'gender': 'Male',
        'family_code': 'AB221ZY',
        'qualification': 'FCPS',
        'speciality': ' Cardiologist',
        'location': '14 New Abu Bakar Block, New Garden Town, Garden Town, Lahore',
        'contact': '03387745639',
        'working_hrs': '9:30 AM - 2:30 PM',
        'fee': 2500
    }, {
        'name': 'Dr. Israr Amir',
        'age': 32,
        'gender': 'Male',
        'family_code': 'AB221ZZ',
        'qualification': 'FCCP',
        'speciality': 'Pulmonologist',
        'location': 'Old Post Office, Market City Road, Mianwali',
        'contact': '03168244563',
        'working_hrs': '9:30 AM - 4:30 PM',
        'fee': 3000
    }, {
        'name': 'Dr. Mahrukh Zahoor',
        'age': 35,
        'gender': 'Female',
        'family_code': 'AA221ZY',
        'qualification': 'FCPS',
        'speciality': 'Cardiac Surgeon',
        'location': ' GT Road, Rahim Abad, mingora, Swat',
        'contact': '03351852296',
        'working_hrs': '8:30 AM - 5:30 PM',
        'fee': 1500
    }, {
        'name': 'Dr. Gohar Saeed',
        'age': 50,
        'gender': 'Male',
        'family_code': 'BB221ZZ',
        'qualification': 'CAAAM',
        'speciality': 'Eye Specialist',
        'location': 'DHA Defence, Garden town , Lahore',
        'contact': '03356284933',
        'working_hrs': '9:30 AM - 3:30 PM',
        'fee': 2000
    }]
    doctors = []
    knowledge = {
        'corona': [
            {'name': "Azithromycin",
             'potency': (250, 'mg'),
             'days': 3,
             'dose': (3, "times a day"),
             'dose_qty': (1, 'tab')},
            {'name': "Dexa",
             'potency': (2, 'mg'),
             'days': 3,
             'dose': (2, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'pneumonia': [
            {'name': "Azithromycin",
             'potency': (500, 'mg'),
             'days': 3,
             'dose': (2, "times a day"),
             'dose_qty': (1, 'tab')},
            {'name': "Clarithromycin",
             'potency': (500, 'mg'),
             'days': 3,
             'dose': (1, "times a day"),
             'dose_qty': (1 / 2, 'tab')}
        ],
        'influenza': [
            {'name': "Cetirizine",
             'potency': (10, 'mg'),
             'days': 3,
             'dose': (3, "times a day"),
             'dose_qty': (1, 'tab')},
            {'name': "Montika",
             'potency': (5, 'mg'),
             'days': 3,
             'dose': (2, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'migraine': [
            {'name': "ginkgo biloba extract",
             'potency': (60, 'mg'),
             'days': 5,
             'dose': (3, "times a day"),
             'dose_qty': (1 / 4, 'tab')},
            {'name': "opioids",
             'potency': (25, 'mg'),
             'days': 3,
             'dose': "once a day",
             'dose_qty': (1, 'tab')}
        ],
        'cluster headache': [
            {'name': "0xycodone",
             'potency': (5, 'mg'),
             'days': 5,
             'dose': (2, "times a day"),
             'dose_qty': (1 / 2, 'tab')}
        ],
        'sinus headache': [
            {'name': "Panadol",
             'potency': (500, 'mg'),
             'days': 5,
             'dose': (3, "times a day"),
             'dose_qty': (1, 'tab')},
            {'name': "Danzen ds ",
             'potency': (10, 'mg'),
             'days': 5,
             'dose': (2, "times a day"),
             'dose_qty': (1 / 2, 'tab')},
            {'name': " Cipcin",
             'potency': (250, 'mg'),
             'days': 3,
             'dose': (2, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'stroke': [
            {'name': "Heparin",
             'potency': (40, 'mg'),
             'days': 3,
             'dose': (1, "times a day"),
             'dose_qty': (1, 'injection')}
        ],
        'diabetes': [
            {'name': "Metformin",
             'potency': (500, 'mg'),
             'days': 5,
             'dose': (3, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'optic neuritis': [
            {'name': "Methylprednisolone",
             'potency': (4, 'mg'),
             'days': 3,
             'dose': (1, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'muscle strain': [
            {'name': "Thiocolchicoside",
             'potency': (4, 'mg'),
             'days': 2,
             'dose': (1, "times a day"),
             'dose_qty': (1, 'tab')}
        ],
        'asthma': [
            {'name': "Xylocin Inhalor",
             'potency': (200, 'mg'),
             'days': 10,
             'dose': (3, "times a day"),
             'dose_qty': (1, 'tab')}
        ]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']
        self.language = "English"
        self.speciality = kwargs['speciality']
        self.location = kwargs['location']
        self.contact = kwargs['contact']
        self.working_hrs = kwargs['working_hrs']
        self.ratings = []
        if self.ratings:
            self.rating = sum(self.ratings) / len(self.ratings)
        else:
            self.rating = 0
        self.fee = kwargs['fee']

    @staticmethod
    def read_doctors_data():
        for data in Doctor.doctors_data:
            fam = Family.add_family(data['family_code'])
            doctor = Doctor(name=data['name'], gender=data['gender'], age=data['age'], family=fam,
                            qualification=data['qualification'],
                            speciality=data['speciality'], location=data['location'], contact=data['contact'],
                            working_hrs=data['working_hrs'], fee=data['fee'])
            Doctor.doctors.append(doctor)

    def display_profile(self):
        """
        This method displays all the information of a doctor.
        :returns
        """
        statement = f"""
        ------
        {self.name.upper()}
        ------
        Fee: {self.fee} -/Rs.
        Rating: {self.rating} STARS
        Qualification: {self.qualification}
        Speciality: {self.speciality}
        Language: {self.language}
        Working Hours: {self.working_hrs}
        Contact: {self.contact}
        Location: {self.location}
        """
        print(statement)

    def display_short(self):
        """
        This method displays the brief description
        :returns
        """
        print(f'{self.name.upper()} ({self.speciality.upper()})')

    @staticmethod
    def get_initial_symptoms():
        """
        This method makes the list of all the initial_symptoms of diseases
        :returns list of initial_symptoms
        """
        initial_symptoms = []
        for disease in Disease.diseases:
            initial_symptoms.append(disease.symptoms[0])
        return list(set(initial_symptoms))

    @staticmethod
    def check_symptoms() -> list:
        """
        This method makes the list of symptoms by using the list provided by above staticmethod get_initial_symptoms
        :returns list of symptoms
        """
        symptoms = Doctor.get_initial_symptoms()
        for idx, value in enumerate(symptoms):
            print(idx + 1, end=': ')
            print(value.upper())
        symptom_num = input_integer('Which symptom do you have? Enter number (i.e 1): ') - 1
        symptom_lists = []
        for value in Disease.diseases_data:
            if symptoms[symptom_num] == value['symptoms'][0]:
                symptom_lists.append(value['symptoms'])
        return symptom_lists

    @staticmethod
    def diagnose(patient: Patient) -> Disease:
        """
        This method checks for the symptoms.
        :param patient
        :returns Disease, diagnosed disease as per symptoms.
        """
        symptom_lists = Doctor.check_symptoms()
        for idx, value in enumerate(symptom_lists):
            print(idx + 1, end=': ')
            print(value)
        list_num = input_integer('Select set of symptoms do you have, Enter number (i.e 1): ') - 1
        exact_symptoms = symptom_lists[list_num]
        for disease in Disease.diseases:
            if exact_symptoms == disease.symptoms:
                return disease

    @staticmethod
    def prescribe_medicines(disease: Disease, prescription):
        """
        :returns this method will return the prescription on the basis of disease
        """
        for medicine in Doctor.knowledge[disease.name]:
            prescribed_drug = PrescribedMedicine(name=medicine['name'], potency=medicine['potency'],
                                                 dose=medicine['dose'],
                                                 dose_qty=medicine['dose_qty'], dose_days=medicine['days'])
            prescription.cure.append(prescribed_drug)
        return prescription

    def write_prescription(self, disease: Disease, patient: Patient):
        """
         This method appends the object of prescription in list of prescriptions
         :returns object
         """
        prescription = Doctor.prescribe_medicines(disease, Prescription(doctor=self, patient=patient))
        patient.prescriptions.append(prescription)
        return prescription


# -------------------- PRESCRIPTION --------------------


class Prescription:
    def __init__(self, **kwargs):
        self.identity = generate_code()
        self.prescribed_by = kwargs['doctor']
        self.prescribed_to = kwargs['patient']
        self.cure = []  # list of prescribed medicines (objects)

    def display_cure(self):
        """
        This method displays the prescribed medicines
        :returns
        """
        for medicine in self.cure:
            medicine.display()

    def display(self):
        """
        This method displays the patient's details
        :returns
        """
        statement = f"""
        ------
        By {self.prescribed_by.name.upper()}
        ------
        Patient Detail!
         Name: {self.prescribed_to.name.capitalize()}
         Age: {self.prescribed_to.age}
         Gender: {self.prescribed_to.gender}
        Prescribed Medicines!"""
        print(statement)
        self.display_cure()


# -------------------- PRESCRIBED MEDICINE --------------------


class PrescribedMedicine:
    prescribed_days = 3
    cure = []

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.potency = kwargs['potency']
        self.dose = kwargs['dose']
        self.dose_qty = kwargs['dose_qty']
        self.dose_days = kwargs['dose_days']
        self.quantity = self.dose[0] * self.dose_qty[0] * self.dose_days

    def display(self):
        """
        This method displays the details of medicine
        :returns
        """
        print(
            f'\t\t {self.name.upper()} {self.potency[0]}{self.potency[1]}\t\t'
            f' {self.dose_qty[0]} {self.dose_qty[1]} {self.dose[0]} {self.dose[1].upper()}')
