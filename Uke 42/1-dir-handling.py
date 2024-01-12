import os
import shutil

# Finner nåværende path (mappe i fylsystemet)
current_dir = os.getcwd()
print("")
print(current_dir)

# Lage en ny mappe fra der vi står i utgangspunktet
# Vi sjekker at mappen ikke finner fra før av
ny_mappe = os.path.join(current_dir, "ny_mappe")
if not os.path.exists(ny_mappe):
    os.mkdir("ny_mappe")
    print(f"Opprettet mappen {ny_mappe}")
else:
    print(f"Mappen {ny_mappe} finnes fra før")

# Slette 'ny_mappe'
if os.path.exists(ny_mappe) and os.path.isdir(ny_mappe):
    os.rmdir(ny_mappe)
    print(f"Slettet mappen {ny_mappe}")
else:
    print(f"{ny_mappe} finnes ikke.")

# Vi oppretter mappestruktur
multiple_dirs = os.path.join(current_dir, "M1", "M2", "M3")
if not os.path.exists(multiple_dirs):
    os.makedirs(multiple_dirs)
    print(f"Opprettet mappestrukturen {multiple_dirs}")
else:
    print(f"Mappestrukturen {multiple_dirs} finnes allerede")

# Vi sletter alle mapper
remove_dirs = os.path.join(current_dir, "M1")
if os.path.exists(remove_dirs) and os.path.isdir(remove_dirs):
    print(f"Slettet mappestrukturen {remove_dirs}")
    shutil.rmtree(remove_dirs)
else:
    print(f"Mappestrukturen {remove_dirs} finnes ikke")
