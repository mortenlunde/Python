#%% 1. Skriv et program som ber brukeren om å oppgi et tall,
# konverterer input til et heltall, og skriver ut dobbelt så mye.
int_input = input("Skriv inn ett tall: ")
int_input = int(int_input) * 2
print(f"Det dobbelte av tallet du skrev inn er: {int_input}")

#%% 2. Skriv et program som ber brukeren om å oppgi et tall,
# konverterer input til et flyttall, og skriver ut halvparten av tallet.
float_input = input("Skriv inn et tall: ")
float_input = float(float_input) / 2
print(f"Halvparten av tallet du skrev inn er: {float_input}")

#%% 3 Skriv et program som ber brukeren om å oppgi to tall, konverterer
# input til heltall, og skriver ut summen av tallene.
tall_input_1 = input("Skriv inn tall nummer 1: ")
tall_input_2 = input("Skriv inn tall nummer 2: ")
input_sum = int(tall_input_1) + int(tall_input_2)
print(f"Summen av tallene du skrev inn er: {input_sum}")

#%% 4. Skriv et program som ber brukeren om å oppgi to tall,
# konverterer input til flyttall, og skriver ut produktet av tallene.
float_input_1 = input("Skriv inn tall nummer 1: ")
float_input_2 = input("Skriv inn tall nummer 2: ")
float_sum = float(float_input_1) * float(float_input_2)
print(f"Produktet av tallene du skrev inn er: {float_sum}")

#%% 5. Skriv et program som ber brukeren om å oppgi en tekststreng og
# et tall, konverterer tallet til et heltall, og skriver ut tekststrengen det spesifiserte antallet ganger.
tekst_input = input("Skriv inn en tekst: ")
repeat_input = int(input("Hvor mange ganger ønsker du å skrive ut teksten?: "))
for _ in range(repeat_input):
    print(tekst_input)
