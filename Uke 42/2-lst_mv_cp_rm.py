import os
import shutil

# Lister opp alle filer vi har i pathen
dir_content = os.listdir()

for content in dir_content:
    print(f"{content}: Er en mappe: {os.path.isdir(content)}, Er en fil {os.path.isfile(content)}")

# Gi nytt navn på fil
org_name = "test.txt"
new_name = "test.log"
org_name_2 = "testt.txt"
if (not os.path.exists(org_name) and os.path.isfile(org_name)
        and not os.path.exists(new_name)):
    os.rename(org_name, new_name)
    print(f"Endret navn på {org_name} til {new_name}")
else:
    print(f"Filen {new_name} finnes allerede")

# Flytte filer
# shutil.move(org_name, new_name)

# Kopiere filer
cpy_name = f"copy_{org_name_2}"
if os.path.exists(org_name_2) and os.path.isfile(org_name_2) and not os.path.exists(cpy_name):
    shutil.copy2(org_name_2, cpy_name)
    print(f"Kopierer {org_name_2} til {cpy_name}")
else:
    print("Original fil finnes ikke, eller kopi finnes fra før")

# Sletting av fil
if os.path.exists(cpy_name) and os.path.isfile(cpy_name):
    os.remove(cpy_name)
    print(f"Slettet filen {cpy_name}")
else:
    print("Filen finnes ikke")
