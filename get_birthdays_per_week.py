from collections import defaultdict
from datetime import datetime

WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
LAST_WORK_DAY = 4 # Friday

def get_weekday(birthday):
    """Takes the week number and returns the name of the day of the week or Monday if the birthday falls on a weekend."""
    return WEEKDAYS[0] if birthday > LAST_WORK_DAY else WEEKDAYS[birthday]

def get_birthdays_per_week(users):
    """Takes the list of people and show them with birthdays one week ahead of the current day."""
    today = datetime.today().date()
    grouped_birthdays = defaultdict(list)
    DAYS_RANGE = 7

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days

        if delta_days < DAYS_RANGE:
            birthday_weekday = birthday_this_year.weekday()
            weekday = get_weekday(birthday_weekday)
            grouped_birthdays[weekday].append(name)


    for weekday, people_list in grouped_birthdays.items():
        print('{}: {}'.format(weekday, ', '.join(people_list)))
