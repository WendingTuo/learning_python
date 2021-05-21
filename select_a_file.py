# Modules
import os

# Variables
matches = []
matchesDict = {}

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

# Now print that list to check
for i in (matches):
    print(i)

# Build the matches into a dictionary
for i in [matches]:
    matchesDict[file] = (matches)

# # * Build the selection list function and set starting variables
# def selectFromResults(matches, name):
#     index = 0
#     indexValidList = []
#     print('Select a ' + name + ': ')
# # * For each entry in the matches list, append an index value and insert into a dictionary
#     for optionName in matchesDict:
#         index = index + 1
#         indexValidList.extend([matchesDict[optionName]])
#         print(str(index) + ') ' + optionName)
#     inputValid = False
#     while not inputValid:
#         inputRaw = input(name + ': ')
#         inputNo = int(inputRaw) - 1
#         if inputNo > -1 and inputNo < len(indexValidList):
#             selected = indexValidList[inputNo]
#             print('Selected ' + name + ': ' + selected)
#             inputValid = True
#             break
#         else:
#             print('Please select a valid ' + name +' number')
#     return selected

# option = selectFromResults(matches, 'file')