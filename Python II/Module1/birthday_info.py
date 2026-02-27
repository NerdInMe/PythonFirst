# Birthday info program
from datetime import datetime, timedelta

def main():
    name = input("Enter your name: ")
    birth_str = input("Enter your birth date (MM/DD/YY): ")

    # Parse birth date
    try:
        birth_date = datetime.strptime(birth_str, "%m/%d/%y")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YY.")
        return

    today = datetime.now()
    # Adjust birth year if in the future
    if birth_date > today:
        birth_date = birth_date.replace(year=today.year - 1)

    # Birthday this year
    this_year_birthday = birth_date.replace(year=today.year)
    # If birthday already passed this year, next birthday is next year
    if this_year_birthday < today:
        next_birthday = this_year_birthday.replace(year=today.year + 1)
    else:
        next_birthday = this_year_birthday

    # Calculate age
    age_days = (today - birth_date).days
    if age_days >= 730:
        age = (today.year - birth_date.year)
        # Adjust if birthday hasn't happened yet this year
        if today < this_year_birthday:
            age -= 1
        age_str = f"{age} years"
    else:
        age_str = f"{age_days} days"

    # Days until next birthday
    days_until = (next_birthday.date() - today.date()).days
    if days_until == 0:
        bday_msg = f"{name}'s birthday is today!"
    elif days_until == 1:
        bday_msg = f"{name}'s birthday is tomorrow!"
    elif days_until == -1:
        bday_msg = f"{name}'s birthday was yesterday!"
    else:
        bday_msg = f"{name}'s birthday is in {days_until} days"

    # Output
    print(f"\n{name}'s birthday: {birth_date.strftime('%m/%d/%Y')}")
    print(f"Today: {today.strftime('%m/%d/%Y')}")
    print(f"{name}'s age: {age_str}")
    print(bday_msg)

if __name__ == "__main__":
    main()
