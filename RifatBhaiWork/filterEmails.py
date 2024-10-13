import re

def filter_emails(input_file, output_file):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            emails = re.findall(email_regex, line)  # Find all email addresses in the line
            for email in emails:
                outfile.write(email + '\n')  # Write each email address to the output file

input_file = 'input_emails.txt'
output_file = 'output_emails.txt'

filter_emails(input_file, output_file)
print("Emails filtered successfully.")
