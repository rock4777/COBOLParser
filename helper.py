import pandas as pd
import os

def findWordRow(fileNm, word):
    with open(fileNm) as fp:
        lines = fp.readlines()
        for row in lines:
            if row.find(word) != -1:
                return int(lines.index(row))
        
def filetoList(fileNm, lRow, fRow):
    with open(fileNm) as fp:
        lines = fp.readlines()
        list = []
        for x in range(lRow, fRow):
            list.append(lines[x])
        return list
    
def extTblAtt(attList):
    df = pd.DataFrame(columns=['tblNm', 'colNm', 'colDType', 'isNull'])

    for row in attList:
        if attList.index(row) == 0:
            continue
        elif attList.index(row) == 1:
            rowSplit = attList[attList.index(row)].split()
            colNm = rowSplit[1]
            if 'DECIMAL' in rowSplit[2]:
                colDType = rowSplit[2] + rowSplit[3]
            else: colDType = rowSplit[2]
            if len(rowSplit) > 2 and 'DECIMAL' in rowSplit[2] and rowSplit[3] == 'NOT':
                isNull = 'NOT NULL'
            elif len(rowSplit) > 2 and rowSplit[4] == 'NOT':
                isNull = 'NOT NULL'
            else: isNull = 'NULL'
        elif attList.index(row) > 1:
            rowSplit = attList[attList.index(row)].split()
            colNm = rowSplit[0]
            if 'DECIMAL' in rowSplit[1]:
                colDType = rowSplit[1] + rowSplit[2]
            else: colDType = rowSplit[1]
            if len(rowSplit) > 2 and rowSplit[3] == 'NOT' and 'DECIMAL' in rowSplit[1]:
                isNull = 'NOT NULL'
            elif len(rowSplit) > 2 and rowSplit[2] == 'NOT':
                isNull = 'NOT NULL'
            else: isNull = 'NULL'
    
        df=df.append({'colNm': colNm, 'colDType': colDType, 'isNull': isNull}, ignore_index=True)
    return df

def getTblNm(attList):
    tableNm = attList[0]
    tableNm = tableNm.replace('EXEC SQL DECLARE','')
    tableNm = tableNm.replace('TABLE','')
    tableNm = tableNm.strip()
    return tableNm

def getFLst(dir):
    fileList = os.listdir(dir)
    return fileList