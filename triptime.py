# ...existing code...

from datetime import datetime, timedelta
def main():
	# Get user input
	miles = int(input("Enter the number of miles for your trip (integer): "))
	mph = int(input("Enter your average speed in miles per hour (integer): "))
	dep_date = input("Enter the date of departure (YYYY-MM-DD): ")
	dep_time = input("Enter the time of departure (HH:MM AM/PM): ")

	# Parse departure datetime
	dep_datetime_str = dep_date + ' ' + dep_time
    dep_datetime = datetime.strptime(dep_datetime_str, "%Y-%m-%d %I:%M %p")

	# Calculate trip duration
	total_hours = miles // mph
	total_minutes = round((miles / mph - total_hours) * 60)

	# Calculate arrival datetime
	duration = timedelta(hours=total_hours, minutes=total_minutes)
	arr_datetime = dep_datetime + duration

	# Output results
	print(f"\nTrip duration: {total_hours} hours and {total_minutes} minutes")
	print(f"Estimated date of departure: {dep_datetime.strftime('%Y-%m-%d')}")
	print(f"Estimated time of departure: {dep_datetime.strftime('%I:%M %p')}")
	print(f"Estimated date of arrival: {arr_datetime.strftime('%Y-%m-%d')}")
	print(f"Estimated time of arrival: {arr_datetime.strftime('%I:%M %p')}")

if __name__ == "__main__":
	main()
