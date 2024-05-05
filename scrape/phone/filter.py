import re

def extract_numbers_from_text_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find numbers in each line
            matches = re.findall(r'\b01\d{9}\b', line)
            for match in matches:
                numbers.append(match)
    return numbers

def export_numbers_to_text_file(numbers, output_file_path):
    with open(output_file_path, 'w') as file:
        for number in numbers:
            file.write(number + '\n')

file_path = 'filtered.txt'  # Provide the path to your text file
output_file_path = 'extracted_numbers.txt'  # Provide the path for the new text file
numbers = extract_numbers_from_text_file(file_path)
export_numbers_to_text_file(numbers, output_file_path)
print("Numbers exported to 'extracted_numbers.txt'")
