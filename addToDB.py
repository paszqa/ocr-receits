#OCR-Receits
#Third file to execute

### IMPORTS
import mysql.connector
import re
from difflib import SequenceMatcher

### AUTO SETUP
db = mysql.connector.connect(
        host="localhost",
        user="loser",
        password="dupa",
        database="ocr-receits"
        )
mycursor = db.cursor()
mycursor.execute("SHOW TABLES FROM `ocr-receits`;")
#mycursor.execute("INSERT INTO `ocr-receits`.`KajzerkaPszenna` (`price`, `date`, `store`) VALUES ('0.25', '2021-06-20', 'Lidl');")
#mycursor.execute("SELECT * FROM KajzerkaPszenna")
allTables = mycursor.fetchall()
contentfile = open('content.txt','r').readlines()


#s = SequenceMatcher(None, "BakomaJogurtBioldógt", "BomaJgurtBo10g")
#print(s.ratio())

'''
for singleTable in allTables:
    highestRatio = 0
    lineNumber = -1
    highestLineNumber = -1
    for line in contentfile:
        lineNumber += 1
        s = SequenceMatcher(None, singleTable[0], line.split()[0])
        if s.ratio() > 0.3 :
                if s.ratio() > highestRatio:
                        highestRatio = s.ratio()
                        highestLineNumber = lineNumber
        print("LineNo: "+str(lineNumber)+" Name: "+line.split()[0]+" highestRatio: "+str(highestRatio)+" (on line "+str(highestLineNumber)+")")
    print(singleTable[0]+" [VERSUS] "+contentfile[highestLineNumber].split()[0]+" [RATIO] "+str(s.ratio()))
'''


for line in contentFile:
        highestRatio = 0
        tableNumber = -1
        highestTableName = "-"
        print("Checking now: "+line.split()[0])
        for singleTable in allTables:
                s = SequenceMatcher(None, singleTable[0], line.split()[0])
                print(".......against: "+singleTable[0]+" score: "+str(s.ratio()))