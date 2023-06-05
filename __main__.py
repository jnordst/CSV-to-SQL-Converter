import csv
import re

# Define Table Structure
table_name = "steam_games"
columns = ["game_id", "game_name", "release_date", "peak", "price", "positive_reviews", "negative_reviews", "average_playtime"]

# Read CSV File
csv_file_path = "games.csv"
csv_data = []
with open(csv_file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    csv_data = list(reader)

# Process the data and generate SQL INSERT statements
sql_statements = []
for row in csv_data:
    data_row = []

    for value in row:
        # Remove leading/trailing spaces
        value = value.strip() 
        
        # Check for data types
        if value.isdigit():  # Integer
            data_row.append(value)
        
        elif re.match(r'^-?\d+(\.\d+)?$', value):  # Double
            data_row.append(value)
        
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', value):  # Date in YYYY-MM-DD format
            data_row.append(f"'{value}'")

        else:  # Varchar
            value = value.replace("'", r"\'")  # Replace apostrophes with backslash
            data_row.append(f"'{value}'")

    # Generate SQL INSERT statement
    values = ",".join(data_row)
    sql = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({values});"

    # Add the SQL statement to the list
    sql_statements.append(sql)

# Write SQL statements to a file
sql_file_path = "sql.sql"
with open(sql_file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(sql_statements))

print("Done!")