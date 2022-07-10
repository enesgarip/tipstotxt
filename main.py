import re

fin = open("a.txt", "r")
txt = fin.read()
fin.close()
cropped = re.findall("Tip \d+(?:.*\n){1,3}.*", txt)
cropped.pop(2)
cropped = [str(i).replace("\n", ":", 1).replace("\n", "") for i in cropped]
fout = open("Tips.txt", "w")
for j in cropped:
    fout.write(j + "\n\n")
fout.close()
