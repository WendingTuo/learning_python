# Modules
import os

# Variables
matches = []

# Gets the current working directory
cwd = os.getcwd()
# Define the file types we're looking for
fileTypes = ('.xlsx','.xls','.csv')
# Check current directory, subdirectories, and files
for root, dirs, files in os.walk(cwd):
    # Select the filename from the list of files gathered by os.walk()
    for file in files:
        # Check the extension of the file against our list of extensions
        if file.endswith(fileTypes):
            # Add the matches to our matches list
            matches.append(os.path.join(root, file))

# Now print that as a numbered list
def selectFromResults():
    print("Select a file from the list below: ")
    for i, file in enumerate(matches, 1):
        print(i, ') ' + file)
    # Now request input from the user
    inputValid = False
    while not inputValid:
        inputRaw = input()
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(matches):
            selected = matches[inputNo]
            print('Selected file: ' + selected)
            inputValid = True
            break
        else:
            print('Please enter a valid file number')
    return selected

selectFromResults()