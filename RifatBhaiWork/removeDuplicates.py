# Read emails from the text file
with open('output_phones.txt', 'r') as file:
    emails = file.readlines()

# Remove duplicates by converting the list to a set, then back to a list
unique_emails = list(set(email.strip() for email in emails))

# Sort the emails alphabetically (optional)
unique_emails.sort()

# Write the unique emails back to a new text file
with open('unique_emails.txt', 'w') as file:
    for email in unique_emails:
        file.write(email + '\n')

print("Duplicates removed. Unique emails saved to 'unique_emails.txt'.")
