# Read the numbers from numbers1.txt
with open('numbers1.txt', 'r') as file1:
    numbers1 = set(file1.read().splitlines())

# Read the numbers from numbers2.txt
with open('numbers2.txt', 'r') as file2:
    numbers2 = file2.read().splitlines()

# Filter out the numbers from numbers2 that are in numbers1
filtered_numbers = [number for number in numbers2 if number not in numbers1]

# Write the filtered numbers back to numbers2.txt
with open('numbers2.txt', 'w') as file2:
    for number in filtered_numbers:
        file2.write(f"{number}\n")

print("Filtered numbers2.txt successfully!")

# i have 2 text files, numbers1.txt, numbers2.txt 
# containing numbers like this

# 8801988181920
# 8801988438100
# 8801988833002
# 8801988899925
# 8801989208272
# 8801989678638
# 8801989999003

# now numbers2.txt should not have the numbers that are in numbers1.txt
# write a python script to do it