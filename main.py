import os

def find_folders_with_pdf(folder_path):
    pdf_folders = []
    i=0
    j=0
    # Iterate through all folders and subfolders
    for root, dirs, files in os.walk(folder_path):
        print("Count:",i)
        # Check if any file in the current folder is a PDF
        if any(file.lower().endswith('.pdf') for file in files):
            # Add the current folder to the list
            pdf_folders.append(root)
            print("Append:",j)
            j=j+1
        i=i+1
    
    return pdf_folders

# Provide the path to the main folder
folder_path = "C:/rec2/"

# Call the function to get the list of folders
pdf_folders = find_folders_with_pdf(folder_path)
f = open("folders.txt", "a")
# Print the list of folders
if pdf_folders:
    print("Folders containing PDF files:")
    for folder in pdf_folders:
        print(folder)
        f.write(folder + "\n")
else:
    print("No folders contain PDF files.")
