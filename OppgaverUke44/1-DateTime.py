import random
from datetime import datetime, date, timedelta, time
import time as tme
import pytz  # PycharmProjects TimeZone

print("Oppgave 1")
#%% Skriv et program som skriver ut dagens dato.
today_date = date.today()
print(f"Dagens dato: {today_date}")

#%% Lag et program som skriver ut dagens dato og tid.
today_date_and_time = datetime.now().strftime('%Y-%m-%d. %H:%M.')
print(f"Dagens tid og dato: {today_date_and_time}")

#%% Lag et program som skriver ut gårsdagens dato.
yesterday = today_date - timedelta(days=1)
print(f"Gårsdagens dato: {yesterday}")

print("\nOppgave 2")
#%% Skriv et program som legger til 5 dager til dagens dato og skriver den ut.
today_plus_5 = today_date + timedelta(days=5)
print(f"Dagens dato pluss 5 dager er: {today_plus_5}")

#%% Skriv et program som trekker 10 dager fra dagens dato og skriver den ut.
today_minus_10 = today_date - timedelta(days=10)
print(f"Dagens dato minus 10 dager er: {today_minus_10}")

#%% Lag et program som legger til 2 uker til dagens dato.
today_plus_2_weeks = today_date + timedelta(weeks=2)
print(f"Dato om 2 uker er: {today_plus_2_weeks}")

print("\nOppgave 3")
#%% Skriv et program som legger til 30 minutter til gjeldende tid.
now_plus_30min = (datetime.now() + timedelta(minutes=30)).strftime('%H:%M')
print(f"Klokkeslett om 30 minutter er: {now_plus_30min}")

# Lag et program som trekker 15 minutter fra gjeldende tid.
now_minus_15min = (datetime.now() - timedelta(minutes=15)).strftime('%H:%M')
print(f"Klokkeslett for 15 minutter siden var: {now_minus_15min}")

print("\nOppgave 4")
#%% Skriv et program som konverterer en streng til et datetime objekt ("2023-10-05").
some_day_str = "2023-10-05"
some_day = datetime.strptime(some_day_str, '%Y-%m-%d').date()
print(f"En string til dato- objekt: {some_day}")

#%%	Skriv et program som konverterer et datetime objekt til en streng i formatet "dd-mm-yyyy".
today_date_str = today_date.strftime('%d-%m-%Y')
print(f"Dagens dato: {today_date_str}")

print("\nOppgave 5")
#%% Lag et program som regner ut antall dager mellom to gitt datoer.
date_a = datetime(1990, 10, 30)
date_b = datetime.now()

date_diff = (date_b - date_a).days
print(f"Jeg har levd i {date_diff} dager.")

#%%	Skriv et program som finner antall sekunder mellom nåværende tidspunkt og midnatt.
time_now = datetime.now().time()
midnight = time(0, 0)
seconds_to_midnight = (datetime.combine(datetime.today(), midnight) -
                       datetime.combine(datetime.today(), time_now)).seconds
print(f"Det er {seconds_to_midnight} sekunder til midnatt.")

print("\nOppgave 6")
#%% Skriv et program som finner hvilken ukedag det er i dag (f.eks. Mandag, Tirsdag).
today_weekday = datetime.today().strftime('%A')
print(f"Todays weekday is {today_weekday}.")


#%%	Lag et program som finner ut om en gitt dato er en helgedag (lørdag eller søndag).
def create_random_date():
    start = datetime(1990, 1, 1)
    years = 2023 - 1990 + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


random_date = create_random_date()
random_date_str = random_date.strftime('%d-%m-%Y')
random_date_weekday = random_date.strftime('%A')
if random_date_weekday in ['Saturday', 'Sunday']:
    print(f'Picked a random date: {random_date_str}. This was a {random_date_weekday}, which is the weekend.')
else:
    print(f'Picked a random date: {random_date_str}. This was a {random_date_weekday}, which is not the weekend.')

print("\nOppgave 7")
#%%	Skriv et program som beregner hvor mange dager det er igjen til neste nyttårsaften.
new_years = datetime(datetime.now().year, 12, 31).date()
days_until_newyears = (new_years - today_date).days
print(f"Det er {days_until_newyears} dager igjen til årets nyttårsaften.")

