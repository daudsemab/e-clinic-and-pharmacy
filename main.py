from utilities import input_integer, InvalidChoice
from pharmacy_system import *
from clinic_system import *

Disease.read_disease_data()
Doctor.read_doctors_data()
pharmacy_warning = 'WARNING! You cannot do this until you have a pharmacy.'

print("---------------------------------------------------\n"
      "HELLO, WELCOME TO 'ONLINE CLINIC & PHARMACY SYSTEM'"
      "\n---------------------------------------------------")

user = None

while True:
    try:
        choice = input_integer("Signup as a,\n\t1: PATIENT\n\t2: PHARMACIST\nEnter Choice: ")
        if choice != 1 and choice != 2:
            raise InvalidChoice('WARNING! Your choice is invalid.\n------\nTRY AGAIN\n------')
        else:
            break
    except Exception as e:
        print(e, "This is exception")
if choice == 1:
    user = Patient.create_self()
elif choice == 2:
    user = Pharmacist.create_self()

if isinstance(user, Patient):
    pharmacist_family = Family.add_family("AC456XZ")
    pharmacist = Pharmacist(name='Tariq Zaid', gender='Male', age=29, family=pharmacist_family)
    pharmacist.pharmacy = Pharmacy(name='Tariq Pharmacy', pharmacist=pharmacist, license_num=987678)
    pharmacist.pharmacy.read_medicine_data()
    commands = f"""
                    -------- COMMANDS --------
                    Enter --> 1: See Available Doctors For Checkup
                    Enter --> 2: See Your Prescriptions
                    Enter --> 3: Buy Medicines 
                    ENTER --> 4: TO EXIT PROGRAM.
                    -------------------------- """
    print(commands)
    while True:
        command = input_integer("Enter Instruction Number (i.e 1): ")
        if command == 1:
            doctor = user.see_available_doctors()
            if doctor:
                doctor.display_profile()
                diagnosed_disease = user.get_checkup()
                print(f'------\nYou are a patient of {diagnosed_disease.name.upper()}.\n------')
                user.add_disease(diagnosed_disease)
                prescription = doctor.write_prescription(diagnosed_disease, user)
                choice = input_integer(
                    f"Do you want to rate {doctor.name.upper()},\n\t1: YES\n\t2: NO\nEnter Choice (i.e 1): ")
                if choice == 1:
                    user.rate_doctor(doctor)
        elif command == 2:
            if len(p := user.prescriptions):
                for prescription in p:
                    prescription.display()
            else:

                print("YOU HAVE NO PRESCRIPTION!")
        elif command == 3:
            prescription = user.choose_prescription()
            drug_list = pharmacist.read_prescription(prescription)
            if pharmacist.pharmacy.is_medicines_available(drug_list):
                total_bill, invoice = pharmacist.pharmacy.make_order(drug_list)
                if pharmacist.check_bill(total_bill):
                    pharmacist.pharmacy.update_inventory(drug_list)
                    pharmacist.pharmacy.add_sale(total_bill)
                    print(invoice)
                    print('THANK YOU FOR SHOPPING!')
                else:
                    print("YOU HAVE NOT ENOUGH AMOUNT TO BUY MEDICINES!")
            else:
                print("SORRY! Your required medicines are not available.")
        elif command == 4:
            print('-----\nPROGRAM ENDS ... HAVE A NICE DAY!\n-----')
            break
        else:
            print(f'KINDLY ENTER RIGHT COMMAND!\n{commands}')
elif isinstance(user, Pharmacist):
    commands = f"""
                    -------- COMMANDS --------
                    Enter --> 0: Create Pharmacy
                    Enter --> 1: Add Medicines
                    Enter --> 2: Display Expired Drug
                    Enter --> 3: Dispose Expired Medicines
                    Enter --> 4: Display Pharmacy States
                    ENTER --> 5: TO EXIT PROGRAM.
                    --------------------------  """
    print(commands)
    while True:
        try:
            command = input_integer("Enter Instruction Number (i.e 0): ")
            if command == 0:
                if not user.pharmacy:
                    user.create_pharmacy()
                    user.pharmacy.read_medicine_data()
                else:
                    print("You already have a pharmacy and cannot you cannot create more than one.")
            elif command == 1:
                if user.pharmacy:
                    user.pharmacy.add_medicine()
                else:
                    print(pharmacy_warning)
            elif command == 2:
                if user.pharmacy:
                    user.pharmacy.display_expired_drugs()
                else:
                    print(pharmacy_warning)
            elif command == 3:
                if user.pharmacy:
                    user.pharmacy.remove_expired_drugs()
                else:
                    print(pharmacy_warning)
            elif command == 4:
                if user.pharmacy:
                    user.pharmacy.display_pharmacy_stats()
                else:
                    print(pharmacy_warning)
            elif command == 5:
                print('-----\nPROGRAM ENDS ... HAVE A NICE DAY!\n-----')
                break
            else:
                raise InvalidChoice(f"WARNING! Entered command is not valid.\n------ TRY AGAIN ------\n{commands}")
        except Exception as e:
            print(e)
