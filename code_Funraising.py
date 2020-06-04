
import csv

customers = {}     

with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as csv_file: 
	data = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for contact_info in data:
		#Skips header row
		if line_count == 0:
			line_count += 1
		else:
			#no contact condition - people who don't want to be contacted
			if contact_info[13] == 1:
				line_count += 1
			else:
				#This prints contact_info rows
				first_name = contact_info[0] 
				last_name = contact_info[1]
				#TODO: clean up and save .lowercase .capetalize
				phone_num = contact_info [8] 
				phone_no = phone_num.replace('-', '')
				email = contact_info[11] 
				#TODO: might have to import regex - model
				address = contact_info[3] #TODO: do last
				# print(first_name, last_name, phone_num, email, address)
#Dictionary - these people are OK with being contacted
				customers[email] = {
					"First Name": first_name,
					"Last Name": last_name,
					"Phone Number": phone_no,
					"Email": email,
					"Address": address
				}
print(customers)
# TODO create new csv with only those 6 columns 
# ----------- Clean up data --------
# regex look at password string lab , string module,  


 