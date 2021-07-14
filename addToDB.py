#OCR-Receits v0.2
#Third file to execute

### IMPORTS
import mysql.connector
import re
from difflib import SequenceMatcher
import sys

### AUTO SETUP
db = mysql.connector.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database="ocr-receits"
        )
mycursor = db.cursor()
contentFile = open('content.txt','r').readlines()
infoFile = open('info.txt','r').readlines()
receitDate = infoFile[0]
storeName = infoFile[1]



for line in contentFile:
        mycursor.execute("SHOW TABLES FROM `ocr-receits`;")
        allTables = mycursor.fetchall()
        highestRatio = 0
        tableNumber = -1
        highestTableName = "-"
        print("Checking now: "+line.split()[0])
        for singleTable in allTables:
                s = SequenceMatcher(None, singleTable[0], line.split()[0])
                #Check if ratio is higher than previous one
                if s.ratio() > highestRatio:
                        #if yes, then set highest ratio AND highest ratio table name
                        highestRatio = s.ratio()
                        highestTableName = singleTable[0]
                #print(".......against: "+singleTable[0]+" score: "+str(s.ratio())+ " /// current highest: "+str(highestRatio)+ " ("+highestTableName+")")
        name=line.split()[0]
        price=line.split()[1].replace(",",".")
        if highestRatio > 0.75:
                print("...............WINNER: "+highestTableName+ ", so lets add to DB this name: "+name+" with price: "+line.split()[1])
                print("...............EXECUTING: "+"INSERT INTO `ocr-receits`.`"+highestTableName+"` (`name`, `price`, `date`, `store`) VALUES ('"+line.split()[0]+"', '"+price+"', '"+receitDate+"', '"+storeName+"');")
                mycursor.execute("INSERT INTO `ocr-receits`.`"+highestTableName+"` (`name`, `price`, `date`, `store`) VALUES ('"+name+"', '"+price+"', '"+receitDate+"', '"+storeName+"');")
                db.commit()
        else:
                print("...............NO WINNER. Lets create new table.")
                mycursor.execute("CREATE TABLE `ocr-receits`.`"+name+"` (`id` INT(11) NOT NULL AUTO_INCREMENT,`name` VARCHAR(30) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',`price` FLOAT NULL DEFAULT NULL,`date` DATE NULL DEFAULT NULL,`store` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci', PRIMARY KEY (`id`) USING BTREE) COLLATE 'utf8mb4_general_ci' ENGINE=InnoDB ROW_FORMAT=Dynamic AUTO_INCREMENT=5;")
                mycursor.execute("INSERT INTO `ocr-receits`.`"+name+"` (`name`, `price`, `date`, `store`) VALUES ('"+name+"', '"+price+"', '"+receitDate+"', '"+storeName+"');")
