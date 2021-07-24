# built-in modules
from random import randint, sample
# local modules
from utilities import Person, Date, input_alpha, input_integer
from custom_exceptions import InvalidDates


class Manufacturer:
    manufacturers = []
    new_code = 0

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self._license_num = kwargs['license_num']
        self.medicines = []  # list of medicines made by a single manufacturer
        self.manufacturer_id = Manufacturer.new_code + 10000
        Manufacturer.new_code = self.manufacturer_id

    def append_medicine(self, medicine):
        if drugs := self.medicines:
            for drug in drugs:
                if drug.name == medicine.name:
                    break
            else:
                self.medicines.append(medicine)

    @classmethod
    def add_manufacturer(cls):
        name = input_alpha("Name", "Enter name of Manufacturer: ")
        license_num = input_integer("Enter license number of manufacturer: ")
        manufacturer = cls(name=name, license_num=license_num)
        Manufacturer.manufacturers.append(manufacturer)
        return manufacturer


class Medicine:
    medicines = []

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.salt = kwargs['salt']
        self.manufacturer = kwargs['manufacturer']
        self.mfg_date = kwargs['mfg_date']
        self.exp_date = kwargs['exp_date']
        # Before assigning drug_id check if its exists in the manufacturer's medicines list.
        for drug in self.manufacturer.medicines:
            if self.name == drug.name:
                # Drugs with the same names must have same drug_id.
                self.drug_id = drug.drug_id
                break
        else:
            self.drug_id = self.manufacturer.manufacturer_id + len(self.manufacturer.medicines) + 1
        # Generate a unique random code
        self.batch_code = f'{"".join(sample("ABC", k=1))}{randint(111, 999)}{"".join(sample("XYZ", k=1))}'

    def display(self, count: int = ''):
        statement = f"""
        ------\nDRUG {count}\n------
        Name: {self.name}
        Chemical: {self.salt}
        Manufacturer: {self.manufacturer.name}
        Manufacturing Date: {self.mfg_date}
        Expiry Date: {self.exp_date}"""
        print(statement, end='')

    @staticmethod
    def input_manufacturer():
        """
        This func takes name of manufacturer as an input from the user and returns its object if exists.
        :returns object of Manufacturer
        """
        while True:
            mnf_name = input_alpha("Name", "Enter name of manufacturer: ")
            for manufacturer in Manufacturer.manufacturers:
                if mnf_name == manufacturer.name:
                    return manufacturer
            else:
                print('WARNING! Manufacturer does not exist.\nTry Again!')

    @staticmethod
    def __return_valid_dates() -> tuple:
        """
        This func takes input manufacturing and expiry dates of the medicines and checks their validity.
        :returns tuple: manufacturing and expiry date objects in a tuple i.e (mnf_date, exp_date).
        """
        while True:
            try:
                mfg_date = Date.add_date("Enter manufacturing date of the medicine!")
                exp_date = Date.add_date("Enter expiry date of the medicine!")
                if exp_date < mfg_date:
                    raise InvalidDates('WARNING! Entered dates are invalid.\nTry Again!')
                return mfg_date, exp_date
            except Exception as e:
                print(e)

    @classmethod
    def add_medicine(cls):
        name = input_alpha("Name", "Enter the name of medicine: ")
        salt = input_alpha("Name", "Enter salt (Chemical) of the medicine: ")
        manufacturer = Medicine.input_manufacturer()
        mfg_date, exp_date = Medicine.__return_valid_dates()
        medicine = cls(name=name, salt=salt, manufacturer=manufacturer, mfg_date=mfg_date, exp_date=exp_date)
        Medicine.medicines.append(medicine)
        manufacturer.append_medicine(medicine)
        return medicine


class Pharmacist(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = kwargs['qualification']


class Pharmacy:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.license_num = kwargs['license_num']
        self.inventory = []
        self.expired_drugs = []
        self.sale = 0

    def get_purchasing_drug_info(self, drug_name):
        retail_price = input_integer(f"Enter retail price of {drug_name}: ")
        margin = input_integer(f"How many percent is the margin on {drug_name}: ")
        purchase_price = retail_price - (retail_price * (margin/100))
        qty = input_integer(f"Enter the quantity of medicine to be added into inventory of {self.name}: ")
        return purchase_price, retail_price, qty

    def add_medicine(self):
        medicine = Medicine.add_medicine()
        medicine.purchase_price, medicine.retail_price, medicine.quantity = self.get_purchasing_drug_info(medicine.name)
        self.inventory.append(medicine)

    def update_inventory(self, name, qty):
        for drug in self.inventory:
            if (name == drug.name) and (drug.quantity >= qty):
                drug.quantity -= qty
                break

    def read_prescription(self):
        """:returns
        """
        pass

    def calculate_expired_drugs(self):
        today = Date.add_date("Enter Today's Date!")
        for drug in self.inventory:
            if today == drug.exp_date:
                self.expired_drugs.append(drug)

    def display_expired_drugs(self):
        self.calculate_expired_drugs()
        if self.expired_drugs:
            print('------------ EXPIRED DRUGS ------------')
            for drug in self.expired_drugs:
                drug.display()
            print(f'COUNT = {len(self.expired_drugs)}\n---------------------------------------')
        else:
            print('NO EXPIRED DRUG!')
