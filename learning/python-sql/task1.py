# file = open("C:\\Users\\srira\\OneDrive\\Desktop\\excel2.csv","r")
# contents=file.read()
# print(contents)

# file = open("C:\\Users\\srira\\OneDrive\\Desktop\\excel2.csv","w")
# file.write("asdf python java selenium")

#import csv
# def read_csv_file():
#     file_path="test.csv"
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)
# read_csv_file()

# def write_csv(new_row):
#     file_path = "test.csv"
    
#     # Open the CSV file in append mode
#     with open(file_path, 'a', newline='') as file:
#         writer = csv.writer(file)
        
#         # Write the new row to the CSV file
#         writer.writerow(new_row)

# # Example usage:
# new_data = ['9', 'ram', '21']

# write_csv(new_data)




# # Removing csv file
# import os

# # Removing (deleting) a CSV file
# file_path = 'test.csv'
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"The file {file_path} has been removed.")
# else:
#     print(f"The file {file_path} does not exist.")







import csv
def readcsv():
    with open("test.csv",'r') as file:
     reader=csv.reader(file)
     for row in reader:
        print(row)
readcsv()


