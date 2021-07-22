def input_integer(text_to_display):
    """
    This function will take input from the user check if the input is an integer or not.
    If its not, func will raise exception and let the user try again to input integer until
    user enter the integer.
    :param text_to_display:
    :return: integer
    """
    while True:
        try:
            num = int(input(f'{text_to_display}'))
            return num
        except ValueError:
            print('(ValueError) WARNING! Input should be an integer.')
        except Exception as e:
            print(e)
            continue


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

    @classmethod
    def add_date(cls):
        d_objection = 'KINDLY ENTER VALID DAY NUMBER!'
        m_objection = 'KINDLY ENTER VALID MONTH NUMBER!'
        y_objection = 'KINDLY ENTER VALID YEAR NUMBER!'
        while True:
            y = int(input('Enter Year: '))
            try:
                if y <= 0:
                    print(y_objection)
                    continue
                else:
                    break
            except ValueError:
                print(y_objection)
                continue

        while True:
            m = int(input('Enter Month (i.e. 1-12): '))
            try:
                if (m > 12) or (m <= 0):
                    print(m_objection)
                    continue
                else:
                    break
            except ValueError:
                print(m_objection)
                continue

        while True:
            d = int(input('Enter Day (i.e. 1-31): '))
            is_leap = (y % 4 == 0)
            try:
                if (not is_leap and ((m == 2) and ((d > 28) or (d <= 0)))) or (
                        is_leap and ((m == 2) and ((d > 29) or (d <= 0)))) or (
                        ((d > 30) and (d <= 0)) and (m in [4, 6, 9, 11])) or (
                        d <= 0):
                    print(d_objection)
                    continue
                else:
                    break
            except ValueError:
                print('KINDLY ENTER VALID DAY NUMBER!')
                continue
        print('')
        return cls(d, m, y)


class Time:
    def __init__(self, hour, minute):
        if (hour <= 24) or (hour >= 0):
            self.__hour = hour
            self.__minute = minute

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def set_hour(self, n_hour):
        self.__hour = n_hour

    def set_minute(self, n_minute):
        self.__minute = n_minute

    def __eq__(self, other):
        if (self.__hour == other.__hour) and (self.__minute == other.__minute):
            return True
        else:
            return False

    def __sub__(self, other):
        hours = self.__hour - other.__hour
        minutes = self.__minute - other.__minute
        return Time(hours, minutes)

    def __gt__(self, other):
        if (self.__hour >= other.__hour) and (self.__minute > other.__minute):
            return True
        else:
            return False

    @classmethod
    def add_time(cls):
        t_objection = 'KINDLY ENTER VALID INPUT!'
        # Take Hours
        while True:
            h = int(input('Enter Hour (i.e. 1-24): '))
            try:
                if (h > 24) or (h < 1):
                    print(t_objection)
                    continue
                else:
                    break
            except ValueError:
                print(t_objection)
                continue
        # Take Minutes
        while True:
            m = int(input('Enter Minutes (i.e. 0-60): '))
            try:
                if (m > 60) or (m < 0):
                    print(t_objection)
                    continue
                else:
                    break
            except ValueError:
                print(t_objection)
                continue
        return cls(h, m)

    def display(self):
        return f'{self.__hour}:{self.__minute}'


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
