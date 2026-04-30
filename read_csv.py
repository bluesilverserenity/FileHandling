import csv
import io

# Create a CSV sample in memory
csv_data = """Name,Age,Gender
John,30,Male
Jane,25,Female
Doe,22,Female
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(" | ".join(row)) # Print each row of the CSV file, joining the columns with a separator for better readability
