class NegativeTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


def validate_title(title):
    if title is not None and title < 0:
        raise NegativeTitlesError("titles cannot be negative")


class InvalidYearCupError(Exception):
    def __init__(self, message: str):
        self.message = message


def check_cup_year(cup_year):
    if cup_year < 1930:
        raise InvalidYearCupError("there was no world cup this year")
    elif (cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


def validate_titles(titles, cups):
    if titles > cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
