from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    
    if not users:
        return {}
    today = datetime.today().date()
    birthdays_per_week = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            birthday_date = today + timedelta(days=delta_days)
            if birthday_date.weekday() >= 5:  # Вихідні (субота або неділя)
                next_monday = today + timedelta(days=(7 - today.weekday()))
                day_of_week = next_monday.strftime("%A")
            else:
                day_of_week = birthday_date.strftime("%A")

            birthdays_per_week[day_of_week].append(name)
            
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")
        else:
            print(f"No birthdays on {day}")