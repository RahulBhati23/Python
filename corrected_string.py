#You need to replace a section of a string with new content
string="Here are a string"
'''
corrected_string=string[:5] + "is" + string[8:]
print(corrected_string)
'''
corrected_string=string.replace("are","is",1)
print(corrected_string)
