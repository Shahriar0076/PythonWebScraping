import csv 

#read
with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])

# write
rows = [ [variable1, variable2, variable3, variable4, variable5, variable6] ] 
filename = "scraped_data.csv"    
with open(filename, 'a') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(rows)