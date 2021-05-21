import os

options = {}

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
            # Print the list of matching files
            print(file)

#print(options)

# Build the selection list
# def selectFromResults(options, name):
#     index = 0
#     indexValidList = []
#     print('Select a ' + name + ': ')
#     for optionName in options:
#         index = index + 1
#         indexValidList.extend([options[optionName]])
#         print(str(index) + ': ')
#     inputValid = False
#     while not inputValid:
#         inputRaw = input(name = ': ')
#         inputNo = int(inputRaw) - 1
#         if inputNo > -1 and inputNo < len(indexValidList):
#             selected = indexValidList[inputNo]
#             print('Selected ' + name + ': ' + selected)
#             inputValid = True
#             break
#         else:
#             print('Please select a valid ' + name +' number')
#     return selected

# option = selectFromResults(options, 'option')