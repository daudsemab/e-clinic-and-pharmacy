from utilities import Person


class Pharmacist(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']


class Pharmacy:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.license_num = kwargs['license_num']


class Manufacturer:
    manufacturers = []
    new_code = 0

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.license_num = kwargs['license_num']
        self.manufacturer_id = Manufacturer.new_code + 10000
        Manufacturer.new_code = self.manufacturer_id


class Medicine:
    medicines = []

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.manufacturer = kwargs['manufacturer']
        self.mfg_date = kwargs['mfg_date']
        self.exp_date = kwargs['exp_date']
        self.drug_id = self.manufacturer.manufacturer_id + len(Medicine.medicines) + 1

