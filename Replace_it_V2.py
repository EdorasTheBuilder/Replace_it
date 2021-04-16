import easygui as eg 
#vars 
fieldNames = ['String', 'Find:', 'Replace:']
fieldValues = []  # we start with blanks for the values
fieldValues = eg.multenterbox('Enter values', 'Replace It', fieldNames)
final = fieldValues[0].replace(fieldValues[1], fieldValues[2])
eg.textbox('Final Result', 'Function finished', final)