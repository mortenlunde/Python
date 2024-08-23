import tkinter as tk
from tkinter import messagebox

def submit():
    try:
        # Validerer at input i lånesum og lengde er heltall
        loan_amount = int(entry_a.get())
        months = int(entry_b.get())

        # Validerer at rente er float, og konverterer eventuelt komma til punktum for å hindre program i å krasje
        rate_str = entry_c.get().replace(',', '.')
        rate = float(rate_str)

        # Kalkulerer totalsum for lån og månedlig nedbetaling
        rate_per_month = rate / 100 / 12
        payment = (rate_per_month / (1 - (1 + rate_per_month) ** (-months))) * loan_amount
        total_cost = payment * months

        # Skriver ut resultat
        result_label.config(text="Total kostnad: Kr " + str(round(total_cost, 2)))
        monthly_label.config(text="Månedlig betaling: Kr " + str(round(payment, 2)))

    # Gir feillmelding i pop-up vindu
    except ValueError:
        messagebox.showerror("Input Error", "For lånesum og lengde på lån er kun hele tall tillat. For "
                                            "rente er det tillat med heltall og kommaseparert tall.")

# Generer et vindu
window = tk.Tk()

# Generer en tekst og en input- boks
label_a = tk.Label(window, text="Skriv inn lånesum")
label_a.pack()
entry_a = tk.Entry()
entry_a.pack()

# Generer en tekst og en input- boks
label_b = tk.Label(window, text="Skriv inn lengde på lån (måneder)")
label_b.pack()
entry_b = tk.Entry()
entry_b.pack()

# Generer en tekst og en input- boks
label_c = tk.Label(window, text="Skriv inn effektiv rente (%)")
label_c.pack()
entry_c = tk.Entry()
entry_c.pack()

# Knapp for å utføre beregning
myButton = tk.Button(window, text="Beregn", width=10, command=submit)
myButton.pack()

# Viser totalsum for lånet
result_label = tk.Label(window, text="")
result_label.pack()

# Viser månedlig nedbetaling
monthly_label = tk.Label(window, text="")
monthly_label.pack()

# Kjør programmet
window.mainloop()
