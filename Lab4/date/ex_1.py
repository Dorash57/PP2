import datetime

current_date=datetime.datetime.now()
print("Current date:", current_date.strftime("%Y-%m-%d"))

new_date=current_date-datetime.timedelta(days=5)
print("New date:", new_date.strftime("%Y-%m-%d"))