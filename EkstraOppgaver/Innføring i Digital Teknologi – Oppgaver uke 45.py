#%% Hva er fordelene og ulempene med analoge signaler?
"""
F: Analoge signaler er kontinuerlige og representerer data på en jevn måte over tid.
F: Analoge systemer kan være enklere å designe og implementere i visse tilfeller.
Dette gjelder spesielt for enklere kretser og elektronikk.
F: Noen ganger kan analoge signaler være mer effektive når det gjelder overføringshastighet,
spesielt i sanntidssituasjoner som taleoverføring.
F: Analoge signaler gir en mer naturtro representasjon av den virkelige verden, spesielt når det gjelder lyd og bilde.
Dette gjør dem ideelle for lydopptak og reproduksjon.
U: Analoge signaler er mer utsatt for støy og forvrengning under overføring,
noe som kan påvirke kvaliteten på signalet negativt.
U: Analoge signaler er vanskeligere å behandle og manipulere enn digitale signaler.
Digitale signaler tillater enklere og mer nøyaktig signalbehandling.
U: Analoge signaler har ingen innebygd mekanisme for feilkorrigering. Hvis signalet blir forstyrret,
kan det føre til tap av data uten mulighet for automatisk gjenoppretting.
U: Digital informasjon kan komprimeres mer effektivt og lagres på mindre plass.
"""

#%% Hva er fordelene og ulempene med digitale signaler?
"""
F: En av de mest betydningsfulle fordelene med digitale signaler er evnen til feilkorrigering. Digital informasjon kan 
gjenopprettes nøyaktig ved å bruke teknikker som feilkorrigering og redundans, noe som gjør digitale systemer mer 
pålitelige i forhold til støy og forvrengning under overføring.
F: Digitale signaler gir høy presisjon og nøyaktighet i representasjonen av data. Dette gjør dem spesielt egnet for 
applikasjoner der det er viktig å bevare dataintegritet.
F: Det er lettere å manipulere og prosessere digitale data.
F: Digitale signaler kan komprimeres effektivt, noe som resulterer i besparelser
i lagringsplass og overføringsbåndbredde.
F: Digitale systemer er svært fleksible og kan tilpasses ulike krav. Det er lettere å oppgradere og endre digitale
systemer uten å måtte endre hele infrastrukturen.
U: Digitale systemer kan være mer komplekse å designe og implementere sammenlignet med analoge systemer, spesielt i 
enkelte applikasjoner der enkle kretser er tilstrekkelige.
U: noen tilfeller kan digitale signaler være følsomme for signalintegritet, spesielt over lengre avstander. Dette kan 
kreve bruk av spesialisert utstyr for å opprettholde signalkvaliteten.
U: Digitale signaler kan ha en rundreise forsinkelse, noe som refererer til tiden det tar å konvertere et analogt signal
til digitalt, behandle det digitalt og deretter konvertere det tilbake til analogt.
U: Digitale signaler representerer data i diskrete nivåer, og dette kan føre til tap av informasjon i noen tilfeller.
Dette fenomenet kalles "kvantesprang," og det kan oppstå når kontinuerlige analoge signaler blir diskretisert.
"""

#%% Gjør søk og finn mer informasjon om disse og skriv et par linjer om DAC og ADC, og hva de gjør.
"""
En DAC (Digital to Analog Converter), eller D/A-konverter som den også kalles, omformer det digitale signalet til et 
analogt signal. I og med at en digital til analog converter sitter tidlig i signalveien har kvaliteten på denne stor 
betydning for hvor bra signal forsterkeren får å jobbe med. Om det forsvinner detaljer på veien før signalet går inn i 
forsterkeren er det for sent å rette opp i dette.
ADC - analog-til-digital omformer er et system som konverterer et analogt signal, slik som lyd plukket opp av en 
mikrofon eller lys inn et digitalt kamera, til et digitalt signal. Under konverteringsprosessen måler ADC den 
kontinuerlige analoge spenningen ved jevne intervaller og kvantiserer den til diskrete digitale verdier. Dette gjøres 
ved å tilordne digitale tall til de ulike nivåene av den analoge spenningen.
"""

#%% Skriv en kort tekst der du beskriver stegene for hvordan digitalisering av bilde eller video fungerer.
"""
Først samles analoge visuelle data ved hjelp av kameraer eller andre sensorer. Dette kan være i form av lys som 
registreres av kameraets bildebrikke eller som analoge videosignaler. Det analoge bildet eller videosignalet gjennomgår 
deretter en ADC- prosess. Dette trinnet innebærer å måle den analoge spenningen ved jevne intervaller og konvertere 
disse verdiene til digitale tall. Dette resulterer i en digital representasjon av det opprinnelige bildet eller videoen.
Den digitale informasjonen blir deretter behandlet ved hjelp av ulike digitale signalbehandlingsteknikker. Dette kan 
inkludere komprimering for å redusere filstørrelsen, justering av kontrast og farger, eller andre 
bildebehandlingsteknikker for å forbedre kvaliteten. Til slutt kan det digitale bildet eller videoen vises på digitale 
enheter som dataskjermer, TV-skjermer, eller projektorer. For å kunne visualisere det, må det digitale signalet 
konverteres tilbake til et analogt signal gjennom en Digital-til-Analog konverter (DAC) før det sendes til skjermen.
"""

