from string import ascii_letters

integer_warning = '(ValueError) WARNING! Input should be an integer.'


class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def set_day(self, n_day):
        self.__day = n_day

    def set_month(self, n_month):
        self.__month = n_month

    def set_year(self, n_year):
        self.__year = n_year

    def display(self):
        return f'Day/Month/Year: {self.__day}/{self.__month}/{self.__year}'

    @staticmethod
    def input_year():
        while True:
            try:
                year = int(input('Enter Year (i.e. 2020): '))
                if year <= 0:
                    raise InvalidYear('WARNING! Year cannot be zero or less than zero.')
                return year
            except ValueError:
                print(integer_warning)
            except Exception as e:
                print(e)
                continue

    @staticmethod
    def input_month():
        while True:
            try:
                month = int(input('Enter Month (i.e. 1 -> 12): '))
                if (month > 12) or (month <= 0):
                    raise InvalidMonth('WARNING! Month can never be less than 1 and greater than 12.')
                return month
            except ValueError:
                print(integer_warning)
            except Exception as e:
                print(e)
                continue

    @staticmethod
    def input_day(month, year):
        months = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December')
        while True:
            try:
                day = int(input('Enter Day (i.e. 1-31): '))
                is_leap = (year % 4 == 0)
                if (day <= 0) or (day > 31):
                    raise InvalidDay('WARNING! Day can never be zero or less than zero and greater than 31.')
                else:
                    if (not is_leap) and (month == 2):
                        if day > 28:
                            raise InvalidDay(
                                'WARNING! In February Day cannot be greater than 28, if it\'s non-leap year.')
                        elif day > 29:
                            raise InvalidDay('WARNING! In February, Day cannot be greater than 29, if it\'s leap year.')
                    elif (day > 30) and (month in [4, 6, 9, 11]):
                        raise InvalidDay(f'WARNING! In {months[month - 1]}, Day cannot be greater than 30.')
                return month
            except ValueError:
                print(integer_warning)
            except Exception as e:
                print(e)
                continue

    @classmethod
    def add_date(cls, statement=''):
        print(statement)
        y = Date.input_year()
        m = Date.input_month()
        d = Date.input_day(m, y)
        return cls(d, m, y)

    # Operator Overloading
    def __eq__(self, other):
        if (self.__day == other.__day) and (self.__month == other.__month) and (self.__year == other.__year):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month < other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day < other.__day:
                    return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'{self.__day}/{self.__month}/{self.__year}'


def input_alpha(subject: str, text_to_display: str) -> str:
    """
    Function will raise exception if the input is not only alphabetical; And ask until valid input entered.
    :param subject: It can be 'name' or anything that contains only alphabets.
    :param text_to_display: Its a statement to ask for input subject(i.e name)
    :return string: It will return subject.
    """
    while True:
        try:
            name = input(f'{text_to_display}')
            if set(name) > set(ascii_letters):
                raise InvalidName(f'WARNING! {subject} can only contain alphabets.')
            return name
        except Exception as e:
            print(e)
            continue


def input_integer(text_to_display: str) -> int:
    """
    This function will take input from the user check if the input is an integer or not.
    If its not, func will raise exception and let the user try again to input integer until
    user enter an integer.
    :param text_to_display: A string type statement to ask for integer.
    :return: integer
    """
    while True:
        try:
            num = int(input(f'{text_to_display}'))
            return num
        except ValueError:
            print(integer_warning)
        except Exception as e:
            print(e)
            continue


class Person:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.age = kwargs['age']


class Diagnosis:
    @classmethod
    def disease_and_symptoms_data(cls):
        flue = [[['Symptom 1 = Fever + Shortage of breathe + Loss of appetite'], ['Pneumonia']], [['Symptom 2 = Fever'],
                                                                                                  ['Normal Influenza']],
                [['Symptom 3 = Dry cough + Weakness + Constant fever'], ['Corona']]]
        head_ache = [[['Symptom 1 = One sided + Nausea + Blurry vision'], ['Migraine']],
                     [['Symptom 2 = Behind an eye + Eyelid droop + Eye redness + tears'], ['Cluster headache']],
                     [['Symptom 3 = Pain in cheek bone + Forehead + Bridge of nose'], ['Sinus headache']]]
        blurry_vision = [[['Symptom 1 = Sudden weakness + headache + loss of balance'], ['Stroke']],
                         [['Symptom 2 = Frequent urination + tingling limbs + feeling hungry'], ['Diabetes']],
                         [['Symptom 3 = Vision losing one eye + Pain around eye', ['Optic neuritis']]]]
        chest_tightness = [[['Symptom 1 = tenderness + swelling'], ['Muscle strain']],
                           [['Symptom 2 = Shortness of breathe + coughing'], ['Asthma']]]
        diseases = flue, head_ache, blurry_vision, chest_tightness
        return diseases
