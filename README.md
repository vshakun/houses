# CS50-PSet-7-Houses

This is my code of the program that imports student data into a database, and then produces class rosters, for Harvard's CS50 problems set 7.

## Specifications:

### In import.py, write a program that imports data from a CSV spreadsheet.

1. Program should accept the name of a CSV file as a command-line argument.
    * If the incorrect number of command-line arguments are provided, your program should print an error and exit.

2. For each student in the CSV file, insert the student into the students table in the students.db database.

### In roster.py, write a program that prints a list of students for a given house in alphabetical order.

1. Program should accept the name of a house as a command-line argument.
    * If the incorrect number of command-line arguments are provided, your program should print an error and exit.

2. Program should query the students table in the students.db database for all of the students in the specified house.

3. Program should then print out each student’s full name and birth year.
    * Each student should be printed on their own line.
    * Students should be ordered by last name. For students with the same last name, they should be ordered by first name.

For more detailed specifications, see: 
https://cs50.harvard.edu/x/2020/psets/7/houses/