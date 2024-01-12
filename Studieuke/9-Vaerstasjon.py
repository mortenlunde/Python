import os
import sys
import datetime

weather_data_list = []
default_date = datetime.datetime.now()
print("Morten Værstasjon 1.0")


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def is_valid_temperature(temp_str):
    try:
        temp = float(temp_str)
        return -100.0 <= temp <= 100.0
    except ValueError:
        return False


def is_valid_precipitation(precip_str):
    try:
        precipitation = float(precip_str)
        return precipitation >= 0.0
    except ValueError:
        return False


def add_data():
    date = input(f"Skriv inn dato (dd-mm-åååå) (Dagens dato dersom du ikke taster noe): ")
    if not date:
        date = default_date.strftime('%d-%m-%Y')
    elif not is_valid_date(date):
        print("Ugyldig datoformat. Bruk formatet dd-mm-åååå.")
        return None
    temp = input("Skriv inn temperatur (Celsius): ")
    if not is_valid_temperature(temp):
        print("Ugyldig temperaturverdi. Skriv inn en gyldig temperatur i Celsius.")
        return None
    cond = input("Skriv inn værforhold (Sol, regn, snø etc): ").capitalize()
    precipitation = input("Skriv inn nedbør (Millimeter): ")
    if not is_valid_precipitation(precipitation):
        print("Ugyldig nedbørverdi. Skriv inn en gyldig nedbørsmengde i millimeter.")
        return None
    return {
        'date': date,
        'temp': temp,
        'cond': cond,
        'precipitation': precipitation
    }


def easter_egg():
    print("Kona til sin programmerer-mann: Kan du gå på butikken å kjøpe en liter melk? Og hvis de har egg, kjøp 12.\n"
          "15 minutter kommer mannen hjem med 12 liter melk.\n"
          "Kona: Hvorfor i alle dager kjøpte du 12 liter melk?)\n"
          "Mannen: De hadde egg.")
    input("Vil du høre en vits til? ")
    print("Uansett hva du tastet så får du en vits til:")
    print("Why do frontend developers eat lunch alone?\nThey don't know how to join tables.")


def program():
    while True:
        global weather_data_list
        clear_console()
        print("Hovedmeny:\n1. Legg til ny data\n2. Vis lagrede data\n3. "
              "Slette data\n4. Overaskelse\n5. Avslutt program")
        menu = input("Velg 1, 2, 3, 4 eller 5: ")

        if menu == "1":
            weather_data = add_data()
            weather_data_list.append(weather_data)
            clear_console()
        elif menu == "2":
            if not weather_data_list:
                print("Ingen data tilgjengelig. Vennligst legg til data først.")
            else:
                print("Lagret vær-data:")
                for i, data in enumerate(weather_data_list, 1):
                    print(f"Oppføring #{i}:")
                    print(f"Dato: {data['date']}")
                    print(f"Temperatur: {data['temp']}°C")
                    print(f"Værforhold: {data['cond']}")
                    print(f"Nedbør: {data['precipitation']} mm")
                    print()
                if weather_data_list:
                    print("Analyse av tempratuerer:")
                    lowest_temp = min(data['temp'] for data in weather_data_list)
                    print(f"Laveste registrerte temperatur: {lowest_temp}")
                    highest_temp = max(data['temp'] for data in weather_data_list)
                    print(f"Laveste registrerte temperatur: {highest_temp}")
                    avg_temp = sum(float(data['temp']) for data in weather_data_list) / len(weather_data_list)
                    print(f"Gjennomsnittstemperatur: {avg_temp:.2f}°C")
                input("Trykk Enter for å fortsette...")
            clear_console()
        elif menu == "3":
            if not weather_data_list:
                print("Ingen data tilgjengelig for sletting.")
            else:
                g = input("Hvilket datasett ønsker du å fjerne?")
                if g.isdigit():
                    if 0 < int(g) <= len(weather_data_list):
                        weather_data_list.pop((int(g) - 1))
                else:
                    print("Du skrev inn et ugyldig tall. Prøv igjen.")
            clear_console()
        elif menu == "4":
            easter_egg()
            input("Trykk Enter for å fortsette...")
            clear_console()
        elif menu == "5":
            exit()
        else:
            print("Ugyldig menyvalg. Prøv igjen.")


while True:
    program()
