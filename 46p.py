file_path = input("Enter filename: ")
with open(file_path, 'r') as file:
 text = file.read()
 words = text.split()
 print("Total words:", len(words))
