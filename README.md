# CSV-to-SQL-Converter
A simple Python application that reads a .csv file, formats all the data from each rows, then writes the result to a .sql file

## Disclaimer
I only formatted to cover VARCHAR, INT, DOUBLE, and DATE data types

If your table contains other data types then this will likely not work for. But feel free to adjust it to your needs

## How to Use
1. Replace the games.csv with a your own csv
2. The sql.sql file will be overwritten, so it can stay
3. Open the python file
4. Replace the ``table_name`` field with your table name
5. Replace each column in the ``columns`` field with your tables columns
6. Replace the ``csv_file_path`` field with the filepath to your .csv file
7. Replace the ``sql_file_path`` field with the filepath to your .sql file
8. Run

## Output
![image](https://github.com/jnordst/CSV-to-SQL-Converter/assets/12515630/be6b21a2-0760-47a5-bc40-1afb889f2e5c)
