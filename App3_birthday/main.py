import datetime


def print_header():
    print('---------------------------')
    print('      BIRTHDAY APP')
    print('---------------------------')
    print()


def get_user_birthday():
    print("Enter your birth date? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    bday = datetime.date(year, month, day)
    return bday


def compute_days_between_dates(birth_date, target_date):
    birthdate_this_year = datetime.date(target_date.year, birth_date.month, birth_date.day)

    numDays = birthdate_this_year - target_date
    return numDays.days


def print_birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday!!!")


def main():
    print_header()
    birthday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(birthday, today)
    print_birthday_information(number_of_days)


main()
