# Modules
import os
import openpyxl

#* This function displays a numbered list to the user, requests a number back, throws an error if the number is bad, and returns the selection's file location
#! type must be a text string - used to make the dialog more clear
#! results - is the thing you're counting from your list
#! source - is the list you're populating options from
def selectFromResults(type, results, source):
    print('Select a ' + type + ' from the list below:')
    for i, results in enumerate(source, 1):
        print(i, ') ' + results)
    # Now request input from the user #TODO: Add an autoselect function if only 1 result (and notify auto-select occurred)
    inputValid = False
    while not inputValid:
        inputRaw = input()
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(source):
            selected = source[inputNo]
            print('Selected ' + type + ': ' + selected)
            inputValid = True
            break
        else:
            print('Please enter a valid file number')
    return selected

# * This section gets all the files from the current working directory that match our desired filetypes (spreadsheets)
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

#* Call the function to establish which Excel file you want to run evaulation on
targetFile = selectFromResults('file', file, matches)

# * This section will will display the contents of the selected workbook and ask for instructions on which sheet to process
wb = openpyxl.load_workbook(targetFile)
sheets = wb.get_sheet_names()
targetSheet = selectFromResults('sheet', sheets, sheets)
sheet = wb.get_sheet_by_name(targetSheet)
print(sheet['A1'].value)