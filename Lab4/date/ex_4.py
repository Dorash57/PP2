import datetime

date1=datetime.datetime.strptime(input("Enter date1 like this--> YY-MM-DD H:M:S  "), "%Y-%m-%d %H:%M:%S")
date2=datetime.datetime.strptime(input("Enter date2 like this--> YY-MM-DD H:M:S  "), "%Y-%m-%d %H:%M:%S")
time=date1-date2
print("Разница в секундах:", abs(time.total_seconds()))