# Simple helper code to ingest txt and output csv
# Run with working directory set to main folder
# Text format: "chest pain", "t waves", "etc:

import csv

# Open file, get rid of quotation marks and split by comma
text_file = open("clinical_keywords.txt", "r")
content = text_file.read()
content = content.replace('"', '')
content_list = content.split(',')
text_file.close()

print("example features: ", content_list[0], content_list[1])
print("total number of features: ", len(content_list))

# Write list to CSV
file = open('scraped_clinical_keywords.csv', 'w', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerow(content_list) 
