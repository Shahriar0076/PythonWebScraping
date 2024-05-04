# import re

# def extract_phone_numbers(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding
#         data = file.read()

#     # Regular expression pattern to match phone numbers
#     phone_pattern = r'\+?\d+\s?-\s?\d+\s?\d+'

#     # Find all phone numbers in the text using regular expression
#     phone_numbers = re.findall(phone_pattern, data)

#     return phone_numbers

# def save_phone_numbers(phone_numbers, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:  # Specify the encoding
#         for number in phone_numbers:
#             file.write(number + '\n')

# # Example usage
# input_file = 'text.txt'  # Replace 'hotels.txt' with the path to your input text file
# output_file = 'phone_numbers.txt'  # Replace 'phone_numbers.txt' with the desired output file path
# phone_numbers = extract_phone_numbers(input_file)
# save_phone_numbers(phone_numbers, output_file)
# print("Phone numbers saved to:", output_file)


import re

def extract_numbers_from_text_file(file_path):
    numbers = []
    with  open(file_path, 'r', encoding='utf-8') as file:
        for line in file:            
            matches = re.findall(r'\+?\d{2}\s?\d{3,5}-?\d{5,7}', line)
            for match in matches:
                numbers.append(match)
    return numbers

file_path = 'text.txt'  # Provide the path to your text file
numbers = extract_numbers_from_text_file(file_path)
print("Numbers found in the text file:")
print(numbers)