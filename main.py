import helper as hlp
import config
import pandas as pd

fileList = hlp.getFLst(config.dir)
df2 = pd.DataFrame(columns=['tblNm', 'colNm', 'colDType', 'isNull'])

for file in fileList:
    path = config.dir + '\\' + file
    fRowRet = hlp.findWordRow(path,config.fWord)
    lRowRet = hlp.findWordRow(path,config.lWord)
    attList = hlp.filetoList(path, fRowRet, lRowRet)
    df1 = hlp.extTblAtt(attList)
    df1['tblNm'] = hlp.getTblNm(attList)
    df1['colDType'] = df1['colDType'].str.replace('\,$','',regex=True)
    df2 = pd.concat([df1, df2], ignore_index=True)
df2.to_excel("output.xlsx")