#%% Hva er forkortelsene til bit og byte?
# b(it) og B(yte)

#%% Hvor mange bit er det i 4 byte?
# En byte består av 8 biter. 4 byte x 8 bit = 32 bit

#%% Hvor mange byte er det i 128 bit?
# 128 bit / 8 byte = 16 byte

#%% Se på bildet til høyre, forklar hvordan du leser informasjonen. Forklar forkortelsen Mbps
"""
93,5 Mbps (megabit per sekund). En megabit er 1 million biter. 4G i Norge støtter normalt sett opptil 100/150 Mbps.
I dette tilfellet er det mest sansynlig at bruker er tilkoblet 4G+ som støtter opptil minst 220 Mbps. 4G++ har en 
teoretisk topphastighet på 450 Mbps, og 5G kan ligge på opptil hele 2000 Mbps (2 Gbps).
"""

#%% I hvilke områder brukes det som oftest benevnelser med bit (kilobit, megabit osv.) Velg de som passer:
"""
a) Størrelsen på filer (en data file er 95 kilobit stor)
b) Hastighet på kablet nettverk (eks. megabit hastighet)
c) Hastighet på Internett (eks. 300 megabit per sekund)
Benevnelser med bit (kilobit, megabit, osv.) brukes ofte for å beskrive hastighetene til nettverk og 
overføringshastigheten av data. Hastigheter målt i biter per sekund er vanlige i disse sammenhengene, mens filstørrelser
ofte måles i bytes (kilobyte, megabyte, osv.). Derfor er alternativene b) og c) de mest passende i denne sammenhengen.
"""

#%% Du ønsker å gjennomføre en direktesending over Internett, datastrømmen skal være på HD nivå 1080p og 30 bilder
# pr. sekund.For å kontrollere datamengden velger du en bitrate på 6000 kb.

# a) Hvor mange megabyte/s med data tilsvarer 6000 kb pr. sekund?
# 1 MBps = 8000 kbps. 6000 kbps = 0,75 MBps

# b) Livesendingen sendes over 4G nettet fra en mobil telefon, abonnementet har en datakvote på 12GB (gigabyte).
# Hvor lenge kan livesendingen vare i timer.
# 12288 MB / 0,75 MB/s = 16384 s = 4.55 timer.


# c) Lag et Python skript hvor du kan variere bitrate for å få antall timer og minutter som resultat baser
# på informasjonen over.
def calculate_duration(_data_quota_gb, _bitrate_mb_per_s):
    data_quota_mb = _data_quota_gb * 1024
    duration_seconds = data_quota_mb / _bitrate_mb_per_s

    _duration_hours = int(duration_seconds // 3600)
    _duration_minutes = int((duration_seconds % 3600) // 60)

    return _duration_hours, _duration_minutes


data_quota_gb = 12
bitrate_mb_per_s = 0.75
duration_hours, duration_minutes = calculate_duration(data_quota_gb, bitrate_mb_per_s)

print(f"Livesendingen kan vare i {duration_hours} timer og {duration_minutes} minutter.")

# d) Hvor lang tid vil det ta hvis kvaliteten endres til 4K og sendes til YouTube?
bitrate_4k_mb_per_s = 20 / 8
duration_hours_4k, duration_minutes_4k = calculate_duration(data_quota_gb, bitrate_4k_mb_per_s)

print(f"Livesendingen i 4K-kvalitet kan vare i {duration_hours_4k} timer og {duration_minutes_4k} minutter.")


#%% Lag et Python skript som tar en tallverdi og skriver ut bokstaven i henhold til standard ASCII tabell
def number_to_ascii_char(number):
    try:
        char = chr(int(number))
        print(f"Den tilsvarende bokstaven/karakter er: {char}")
    except ValueError:
        print("Feil: Vennligst skriv inn en gyldig tallverdi.")


user_input = input("Skriv inn en tallverdi (32-126): ")
number_to_ascii_char(user_input)


#%% Lag et Python skript som tar en ASCII karakter og skriver ut tallverdien
def ascii_char_to_number(char):
    try:
        number = ord(char)
        print(f"Den tilsvarende tallverdien er: {number}")
    except TypeError:
        print("Feil: Vennligst skriv inn en gyldig ASCII-karakter.")


user_input = input("Skriv inn en ASCII-karakter: ")
ascii_char_to_number(user_input)
