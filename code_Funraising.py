# import numpy as np
# import pandas as pd
import csv


# # THIS VERSION PRINTS THE LIST
# with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as file: 
#     data = file.read()
 

# #variables
customers = {}     

# THIS VERSION DOESN'T PRINT YET

with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as csv_file: 
	data = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for contact_info in data:
		#Skips header
		if line_count == 0:
			line_count += 1
		else:
			#print row
			first_name = contact_info[0] 
				#if statement: skip

			last_name = contact_info[1]
			phone_num = contact_info [8]
			email = contact_info[11]
			print(first_name, last_name, phone_num, email)
			
			# email = row[2]		
			
			# if email in customers:
			# 	continue
			# else:
			# 	customers[email] = {
			# 		"First Name": first_name,
			# 		"Last Name": last_name,
			# 		"Email": email,
				
			# 	}
			# line_count += 1



 