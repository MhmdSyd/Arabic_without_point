import os

os.chdir(os.path.dirname(__file__))

mydic = {
  "أ": "ا",
  "إ": "ا",
  "آ": "ا",
  "ب": "ٮ",
  "ت": "ٮ",
  "ث": "ٮ",
  "ج": "ح",
  "خ": "ح",
  "ذ": "د",
  "ز": "ر",
  "ش": "س",
  "ض": "ص",
  "ظ": "ط",
  "غ": "ع",
  "ف": "ڡ",
  "ق": "ڡ",
  "ئ": "ى",
  "ي": "ى",
  "ؤ": "و",
  "ن": "ٮ",
  "ة": "ه"
}

myfile = open("input.txt", "r",encoding="utf-8")
lines = myfile.readlines()
myfile.close()

for i in lines:
    print(i)
            



myfile = open("output.txt", "w",encoding="utf-8")

for i in lines:
    for j in range(len(i)):
        if i[j] in mydic.keys():
            myfile.write(mydic[i[j]])
        else:
            myfile.write(i[j])

myfile.close()