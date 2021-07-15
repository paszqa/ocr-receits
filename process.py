#OCR-Receits v0.2
#Second file to execute
import requests
import re
from difflib import SequenceMatcher

def check_for_pattern_in_string(pattern,string):
    if pattern in string:
        #return "[[[["+string+"]]]];"
        return 1
    else:
        #return string+";"
        return 0

raw = open('raw.txt','r').readlines()
infoFile = open('info.txt','w')

start="PARAGON FISKALNY"
foundstart=0
end="Podsuma:"
foundend=0
content=""
previousincomplete=0
alreadyfoundname=0

### Get date from receit:
print("Getting date from receit...")
for line in raw:
  shouldBreak=0
  for part in line.split():
    match = re.search(r'\d{4}-\d{2}-\d{2}', part)
    if match:
      infoFile.write(match.group()+"\n")
      #print("MATCH:"+str(match.group()))
      shouldBreak=1
      break;
  if shouldBreak == 1:
    break;

### Get store name:
print("Getting store name from receit...")
for line in raw:
  shouldBreak=0
  for part in line.split():
    s1 = SequenceMatcher(None, part, "Kaufland")
    s2 = SequenceMatcher(None, part, "Lidl")
    s3 = SequenceMatcher(None, part, "Biedronka")
    s4 = SequenceMatcher(None, part, "Carrefour")
    s5 = SequenceMatcher(None, part, "Auchan")
    if s1.ratio() > 0.75 or s2.ratio() > 0.75 or s3.ratio() > 0.75 or s4.ratio() > 0.75 or s5.ratio() > 0.75:
      infoFile.write(line)
      shouldBreak=1
      break;
  if shouldBreak == 1:
    break;

### Get product list (Kaufland):
print("Getting product list from receit...")
for line in raw:
  print("Checking line: "+line)
  if "PARA" in line:
    start=line
    foundstart=1
  elif "Podsum" in line:
    end=line
    foundend=1
  elif foundstart == 1 and foundend == 0:
    parts = line.split()
    if previousincomplete == 0:
      alreadyfoundname=0
    #First check if last element contains comma
    if "," in parts[-1] and len(parts) > 3:
      for x in range(len(parts)):
        if check_for_pattern_in_string("szt.",parts[x]) == 1:
          alreadyfoundname=1
        if alreadyfoundname == 0:
          content+=parts[x].rstrip()
        #content+=parts[x].rstrip()+" "
      content+=" "+parts[-2].replace("x", "")+"\n"
    #Then check if second last contains comma and remove space if it does
    elif len(parts) > 3:
      if "," in parts[-2]:
        for x in range(len(parts) - 2):
          if check_for_pattern_in_string("szt.",parts[x]) == 1:
            alreadyfoundname=1
          if alreadyfoundname == 0:
            content+=parts[x].rstrip()
          #Check if it is the SZT number
          #content+=check_for_pattern_in_string("szt.",parts[x])
          #if "szt." in parts[x]:
          #  content+="[[[["+parts[x].rstrip()+"]]]]"
          #else:
          #  content+=parts[x].rstrip()+" "
        content+=" "+parts[-3].replace("x", "").rstrip()#+parts[-1].rstrip()
        content+="\n"
      else:
        content+=" AAAAAAAAA "
    else:
#      content
      if previousincomplete == 0:
        previousincomplete = 1
        for x in range(len(parts)):
          content+=parts[x].rstrip()
        content+=" "
      else:
        previousincomplete = 0
        if len(parts) > 2:
          content+=parts[-2].replace("x", "")+"\n"
        else:
          content+=" BBBBBBBBBB "


print(start)
print(end)
print("-------")
print(content)
contentfile = open('content.txt','w')
contentfile.write(content)
contentfile.close()
#from difflib import SequenceMatcher
#s = SequenceMatcher(None, "BakomaJogurtBioldógt", "BomaJgurtBo10g")
#print(s.ratio())

#result = re.search('PARAGON(.*)123jasd', s)
#print(result.group(1))
