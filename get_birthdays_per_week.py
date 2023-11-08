from collections import defaultdict
from datetime import datetime
from birthday_utils import get_birthday_weekday

def get_birthdays_per_week(users):
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
            weekday = get_birthday_weekday(birthday_weekday)
            grouped_birthdays[weekday].append(name)


    for weekday, people_list in grouped_birthdays.items():
        print('{}: {}'.format(weekday, ', '.join(people_list)))

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 11, 11)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 11, 12)},
    {"name": "Kim Kardashian", "birthday": datetime(1955, 11, 10)},
    {"name": "Jan Koum", "birthday": datetime(1955, 11, 10)},
]

get_birthdays_per_week(users)
