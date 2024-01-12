#%% Opprett en dictionary med 5 nøkkel-verdi par, der nøklene er frukt og verdiene er deres farger.
fruit_dict = {"Apple": "Red", "Orange": "Orange", "Pear": "Green", "Banana": "Yellow", "Watermelon": "Green/Red"}
print(f"Oppgave 01: {fruit_dict}")

#%% Legg til et nytt nøkkel-verdi par til den eksisterende dictionaryen.
fruit_dict.update({"Lime": "Green"})
print(f"Oppgave 02: {fruit_dict}")

#%% Slett et nøkkel-verdi par fra dictionaryen ved hjelp av nøkkelen.
del fruit_dict["Orange"]
print(f"Oppgave 03: {fruit_dict}")

#%% Bruk en for-løkke for å skrive ut alle nøklene i dictionaryen.
print("Oppgave 04:", end=" ")
for k in fruit_dict:
    print(k, end=" ")

#%% Bruk en for-løkke for å skrive ut alle verdiene i dictionaryen.
print("\nOppgave 05:", end=" ")
for v in fruit_dict:
    print(fruit_dict[v], end=" ")

#%% Fra to lister: Gitt to lister keys = ['a', 'b', 'c'] og values = [1, 2, 3],
# lag en dictionary ved å koble sammen elementene fra begge listene.
abc_list = ["a", "b", "c"]
num_list = [1, 2, 3]
abc_num_dict = dict(zip(abc_list, num_list))
print(f"\nOppgave 06: {abc_num_dict}")

#%% Fra liste med tupler: Gitt en liste med tupler items = [('a', 1), ('b', 2), ('c', 3)],
# konverter den til en dictionary.
my_tuples = [('a', 1), ('b', 2), ('c', 3)]
nokkel, verdi = zip(*my_tuples)
my_dict = dict(zip(nokkel, verdi))
print(f"Oppgave 07: {my_dict}")

#%% Nøkler fra liste, fast verdi: Gitt en liste ['apple', 'banana', 'cherry'], lag en dictionary
# hvor hvert element i listen er en nøkkel, og verdien for hver nøkkel er 'fruit'.
sweet_fruits = ['apple', 'banana', 'cherry']
sweet_dict = dict(zip(sweet_fruits, ["Fruit"] * len(sweet_fruits)))
print(f"Oppgave 08: {sweet_dict}")

#%% Fra liste, bruk indeks: Gitt en liste ['zero', 'one', 'two', 'three'], lag en dictionary
# hvor nøklene er indeksene (0, 1, 2, osv.) og verdiene er elementene fra listen.
number_list = ['zero', 'one', 'two', 'three']
number_dict = dict(enumerate(number_list))
print(f"Oppgave 09: {number_dict}")

#%% Opprett nested dictionary: Gitt to lister students = ['Anna', 'Bob', 'Charlie'] og grades = [85, 90, 78],
# lag en dictionary hvor hver student er en nøkkel, og verdien er en annen dictionary med nøkkel-verdi
# par for fag (f.eks. 'math') og karakter
students = ['Anna', 'Bob', 'Charlie']
grades = [85, 90, 78]
subjects = ["Math", "Gymnastics", "History"]
report_card = {}

for student, grade, subject in zip(students, grades, subjects):
    if student not in report_card:
        report_card[student] = {}
    report_card[student][subject] = grade

print(f"Oppgave 10: {report_card}")
