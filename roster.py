from sys import argv, exit
import sys
import csv
from cs50 import SQL

# Check command-line arguments
if len(argv) != 2:
    print("missing command-line argument")
    exit(1)

db = SQL("sqlite:///students.db")

result = db.execute("""SELECT first, middle, last, birth
    FROM students WHERE house = (?) ORDER BY last, first""", argv[1])

for row in result:
    birth = row["birth"]
    if row["middle"] is not None:
        name = f'{row["first"]} {row["middle"]} {row["last"]}'
    else:
        name = f'{row["first"]} {row["last"]}'

    print(name + ", " + "born " + str(birth))

exit(0)
