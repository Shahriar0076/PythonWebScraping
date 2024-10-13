import re

def filter_phones(input_file, output_file):
    phone_regex = r'\b(?:\d[ -]?){9,}\b'  # Phone number regex
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            phones = re.findall(phone_regex, line)  # Find all phone addresses in the line
            for phone in phones:
                outfile.write(phone + '\n')  # Write each email address to the output file

input_file = 'input_emails.txt'
output_file = 'output_phones.txt'

filter_phones(input_file, output_file)

print("Phones filtered successfully.")
