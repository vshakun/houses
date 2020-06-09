from sys import argv, exit
import sys
import csv
from cs50 import SQL

# Check command-line arguments
if len(argv) < 2:
    print("missing command-line argument")
    exit(1)

# Create table called `shows`, and specify the columns
open(f"students.db", "w").close()
db = SQL("sqlite:///students.db")
db.execute("""CREATE TABLE students (first TEXT, middle TEXT,
    last TEXT, house TEXT, birth NUMERIC)""")

# Open CSV file
with open(" ".join(argv[1:]), "r") as characters:

    # Create DictReader
    characters_file = csv.DictReader(characters)

    # Iterate over CSV file
    for row in characters_file:
        # Splitting names
        words = row["name"].split()

        first_name = words[0]
        last_name = words[-1]

        if len(words) == 3:
            middle_name = words[1]
        else:
            middle_name = None

        house = row["house"]
        birth = row["birth"]

        db.execute("""INSERT INTO students (first, middle,
            last, house, birth) VALUES(?, ?, ?, ?, ?)
            """, first_name, middle_name, last_name, house, birth)


exit(0)
