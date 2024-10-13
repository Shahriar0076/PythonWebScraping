# Read numbers from the text file
with open('output_phones.txt', 'r') as file:
    numbers = [line.strip() for line in file]

# Filter the numbers with 11 digits and start with '01'
filtered_numbers = [number for number in numbers if len(number) == 11 and number.startswith('01')]

# Write the filtered numbers to a new text file
with open('filtered_numbers.txt', 'w') as output_file:
    for number in filtered_numbers:
        output_file.write(number + '\n')

print("Filtered numbers have been written to 'filtered_numbers.txt'.")
