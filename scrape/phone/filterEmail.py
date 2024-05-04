import re

def extract_numbers_from_text_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find numbers in each line
            matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
            for match in matches:
                numbers.append(match)
    return numbers

file_path = 'webText.txt'  # Provide the path to your text file
numbers = extract_numbers_from_text_file(file_path)
print("Numbers found in the text file:")
print(numbers)
