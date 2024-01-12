import base64
#%%
base64_string = " R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
print(base64_string)
base64_bytes = base64_string.encode("ascii")
print(base64_bytes)

sample_string_bytes = base64.b64decode(base64_bytes)
print(sample_string_bytes)
sample_string = sample_string_bytes.decode("ascii")
print(f"Decoded string: {sample_string}")

#%%
data = 'Yngve'
data_as_bytes = data.encode('utf-8')
bs64_data = base64.b64encode(data_as_bytes)
print(bs64_data)    # print bytes
print(bs64_data.decode('utf-8'))    # Print string

#%%
tekst = 'WW5ndmU='
tekst_decoded = base64.b64decode(tekst)
tekst_decoded_utf8 = tekst_decoded.decode('utf-8')
print(tekst_decoded)
print(tekst_decoded_utf8)
