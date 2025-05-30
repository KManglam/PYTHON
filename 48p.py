file_path = input("Enter filename: ")
with open(file_path, 'r') as file:
  lines = file.readlines()

 
 print("File as array:", lines)
