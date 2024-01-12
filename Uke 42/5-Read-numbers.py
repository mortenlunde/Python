import os
import sys

FILE = "numbers.csv"
if os.path.exists(FILE):
    with open(FILE, "r") as fopen:
        line = fopen.readline().rstrip("\n")
        while line:
            line_sum = 0
            arr_num = line.split(",")
            for num_str in arr_num:
                if num_str.isdigit():
                    num_int = int(num_str)
                    line_sum += num_int
            print(" + ".join(arr_num), " = ", line_sum)
            line = fopen.readline().rstrip("\n")
else:
    print(f"Fant ikke filen {FILE} - avslutter programmet.")
    sys.exit()
