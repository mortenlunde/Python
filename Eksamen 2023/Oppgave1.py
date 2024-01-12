# A. Skriv et program som ber brukeren om deres alder. Programmet skal deretter skrive ut alderen til konsoll.
# B. Les inn et heltall fra tastaturet og skriv det ut til konsoll. Hvis brukeren ikke taster inn et
# heltall, skal programmet gi en feilmelding og avsluttes.
# Her har jeg valgt å kombinere oppgave a og b siden jeg uansett ville kjørt feilhåndtering på oppgave a.
# Denne funksonen går også mot oppgave C, som også tar hensyn til om det er heltall eller desimaltall.

def check_input(prompt, datatype):
    """
    Denne funksjonen tar inn input fra bruker, samt datatype definert i koden hvor bruker skriver input,
    og returnerer heltall der det er mulig og ellers float rundet av til 2 desimaler. Dersom det ikke er
    int eller float (feks string) så vil funksjonen returnere feilmelding.
    :param prompt: Input fra bruker
    :param datatype: int eller float, definert i linjene som spør om input (29, 34 og 35)
    :return: input -> int(input) || float(input) eller feilkode
    """
    while True:
        user_input = input(prompt)
        try:
            result = datatype(user_input)
            if isinstance(result, float) and result.is_integer():
                return int(result)
            else:
                return round(result, 2)
        except ValueError:
            print('Ugyldig inntasting. Du må skrive inn et gyldig tall.')


def main():
    """
    Starter programmet og kaller på funksjonen. Svarer på spørsmålene i oppgaven.
    :return: None
    """
    user_age = check_input('Skriv inn din alder: ', int)
    age = user_age
    print(f"Din alder er {age} år.")

    # C. Skriv et program som ber brukeren om å skrive inn to tall, summerer disse og skrive resultatet til konsoll.
    num_1 = check_input('Skriv inn tall 1: ', float)
    num_2 = check_input('Skriv inn tall 2: ', float)
    num_sum = num_1 + num_2
    print(f'Summen av dine tall: {num_1} + {num_2} = {num_sum}')

    # D. Skriv et program som ber brukeren om å taste inn en setning. Programmet skal deretter
    # skrive ut hvor mange ord setningen består av.
    user_sentence = input('Skriv en en setning med flere ord: ')
    print(f'Antall ord i setningen din: {len(user_sentence.split(" "))}')

    # E. Fortsett programmet fra (D). Denne gang skal programmet skrive ut det lengste ordet i setningen.
    print(f'Det lengste ordet i setningen er: {max(user_sentence.split(" "), key=len)}')

    # F. Fortsett programmet fra (E). Nå skal programmet skrive ut den omvendte setningen. F.eks.
    # hvis brukeren skrev inn 'Python er gøy', skal programmet skrive ut 'gøy er Python'.
    reversed_sentence = ' '.join(user_sentence.split()[::-1])
    print(f'Setningen i reversert rekkefølge er: {reversed_sentence}')


if __name__ == "__main__":
    main()
