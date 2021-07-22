from person import Person


class Pharmacist(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']


class Pharmacy:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.license_num = kwargs['license_num']
