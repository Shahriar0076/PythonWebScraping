def remove_emails(base_file, base2_file):
    # Read emails from base.txt
    with open(base_file, 'r') as f:
        emails_to_remove = set(f.read().splitlines())

    # Read emails from base2.txt
    with open(base2_file, 'r') as f:
        emails = f.read().splitlines()

    # Remove emails that are present in base.txt
    emails_without_duplicates = [email for email in emails if email not in emails_to_remove]

    # Write back to base2.txt
    with open(base2_file, 'w') as f:
        f.write('\n'.join(emails_without_duplicates))

# Replace 'base.txt' and 'base2.txt' with the actual filenames
remove_emails('base.txt', 'base2.txt')
