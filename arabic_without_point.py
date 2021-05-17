import os
import pyperclip as pc
import json

# change directory to project file location.
os.chdir(os.path.dirname(__file__))

# read transform letter Dictionary.
myfile = open("transform_dict.json", "r", encoding="utf-8")
mydic = json.load(myfile)[0]
myfile.close()

# read text content that you wish to transform.
myfile = open("input.txt", "r", encoding="utf-8")
lines = myfile.readlines()
myfile.close()

# open output file to write the transform text.
myfile = open("output.txt", "w", encoding="utf-8")
# loop for all lines that read form input file.
for i in lines:
    # loop for all letter in lines.
    for j in range(len(i)):
        # check that letter is a key in dictionary.
        if i[j] in mydic.keys():
            # True condition: replace letter by the value in dict and write letter in output file..
            myfile.write(mydic[i[j]])
        else:
            # False condition: don't replace and write letter in output file.
            myfile.write(i[j])

myfile.close()

# read output file again to take copy of content after transform.
myfile = open("output.txt", "r", encoding="utf-8")
lines = "\n".join(myfile.readlines())
# take copy
pc.copy(lines)
