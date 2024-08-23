# Hvorfor får vi forskjellige resulater av disse testene?

####################
###### TEST A ######
####################
x = "a" * 100
y = "a" * 100
print(x is y)

a = "a" * 10000
b = "a" * 10000
print(a is b)

####################
###### TEST B ######
####################

c = "py" + "thon"
d = "python"
print(c is d)

d = "py"
e = d + "thon"
f = "python"
print(e is f)

d = "py"
e = d + "thon"
f = "python"
print(e == f)

# Svar:
# Når vi sammenligner med 'is' så ser vi om objektet referer til den samme minneadressen.
# Når vi sammenligner med == så ser vi om to objekter har samme verdi.
# Python gjenbruker minneaddresser ved korte strenger, men for lengre eller kombinerte strenger
# så brukes ikke minneaddressene alltid på nytt. Vi vil derfor kunne få False.