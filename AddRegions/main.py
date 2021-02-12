# from xlrd import open_workbook
# book = open_workbook('Inputdata\\Data_Europe_openENTRANCE_GradualDevelopment_oE_v05_kh_30_12_2020.xlsx')
import pandas as pd
import numpy as np

try:
    open('Output.txt', 'w').close()
except:
    pass

new_regions = ["NO" + str(i) for i in range(1, 6)]
n = len(new_regions)
datafile = 'Data_Europe_openENTRANCE_GradualDevelopment_oE_v05_kh_30_12_2020.xlsx'
skip_rows = 4

datafile = 'Hourly_Data_Europe_v05_kh_29_12_2020.xlsx'
skip_rows = 0

print("Reading data")
try:
    Sets_sheet = pd.read_excel('Inputdata\\' + datafile, sheet_name='Sets')
except:
    pass

cut_sheets = pd.read_excel('Inputdata\\' + datafile, sheet_name=None, skiprows=range(0, skip_rows))
# sheet_description = pd.read_excel('Inputdata\\' + datafile, sheet_name=None, header=None, nrows=skip_rows)

print("Adding regions")
def fprint(*args, **kwargs):
    print(*args, **kwargs)
    with open('Output.txt', 'a') as file:
        print(*args, **kwargs, file=file)


def isNaN(val):
    return val != val


def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


def getIndexes(df, value):
    listOfPos = []

    # isin() method will return a dataframe with
    # boolean values, True at the positionsag
    # where element exists
    result = df.isin([value])

    # any() method will return
    # a boolean series
    seriesObj = result.any()

    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)

    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)

        for row in rows:
            # idx=df.columns.get_loc(col)
            listOfPos.append((row, col))

    return listOfPos


def printPositions(listOfPositions):
    if listOfPositions != []:
        fprint(name, ":", sep="")
        for location in listOfPositions:
            fprint(location)
            """row=location[0]+2+3
            letter=colnum_string(location[1]+1)
            pretty_loc=(row,letter)
            fprint(pretty_loc)"""


def addRows(df, listOfPositions):
    delete = []
    for pos in listOfPositions:
        row_nr = pos[0]
        delete.append(row_nr)
        row = (df.iloc[row_nr, :])
        rep = new_regions.copy()
        rep.insert(0, "NO")
        for i in range(n):
            row = row.replace(rep[i], rep[i + 1])
            df = df.append(row)

    df = df.reset_index(drop=True)
    #df = df.drop(df.index[delete])
    return df


def addCols(df):
    series = df["NO"]
    #del df["NO"]
    for reg in new_regions:
        df[reg] = series

    return df


def addEmptyRows(df, skip_rows):
    empty_df = []
    for row in range(skip_rows):
        empty_df.append([np.nan] * len(df.columns))

    empty_df = pd.DataFrame(empty_df, columns=df.columns)
    df = empty_df.append(df, ignore_index=True)
    return df


def toExcel(dfs, names, filename):
    writer = pd.ExcelWriter('ModifiedInput\\Modified' + filename)
    for df, n in zip(dfs, names):
        df = df.dropna(axis=1, how='all')
        df = df.T.reset_index().T
        for idx, col in enumerate(df):
            val = df.iloc[0, idx]
            if type(val) == str and 'Unnamed' in val:
                df.iloc[0, idx] = ''

        if skip_rows and n != 'Sets':
            df = addEmptyRows(df, skip_rows)

        df.to_excel(writer, sheet_name=n, header=False, index=False)

    writer.save()


dfs = []
names = []
for name, sheet in cut_sheets.items():
    if name == "Sets":
        # continue
        sheet = Sets_sheet
        regions = list(sheet["Region"])
        #regions = [i for i in regions if i != "NO"]
        c = 0
        for idx, reg in enumerate(regions):
            if isNaN(reg):
                regions[idx] = new_regions[c]
                c += 1

            if c == len(new_regions):
                break

        series = pd.Series(regions)
        sheet["Region"] = series

    else:
        listOfPositions = getIndexes(sheet, "NO")
        if listOfPositions != []:
            # printPositions(listOfPositions)
            sheet = addRows(sheet, listOfPositions)

        if "NO" in sheet.columns:
            sheet = addCols(sheet)

    dfs.append(sheet)
    names.append(name)

"""for name, sheet in original_sheets.items():
    if name == "Sets":
        regions = list(sheet["Region"])
        regions = [i for i in regions if i != "NO"]
        c = 0
        for idx, reg in enumerate(regions):
            if isNaN(reg):
                regions[idx] = new_regions[c]
                c += 1

            if c == len(new_regions):
                break

        series = pd.Series(regions)
        sheet["Region"] = series

    if name not in names:
        #sheet = sheet.dropna(thresh=len(sheet) // nanTresh, axis=1)
        dfs.append(sheet)
        names.append(name)"""

print("Writing to Excel")
toExcel(dfs, names, datafile)
