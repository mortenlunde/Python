#%% ascii -> bytes
tekst = 'æøå'
bts = tekst.encode('iso-8859-1')
print(bts)
print([b for b in bts])
print([chr(b) for b in bts])

#%%
print(bts)
ascii_tekst = bts.decode('iso-8859-1')
print(ascii_tekst)

#%%
tekst = 'æøå'
utf8_tekst = tekst.encode('utf-8')
print(utf8_tekst)
print([b for b in utf8_tekst])
print([chr(b) for b in utf8_tekst])

#%%
tekst = 'æøå'
utf8_tekst = tekst.encode('utf-8')
print(utf8_tekst)
print([b for b in utf8_tekst])
print([bin(b) for b in utf8_tekst])

#%% Plukke ut bits
des_verdi = int('000011100110', 2)
print(des_verdi)
print(chr(des_verdi))

#%%
tekst = 'abc'
utf8_tekst = tekst.encode('utf-8')
hex_verdi = utf8_tekst.hex()
print(hex_verdi)
bts = bytes.fromhex(hex_verdi)
print(bts)
