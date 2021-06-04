import requests
import re

raw = open('raw.txt','r').readlines()
#rawlist = raw.readlines()
start="PARAGON FISKALNY"
foundstart=0
end="Podsuma:"
foundend=0
content=""
for line in raw:
  if "PARA" in line:
    start=line
    foundstart=1
  elif "Podsuma" in line:
    end=line
    foundend=1
  elif foundstart == 1 and foundend == 0:
    content+=line


print(start)
print(end)
print("-------")
print(content)

#result = re.search('PARAGON(.*)123jasd', s)
#print(result.group(1))
