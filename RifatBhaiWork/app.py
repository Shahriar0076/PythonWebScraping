print(250)
def remove_duplicates(input_file, output_file):
    lines_seen = set()  # Maintain a set to keep track of unique lines
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip() not in lines_seen:  # Check if line is not in the set
                outfile.write(line)  # Write the line to output file
                lines_seen.add(line.strip())  # Add line to set

input_file = 'input.txt'
output_file = 'output.txt'

remove_duplicates(input_file, output_file)
print("Duplicates removed successfully.")
