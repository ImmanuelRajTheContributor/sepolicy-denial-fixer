# Denials Input : denials.txt | Fix Output : fixdenials.txt
import re
denres = ""
denlist = []
with open("denials.txt") as deninput:
    denlines = deninput.readlines()
    
regex = {}
regex[0] = re.compile(r"scontext=u:r:(.*?):", re.IGNORECASE)
regex[1] = re.compile(r"tcontext=.*:(.*?):", re.IGNORECASE)
regex[2] = re.compile(r"tclass=(.*?) ", re.IGNORECASE)
regex[3] = re.compile(r"{ .*? }", re.IGNORECASE)

for text in denlines:
    if "scontext" not in text :
        continue
    denialfix = "allow "
    denialfix += f"{re.findall(regex[0], text)[0]} "
    denialfix += f"{re.findall(regex[1], text)[0]}:"
    denialfix += f"{re.findall(regex[2], text)[0]} "
    denialfix += f"{re.findall(regex[3], text)[0]};"
    if denialfix in denlist:
        continue
    denres += f"{denialfix}\n"
    denlist.append(denialfix)

fixfile = open("fixdenials.txt", "w")
fixfile.write(denres)
fixfile.close()
