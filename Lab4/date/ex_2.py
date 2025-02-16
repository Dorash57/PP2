import datetime

today_date=datetime.datetime.now()
yesterday_date=today_date-datetime.timedelta(days=1)
tomorrow_date=today_date+datetime.timedelta(days=1)

print("Yesterday:", yesterday_date.strftime("%Y-%m-%d"))
print("Today:", today_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow_date.strftime("%Y-%m-%d"))