# Generic exception
class Error(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class InvalidYear(Error):
    pass


class InvalidMonth(Error):
    pass


class InvalidDay(Error):
    pass


class InvalidName(Error):
    pass


class InvalidDates(Error):
    pass


class InvalidChoice(Error):
    pass


class InvalidFamilyCode(Error):
    pass
