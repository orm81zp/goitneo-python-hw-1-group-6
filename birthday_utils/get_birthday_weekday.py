WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
LAST_WORK_DAY = 4

def get_birthday_weekday(birthday):
    return WEEKDAYS[0] if birthday > LAST_WORK_DAY else WEEKDAYS[birthday]
