import textwrap

# Lærereren ønsker nå å utvide oppgaven og det skal nå legges til både multiplikasjon og divisjon til oppgavene
# som blir laget. Forklar med egne ord hva du som programmerer må gjøre for å utvide med denne funksjonaliteten.

svar = ('Her var det bare å legge til operatører i funksjonen som lager oppgavene - og sørge for at de genererte '
        'tallene ikke er null eller blir 0 til sammen. Da vil den generere nye tall. Like så i funksjonen som '
        'kalkulerer resultatet så legger vi bare til operatørene. Verre var det i '
        'grunn ikke når ting er laget med funksjoner.')

print(*textwrap.wrap(svar, 150), sep='\n')
