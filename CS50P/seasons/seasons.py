from datetime import date
import sys
import inflect


def main():
    try:
        birthday = input('Birthday(YYYY-MM-DD): \n')
        year, month, day = birthday.split('-')
        _date = date(int(year), int(month), int(day))
        c_date = date.today()

        #days
        timedelta = c_date - _date
        minutes = _minutes(timedelta.days)
        print(convert(minutes).capitalize())

    except (ValueError, KeyboardInterrupt, EOFError):
        sys.exit(1)


def _minutes(days):
    return days * 24 * 60

def convert(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="") + " minutes"




if __name__ == "__main__":
    main()