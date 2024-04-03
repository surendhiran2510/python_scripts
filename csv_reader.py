import csv

def parse_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)  # Print each row of the CSV file

# Example usage
csv_file_path = 'example.csv'  # Path to your CSV file
parse_csv(csv_file_path)