#%%	Lag et program som sjekker om dagens dato er en spesiell dato
# (som f.eks. Valentinsdagen) og skriver ut en passende melding.
today_date = date.today()
valentines_day = datetime(datetime.now().year, 2, 14).date()
norway_constitution_day = datetime(datetime.now().year, 5, 17).date()
dog_day = datetime(datetime.now().year, 8, 26).date()
mental_health_day = datetime(datetime.now().year, 10, 10).date()
christmas_eve = datetime(datetime.now().year, 12, 24).date()
new_years = datetime(datetime.now().year, 12, 31).date()

if today_date == valentines_day:
    print("I dag er valentines dagen! Har du funnet deg en date for dagen?")
elif today_date == norway_constitution_day:
    print("I dag er nasjonaldagen. Gratulerer med dagen!")
elif today_date == dog_day:
    print("I dag er den internasjonale hunde- dagen. Gratulerer alle firebeinte!")
elif today_date == mental_health_day:
    print("I dag er den internasjonale 'mental helse'- dagen. Husk å ta vare på de rundt deg.")
elif today_date == christmas_eve:
    print("I dag er det julaften! Åpne gavene dine NÅÅ!")
elif today_date == new_years:
    print("I dag er det nyttårsaften! Godt nytt år når klokken slår 12!")
else:
    print("I dag er bare en helt vanlig hverdag. Gjør den til en spesiell en!")

print("\nOppgave 8")
#%% Lag et program som viser nåværende tid i en annen tidssone (f.eks. UTC).
time_england = (datetime.now(pytz.timezone('Europe/London'))).strftime('%H:%M')
print(f"Lokal tid i England er nå {time_england}.")

#%% Skriv et program som konverterer tidspunkt fra en tidssone til en annen.
source_timezone = pytz.timezone('Europe/Oslo')
time_now = datetime.now(source_timezone)
timezones = {
    1: pytz.timezone('Europe/Helsinki'),        # Finland
    2: pytz.timezone('Europe/Astrakhan'),       # Astrakhan, Russia
    3: pytz.timezone('Pacific/Honolulu')        # Hawaii
}
convert_timezone = int(input("Skriv inn tall for å vise lokaltid i (1) Finland (2) Astrakhan/Russland (3) Hawaii: "))
if convert_timezone in timezones:
    target_timezone = timezones[convert_timezone]
    converted_time = time_now.astimezone(target_timezone)
    print(f"Tiden nå i tidssonen du valgte er {converted_time.strftime('%H:%M gmt%z')}")
else:
    print("Ugyldig valg av tidssone")

print("\nOppgave 9")
#%% Skriv et program som beregner en persons alder basert på deres fødselsdato.
steve_jobs_birth = datetime(1955, 2, 24)
steve_jobs_death = datetime(2011, 10, 5)
steve_jobs_age = (steve_jobs_death - steve_jobs_birth).days/365
print(f"Steve jobs ble {int(steve_jobs_age)} år gammel.")

#%%	Lag et program som bestemmer om en person er gammel nok til å kjøre bil (18 år i de fleste land).
print("Type in your birthday (DD/MM/YYYY):")
day = input("Day: ")
month = input("Month: ")
year = input("Year: ")
birthday_str = f"{year}-{month}-{day}"
birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
today = datetime.today().date()
if (today - birthday).days/365 > 18:
    print("Du er gammel nok til å kjøre bil.")
else:
    print("Du er ikke gammel nok til å kjøre bil.")

print("\nOppgave 10")
#%% Skriv et program som teller ned sekunder til en spesifisert fremtidig tidspunkt (f.eks. et nytt år).
time_now = datetime.now()
time_now_plus_10_seconds = time_now + timedelta(seconds=10)
print("10 Sekunders nedtelling:")
while True:
    time_now = datetime.now()
    time_difference = time_now_plus_10_seconds - time_now
    if time_difference.total_seconds() <= 0:
        print("BOOOOOOOOOOOOOM!")
        break
    remaining_seconds = int(time_difference.total_seconds()) + 1
    print(f"Sekunder igjen: {remaining_seconds}")
    tme.sleep(1)

#%% Lag et program som sammenligner to gitt datoer og bestemmer hvilken som er tidligst.
date_c = datetime(1990, 10, 30)
date_d = datetime(1994, 12, 16)
if date_c < date_d:
    print("Morten er eldst.")
else:
    print("Kine er eldst.")
