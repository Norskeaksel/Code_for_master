# from xlrd import open_workbook
# book = open_workbook('Inputdata\\Data_Europe_openENTRANCE_GradualDevelopment_oE_v05_kh_30_12_2020.xlsx')
import pandas as pd
import numpy as np
import numbers

try:
    open('Output.txt', 'w').close()
except:
    pass


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
        rep.insert(0, original_region)
        for i in range(n):
            row = row.replace(rep[i], rep[i + 1])
            df = df.append(row)

    df = df.reset_index(drop=True)
    # df = df.drop(df.index[delete])
    return df


def addCols(df):
    series = df[original_region]
    # del df["NO"]
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


def fixStupidErrors(df, first_lines, n, skiprows):
    """for idx, col in enumerate(df.columns):
        header = df.iloc[0, idx].split('.')
        if len(header) > 1:
            df.iloc[0, idx] = header[0]"""

    first_sheet_lines = first_lines[n]
    someNa = first_sheet_lines.isnull().values.any()
    onlyNa = first_sheet_lines.isnull().sum().sum() == len(first_sheet_lines.columns)
    new_skiprows = skiprows
    if someNa and not onlyNa and n != 'Sets':
        new_skiprows = skiprows - 1
        df = first_sheet_lines.append(df)

    return df, new_skiprows


def toExcel(dfs, names, filename, first_lines, skip_rows):
    writer = pd.ExcelWriter('ModifiedInput\\Modified_' + filename)
    for df, n in zip(dfs, names):
        #df = df.dropna(axis=1, how='all')
        df = df.T.reset_index().T
        for idx, col in enumerate(df):
            val = df.iloc[0, idx]
            if type(val) == str and 'Unnamed' in val:
                df.iloc[0, idx] = ''

        #df, sr = fixStupidErrors(df, first_lines, n, skip_rows)
        if n != 'Sets':
            #df = addEmptyRows(df, sr)
            df = first_lines[n].append(df,ignore_index=True)

        df.to_excel(writer, sheet_name=n, header=False, index=False)

    writer.save()


def deleteNonNO(df, listOfPositions):
    keep_rows = [i[0] for i in listOfPositions]
    # keep_cols = [i[1] for i in listOfPositions]
    # keep_cols += ([i for i in df.columns if isinstance(i, numbers.Number) or'named' in i])
    # keep_cols = set(keep_cols)
    # cut_df = df[keep_cols]
    # if 'NO' in df.columns:
    # cut_df['NO'] = df['NO']

    cut_df = df.iloc[keep_rows]
    cut_df = cut_df.reset_index(drop=True)
    # if 'Trade' in name:
    # cut_df = pd.DataFrame()

    return cut_df


new_regions = ["Mordor" + str(i) for i in range(1, 6)]
original_region="Mordor"
n = len(new_regions)
datafile = 'Data_MiddleEarth_v01.xlsx'
skip_rows = 4

datafile = 'Hourly_Data_MiddleEarth_v01.xlsx'
skip_rows = 0

print("Reading data")
try:
    Sets_sheet = pd.read_excel('Inputdata\\' + datafile, sheet_name='Sets')
except:
    pass

cut_sheets = pd.read_excel('Inputdata\\' + datafile, sheet_name=None, skiprows=range(0, skip_rows))
first_lines = pd.read_excel('Inputdata\\' + datafile, sheet_name=None, header=None, nrows=skip_rows)
print("Adding regions")
dfs = []
names = []
for name, sheet in cut_sheets.items():
    if name == "Sets":
        # continue
        sheet = Sets_sheet
        regions = list(sheet["Region"])
        # regions = [i for i in regions if i != "NO"]
        c = 0
        for idx, reg in enumerate(regions):
            if isNaN(reg):
                regions[idx] = new_regions[c]
                c += 1

            if c == len(new_regions):
                break

        series = pd.Series(regions)
        sheet["Region"] = series
        # remove following
        dfs.append(sheet)
        names.append(name)

    else:
        listOfPositions = getIndexes(sheet, original_region)
        """sheet = deleteNonNO(sheet, listOfPositions)
        datafile = 'Needed_Norwegian_data_without_trade.xlsx'
        datafile = 'Needed_Norwegian_data_with_trade.xlsx'
        listOfPositions = getIndexes(sheet, "NO")"""
        add = False
        if listOfPositions != []:
            # printPositions(listOfPositions)
            sheet = addRows(sheet, listOfPositions)
            add = True

        if original_region in sheet.columns:
            sheet = addCols(sheet)
            add = True

        dfs.append(sheet)
        names.append(name)

print("Writing to Excel")
toExcel(dfs, names, datafile, first_lines, skip_rows)
