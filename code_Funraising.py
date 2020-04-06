import csv

# import pandas as pd
# from openpyxl.workbook import Workbook

        #using pandas
# df_csv = pd.read_csv('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv')
# print(df_csv)

        #ORIGINAL READ CODE


with open('/Users/ElMiche/Desktop/PDX_Code_Guild/Confidential_CCC_files/customer_listings_CCC.csv', 'r', encoding='ISO-8859-1') as file: 
    data = file.read()
        
print(data)


        # TODO save as dictionary

 