# filename: teams.py

# Modules
import csv

# variables
students = {}
# find leads
with open('from-SFDC_all-leads.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if it's the first row (header), skip
        if line_count == 0:
            line_count += 1
        else:
            # print(row)
            first_name = row[0]
            last_name = row[1]
            email = row[2]

            if email in students:
                continue
            else:
                students[email] = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Enrolled": False
                }
            line_count += 1

with open('from-SFDC_all-acounts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if it's the first row (header), skip
        if line_count == 0:
            line_count += 1
        else:
            # print(row)
            first_name = row[0]
            last_name = row[1]
            email = row[2]
            type = row[3]


            students[email] = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Enrolled": True
            }
            
            line_count += 1
print("\nStudents:")
print(students)

with open('duplicates.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    for student in students:
        print(students[student])

        first_name = students[student]["First Name"]
        last_name = students[student]["Last Name"]
        email = students[student]["Email"]
        enrolled = students[student]["Enrolled"]

        csv_writer.writerow([first_name, last_name, email, type, enrolled])
