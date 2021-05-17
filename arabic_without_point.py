import os
import pyperclip as pc
import json

# change directory to project file location.
os.chdir(os.path.dirname(__file__))
# letter baq and noun encoding in utf-8
noun = b'\xd9\x86'
baq = b'\xd8\xa8'
# read transform letter Dictionary.
myfile = open("transform_dict.json", "r", encoding="utf-8")
mydic = json.load(myfile)[0]
myfile.close()

# read text content that you wish to transform.
myfile = open("input.txt", "r", encoding="utf-8")
lines = myfile.readlines()
lines[-1] = lines[-1]+" "
myfile.close()

# open output file to write the transform text.
myfile = open("output.txt", "w", encoding="utf-8")
# loop for all lines that read form input file.
for i in lines:
    i = i + " "
    letterList =[]
    # loop for all letter in lines.
    for j in range(len(i)):
        if i[j] == noun.decode("utf-8") and (i[j+1] != " " and i[j+1] != "\n"):
            y = baq.decode("utf-8")
        else:
            y = i[j]
        # check that letter is a key in dictionary.
        if y in mydic.keys():
            # True condition: replace letter by the value in dict and write letter in output file..
            letterList.append(mydic[y])
        else:
            # False condition: don't replace and write letter in output file.
            letterList.append(y)
    myfile.write("".join(letterList).strip(" "))

myfile.close()

# read output file again to take copy of content after transform.
myfile = open("output.txt", "r", encoding="utf-8")
lines = "\n".join(myfile.readlines())
# take copy
pc.copy(lines)
