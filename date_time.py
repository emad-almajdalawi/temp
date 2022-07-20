from datetime import datetime, timedelta, timezone, date, time
import pytz

# tz = timezone("EST")
# tz2 = timezone(timedelta(hours=8))
now = datetime.now()
today = datetime.today()

print("now", now)
print("today", today)
print("year:", today.year)
print("month", today.month)
print("day", today.day)
print("hour", today.hour)
print("minute", today.minute)
print("second", today.second)
print("microsecond", today.microsecond)
print("strftime:", today.strftime("%a, %Y %B %d - %H:%M:%S"))
print("strftime:", today.strftime("%I:%M %p"))
print(datetime.fromisoformat("1997-09-09 12:30:05:000000"))

print("-----------------------------------------------------")

print(date(1997, 9, 9))
print(date.fromisoformat("1997-09-09"))
print(date(1997, 9, 9).weekday())

print("-----------------------------------------------------")

print(time.fromisoformat("12:30:05"))
print(time(15, 45, 50))
print(time(15, 45, 50).strftime("%I:%M %p"))

print("-----------------------------------------------------")

the_date = date(1997, 9, 9)
the_time = time(15, 45, 50)
combined = datetime.combine(the_date, the_time)
print(combined)

print("-----------------------------------------------------")

# print(pytz.all_timezones)
tz = pytz.timezone("Asia/Amman")
print(tz)
print("now:", datetime.now(), "---- Amman:", datetime.now(tz))
print("tzinfo", today.tzinfo)
print("utcnow", datetime.utcnow())
print("utcnow", datetime.utcnow().isoformat())
print("utcnow", datetime.utcnow().isoformat(timespec="seconds"))
print("utcnow", datetime.utcnow().isoformat(sep="-"))
print("delta:", datetime.utcnow() - datetime.now())
print("delta 3h:", datetime.utcnow() + timedelta(hours=3))
print("delta 5d:", datetime.now() - timedelta(days=5))
