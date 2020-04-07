import csv

#THIS VERSION PRINTS THE LIST
# with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as file: 
#     data = file.read()
        

#variables
customers = {}     

# THIS VERSION DOESN'T PRINT YET

with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as csv_file: 
    data = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in data:
        #Skips header
        if line_count == 0:
           line count += 1
        else:
                #print row
                first_name = row[0]
                last_name = row [1]
                email = row[2]

                if email in data:
                        continue
                else:
                     students
print(data)


 
        # TODO save as dictionary

 