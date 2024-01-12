import csv
import os
import sys

FILE = 'solgtevarer.csv'
FILE_SOLUTION = 'salgs_analyse_svar.txt'

CATEGORIES = ['genser', 't-skjorte']
SIZES = ['s', 'm', 'l', 'xl', 'xxl']


def read_csv_file(file):
    """
    Denne funksjonen scanner CSV- filen og kjører flere if- sjekker for å utelukke feil på linjene, og hopper i
    i så fall over disse linjene.
    :param file: CSV-filen
    :return: Liste med lister som inneholder alle csv_data fra CSV-filen
    """
    csv_data = []

    with open(file, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        num_columns = len(next(csv_reader))
        for line_number, val in enumerate(csv_reader, start=2):
            if len(val) != num_columns:
                print(f'Feil format i filen. Ikke riktig antall kolonner på linje {line_number}.')
                continue
            if any(char.isdigit() for char in val[0]):
                print(f'Feil format i fornavn. Det tillates ikke med nummer i feltet. Linje {line_number}.')
                continue
            if any(char.isdigit() for char in val[1]):
                print(f'Feil format i etternavn. Det tillates ikke med nummer i feltet. Linje {line_number}.')
                continue
            if not val[2].lower() in CATEGORIES:
                print(f'Feil verdi i feltet for vare. Verdi må være {CATEGORIES}. Linje {line_number}.')
                continue
            if not val[4].lower() in SIZES:
                print(f'Feil verdi i feltet for størrelse. Verdi må være {SIZES}. Linje {line_number}.')
            if not val[5].isdigit():
                print(f'Feil format i antall- kolonnen. Verdien er ikke et tall. Linje {line_number}.')
                continue
            if not val[6].isdigit():
                print(f'Feil format i pris- kolonnen. Verdien er ikke et tall. Linje {line_number}.')
                continue
            if not val:
                print(f'Tom rad. Linje {line_number}.')
                continue
            csv_data.append(val)
    return csv_data


def analyze_sales(csv_data):
    """
    Denne funksjonen leser nå data som er hentet ut av forrige funksjon og analyserer data som er ønsket
    :param csv_data: Listen med lister fra forrige funksjon.
    :return: Returnerer resultater fra analysene som er kjørt til en tuple.
    """
    tot_sold_sweaters = 0
    income_of_sweaters = 0
    num_xl_items_sold = 0
    customers_with_over_3_items = 0
    selected_category = CATEGORIES[0]  # Genser
    selected_size = SIZES[3]  # XL
    colors = {}

    for row in csv_data:
        # A. Hvor mange gensere er solgt totalt?
        # B. Hva er den totale inntekten fra salget av Gensere?
        if row[2].lower() == selected_category:
            tot_sold_sweaters += int(row[5])
            income_of_sweaters += int(row[5]) * int(row[6])
        # C. Hvor mange kunder kjøpte varer i størrelsen 'XL'?
        if row[4].lower() == selected_size:
            num_xl_items_sold += 1
        # D. Hvor mange kunder har kjøpt mer enn 3 varer?
        if int(row[5]) > 3:
            customers_with_over_3_items += 1
        # E. Hvilken farge har flest solgte varer?
        color = row[3]
        quantity = int(row[5])
        if color not in colors:  # Vi legger til farge i dictinary om den ikke eksisterer
            colors[color] = 0
        colors[color] += quantity  # Vi legger inn antallet som ligger på linjen

    most_sold_color = max(colors, key=colors.get)
    most_sold_quantity = colors[most_sold_color]

    return (tot_sold_sweaters, income_of_sweaters, num_xl_items_sold, customers_with_over_3_items,
            [most_sold_color], most_sold_quantity)


def save_analysis_results(file, results):
    """
    Denne funksjonen skriver en ny fil (oppretter eller overskriver) med dataanalysen fra forrige funksjon.
    :param file: Filnavn på ny fil.
    :param results: Tuple med resultater fra forrige funksjon.
    :return: None
    """
    with open(file, 'w', encoding='utf-8') as output_file:
        output_file.write(f"A. Antall solgte gensere totalt: {results[0]}\n"
                          f"B. Total inntekt for alle gensere: {results[1]}\n"
                          f"C. Antall personer som har bestilt i XL: {results[2]}\n"
                          f"D. Antall personer som handlet mer enn 3 varer: {results[3]}\n"
                          f"E. Fargen det er solgt mest av er: {', '.join(results[4])} - {results[5]}")


def main():
    """
    Starter programmet og kaller på alle funksjoner. Skriver så ut feilmelding eller smelding om suksess.
    :return:
    """
    if not os.path.isfile(FILE):
        print(f"Finner ikke filen {FILE}")
        sys.exit()
    else:
        csv_data = read_csv_file(FILE)
        results = analyze_sales(csv_data)
        save_analysis_results(FILE_SOLUTION, results)
        print(f'Løsningen er skrevet til {FILE_SOLUTION}')


if __name__ == "__main__":
    main()
