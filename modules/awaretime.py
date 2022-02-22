import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time {local_time}")
print(f"Naive UTC {utc_time}")

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time {aware_local_time}, time zone {aware_local_time.tzinfo}")
print(f"Aware UTC {aware_utc_time}, time zone {aware_utc_time.tzinfo}")

gap_time = datetime.datetime(2020, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 14457330000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print(f"{s} seconds since the epoch is {dt1}")
print(f"{t} seconds since the epoch is {dt2}")