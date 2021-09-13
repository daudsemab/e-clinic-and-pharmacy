# local modules
from utilities import Person, Date, input_alpha, input_integer, generate_code
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
        """
        This method will take the object of medicine and append the it in the list if it already does not exists
        :returns
        """
        if drugs := self.medicines:
            for drug in drugs:
                if drug.name == medicine.name:
                    break
            else:
                self.medicines.append(medicine)
        else:
            self.medicines.append(medicine)

    @classmethod
    def add_manufacturer(cls):
        """
        This method takes the name and license number as input and append the object of manufacturer
        :returns object: it returns the object of manufacturer
        """
        name = input_alpha("Name", "Enter name of Manufacturer: ")
        license_num = input_integer("Enter license number of manufacturer: ")
        manufacturer = cls(name=name, license_num=license_num)
        Manufacturer.manufacturers.append(manufacturer)
        return manufacturer


class Medicine:
    medicines = []
    medicine_data = [
        {'name': "Azithromycin",
         'salt': 'Sodium',
         'manufacturer': ('LOTUS PHARMACEUTICALS', 999888),
         'retail_price': 165,
         'purchase_price': 100,
         'qty': 180,
         'mfg_date': (12, 2, 2021),
         'exp_date': (12, 2, 2023)},
        {'name': "Dexa",
         'salt': 'Sodium phosphate',
         'manufacturer': ('Zydus Cadila', 982342),
         'retail_price': 883,
         'purchase_price': 780,
         'qty': 200,
         'mfg_date': (15, 3, 2021),
         'exp_date': (17, 2, 2023)},
        {'name': "Azithromycin",
         'salt': 'Sodium',
         'manufacturer': ('Zithromax ', 878787),
         'retail_price': 180,
         'purchase_price': 160,
         'qty': 300,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Clarithromycin ",
         'salt': 'methylerythromycin',
         'manufacturer': ('Abbott Laboratories',434567),
         'retail_price': 350,
         'purchase_price': 230,
         'qty': 400,
         'mfg_date': (6, 4, 2021),
         'exp_date': (8, 8, 2023)},
        {'name': "Cetirizine ",
         'salt': 'hydrochloride ',
         'manufacturer': ('HOOVER PHARMACEUTICALS', 534533),
         'retail_price': 50,
         'purchase_price': 42,
         'qty': 1000,
         'mfg_date': (23, 3, 2021),
         'exp_date': (28, 8, 2023)},
        {'name': "Montika ",
         'salt': 'Montilukast Sodium',
         'manufacturer': ('SAMI PHARMACEUTICALS', 342976),
         'retail_price': 180,
         'purchase_price': 130,
         'qty': 600,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Ginkgo Biloba extract",
         'salt': 'Herb Green Health Biotech Co., Ltd.',
         'manufacturer': ('Ginkgolides', 984534),
         'retail_price': 270,
         'purchase_price': 350,
         'qty': 300,
         'mfg_date': (1, 1, 2021),
         'exp_date': (1, 1, 2023)},
        {'name': "Opioids",
         'salt': 'Hydrocodone ',
         'manufacturer': ('Johnson & Johnson', 994534),
         'retail_price': 350,
         'purchase_price': 250,
         'qty': 300,
         'mfg_date': (8, 1, 2021),
         'exp_date': (7, 11, 2022)},
        {'name': "0xycodone",
         'salt': 'Hydrochloride ',
         'manufacturer': ('Purdue Pharma', 549735),
         'retail_price': 390,
         'purchase_price': 320,
         'qty': 400,
         'mfg_date': (8, 4, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Panadol",
         'salt': 'Sodium',
         'manufacturer': ('GSK', 9234334),
         'retail_price': 40,
         'purchase_price': 34,
         'qty': 800,
         'mfg_date': (23, 1, 2021),
         'exp_date': (9, 1, 2023)},
        {'name': "Danzen ds",
         'salt': 'Serratiopepditase',
         'manufacturer': ('Helix Pharma (Pvt) Ltd', 684736),
         'retail_price': 260,
         'purchase_price': 220,
         'qty': 1200,
         'mfg_date': (6, 2, 2021),
         'exp_date': (7, 5, 2023)},
        {'name': "Cipcin",
         'salt': 'Ciprofloxacin',
         'manufacturer': ('OBSONS PHARMACEUTICALS', 385953),
         'retail_price': 190,
         'purchase_price': 150,
         'qty': 300,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Heparin",
         'salt': ' mucosal tissues',
         'manufacturer': ('FRENCH PHARMACEUTICAL GROUP', 453454),
         'retail_price': 140,
         'purchase_price': 100,
         'qty': 700,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Metformin",
         'salt': 'biguanide metformin ',
         'manufacturer': ('MACTOR PHARMACEUTICALS', 580478),
         'retail_price': 90,
         'purchase_price': 50,
         'qty': 500,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Methylprednisolone",
         'salt': 'methylprednisolone sodium succinate',
         'manufacturer': ('HAJI MEDICINE CO', 345345),
         'retail_price': 2500,
         'purchase_price': 1690,
         'qty': 300,
         'mfg_date': (18, 1, 2021),
         'exp_date': (17, 5, 2023)},
        {'name': "Thiocolchicoside",
         'salt': 'Naproxen sodium',
         'manufacturer': ('SANOFI AVENTIS', 485380),
         'retail_price': 803,
         'purchase_price': 780,
         'qty': 80,
         'mfg_date': (22, 5, 2021),
         'exp_date': (27, 8, 2023)},
        {'name': 'Xylocin Inhalor',
         'salt': 'Naproxen sodium',
         'manufacturer': ('GETZ PHARMA', 344355),
         'retail_price': 786,
         'purchase_price': 650,
         'qty': 800,
         'mfg_date': (22, 5, 2021),
         'exp_date': (27, 8, 2023)}
    ]

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
        self.batch_code = generate_code()

    def display(self, count: int = ''):
        """
        This method prints the information of each drug
        :returns
        """
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
        This method takes name of manufacturer as an input from the user and returns its object if exists.
        :returns object: it returns the object of Manufacturer
        """
        return Manufacturer.add_manufacturer()

    @staticmethod
    def __return_valid_dates() -> tuple:
        """
        This method takes input manufacturing and expiry dates of the medicines and checks their validity.
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
        """
        This method takes name and salt used in the formula of medicine as input uses the input_manufacturer and
        return_valid_dates to append the object of medicine in the list of medicines.
        :return: object: it returns the object of medicine
        """
        name = input_alpha("Name", "Enter the name of medicine: ")
        salt = input_alpha("Salt", "Enter salt (Chemical) of the medicine: ")
        manufacturer = Medicine.input_manufacturer()
        mfg_date, exp_date = Medicine.__return_valid_dates()
        medicine = cls(name=name, salt=salt, manufacturer=manufacturer, mfg_date=mfg_date, exp_date=exp_date)
        Medicine.medicines.append(medicine)
        manufacturer.append_medicine(medicine)
        return medicine


class Pharmacist(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qualification = 'D-Pharmacy'
        self.pharmacy = False

    def create_pharmacy(self):
        name = input_alpha("Name", "Enter Pharmacy Name: ")
        license_num = input_integer("Enter License Number: ")
        self.pharmacy = Pharmacy(name=name, license_num=license_num, pharmacist=self)
        return self.pharmacy

    @staticmethod
    def read_prescription(prescription) -> list:
        """
        This method takes prescription (object) and makes list of name and quantity of each drug for that prescription
        :param prescription (object)
        :return: list: it returns the list tuples(containing name and quantity of medicine)
        """
        drug_list = []
        for drug in prescription.cure:
            drug_list.append((drug.name, drug.quantity))
        return drug_list


class Pharmacy:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.pharmacist = kwargs['pharmacist']
        self.license_num = kwargs['license_num']
        self.inventory = []
        self.expired_drugs = []
        self.sale = 0
        self.loss = 0
        self.profit = 0

    def display_pharmacy_stats(self):
        info = f"""
                Total Medicines  : {len(Medicine.medicines)}
                Expired Medicines: {len(self.expired_drugs)}
                Sales: {self.sale}
                Profit: {self.profit}    
                Loss : {self.loss}     
                """
        print(info, end='')

    def remove_expired_drugs(self):
        """This method removes the expired medicines from the inventory"""
        loss = 0
        for expired_drug in self.expired_drugs:
            for drug in self.inventory:
                if expired_drug.name == drug.name:
                    self.inventory.remove(drug)
                    loss += expired_drug.puchase_price
        self.loss = loss
        self.expired_drugs.clear()

    def get_purchasing_drug_info(self, drug_name) -> tuple:
        """
        This method takes the retail price, margin in medicine andl quantity of medicine as input and calculates the
        purchase price through first two.
        :param drug_name
        :return tuple: it returns the tuple containing purchase_price, retail_price, qty of a medicine
        """
        retail_price = input_integer(f"Enter retail price of {drug_name}: ")
        margin = input_integer(f"How many percent is the margin on {drug_name}: ")
        purchase_price = retail_price - (retail_price * (margin / 100))
        qty = input_integer(f"Enter the quantity of medicine to be added into inventory of {self.name}: ")
        return purchase_price, retail_price, qty

    def add_medicine(self):
        """
        This method adds purchase medicines in the pharmacies inventory
        :return
        """
        medicine = Medicine.add_medicine()
        medicine.purchase_price, medicine.retail_price, medicine.quantity = self.get_purchasing_drug_info(medicine.name)
        self.inventory.append(medicine)

    def is_medicines_available(self, drug_list):
        """
        This method checks drug list if drugs exists in pharmacy's inventory
        :param drug_list
        :returns boolean
        """
        for drug in drug_list:
            for medicine in self.inventory:
                if (drug[0] == medicine.name) and (not drug[1] <= medicine.quantity):
                    break
            else:
                return True
        return False

    # Customer Order Process
    def make_order(self, drug_list) -> tuple:
        """
        This method calculates the bill of medicine using the list of drugs and create invoice
        :param drug_list
        :return tuple: (total_bill, invoice)
        """
        total_bill = 0
        invoice = "------ INVOICE ------"
        for drug in drug_list:
            for medicine in self.inventory:
                if drug[0] == medicine.name:
                    price = medicine.retail_price * drug[1]
                    invoice += f'\n{drug[1]} - {drug[0]} {price} -/Rs'
                    total_bill += price
        invoice += f"\n---------------------\nTOTAL BILL : {total_bill} -/Rs"
        invoice += f"\n---------------------\nSOLD USING FAMILY ACCOUNT\n---------------------"
        return total_bill, invoice

    def update_inventory(self, drug_list):
        """
        This method keeps the inventory updated
        :param drug_list
        :return
        """
        profit = 0
        for name, qty in drug_list:
            for medicine in self.inventory:
                if (name == medicine.name) and (medicine.quantity >= qty):
                    medicine.quantity -= qty
                    profit = (medicine.retail_price * qty) - (medicine.purchase_price * qty)
        self.profit = profit

    def add_sale(self, sale):
        """
        :param sale
        """
        self.sale += sale

    def calculate_expired_drugs(self):
        """
        This method checks if the required medicine is expired or not.
        :return None
        """
        today = Date.add_date("Enter Today's Date!")
        for drug in self.inventory:
            if drug.exp_date <= today:
                self.expired_drugs.append(drug)

    def read_medicine_data(self):
        """
        This method reads and passes information of each medicine(which is stored in the form of dictionary) to above class
        method add_medicine
        :return None
        """
        for medicine in Medicine.medicine_data:
            mfg_date = Date.read_date(medicine['mfg_date'])
            exp_date = Date.read_date(medicine['exp_date'])
            name, license_num = medicine['manufacturer']
            manufacturer = Manufacturer(name=name, license_num=license_num)
            medicine_obj = Medicine(name=medicine['name'], salt=medicine['salt'], manufacturer=manufacturer,
                                    mfg_date=mfg_date, exp_date=exp_date)
            medicine_obj.retail_price = medicine['retail_price']
            medicine_obj.purchase_price = medicine['purchase_price']
            medicine_obj.quantity = medicine['qty']
            Medicine.medicines.append(medicine_obj)
            self.inventory.append(medicine_obj)

    def display_expired_drugs(self):
        """
        This method displays all the expired drugs and if the list of expired drugs is empty it displays that there
        is no expired drug.
        :returns None
        """
        self.calculate_expired_drugs()
        if self.expired_drugs:
            print('------------ EXPIRED DRUGS ------------')
            for drug in self.expired_drugs:
                drug.display()
            print(f'COUNT = {len(self.expired_drugs)}\n---------------------------------------')
        else:
            print('NO EXPIRED DRUG!')
