#%% import biblioteker
from datetime import datetime
from datetime import date
from datetime import timedelta
import pytz  # PycharmProjects TimeZone

#%%
onow = date.day
print(onow)

#%%
dtime = datetime(2023, 10, 30)
print(dtime)

now = datetime.now(pytz.timezone('Asia/Kolkata'))
print(now)
print(now.isoformat())

#%% Tidssoner
for timezones in pytz.all_timezones:
    print(f"{timezones}: {datetime.now(pytz.timezone(timezones))}")

#%% kode med navn
for code, name in pytz.country_names.items():
    print(code, ":", name)

#%% Manuelt
dt_time = datetime(2023, 10, 30, 9, 23, 00)
print(dt_time.year)
print(dt_time.month)
print(dt_time.day)
print(dt_time.hour, dt_time.minute)

#%% Konvertere til manuell streng
str_date = dt_time.strftime('%Y-%m-%d. %H:%M. Uke %W')
print(str_date)

#%% beregne tid - timedelta-klasse
today = datetime.now()
print(today)

new_date = today + timedelta(days=30)
print(new_date)

#%% Tidsdifferanse
dato_a = datetime(2017, 4, 12, 19, 7)
dato_b = datetime(2023, 10, 29, 20, 00)

dato_diff = dato_b - dato_a
print(dato_diff)

antall_dager = dato_diff.days
print(antall_dager)
