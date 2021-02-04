import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=server;"
    "Database=database;"
    "Trusted_Connection=yes;"
)

def NHA(PN):
    """Returns an NHA of passed in PN"""
    cursor = conn.cursor()
    cursor.execute(
    f"""SELECT DISTINCT([NHA]) FROM [TABLE1]
    WHERE [PART] LIKE '%{PN}%'"""
    )
    data = cursor.fetchall()
    cursor.close()
    NHA_list =[]
    for row in data:
        var = str(row).lstrip("('")[:-10]
        NHA_list.append(var)
    return NHA_list

def isCI(PN):
    """Checks if a passed in argument is a CI"""
    cursor = conn.cursor()
    cursor.execute(
    f"""SELECT [CI] FROM [TABLE2]
    WHERE [PART_NUMBER] = '{PN}'"""
    )
    data = str(cursor.fetchall())
    cursor.close()
    if data == "[('B', )]" or data == "[('O', )]":
        return True
    else:
        return False

CI_list =[]

def CI_finder(PN):
    """Returns a closest CI of passed in PN"""
    data = NHA(PN)
    if data == []:
        return False
    else:
        for i in data:
            if i != PN: # to prevent printing a CI which is equal to the PN
                if isCI(i):
                    CI_list.append(i) # serves to remove duplicates later
                elif i == "01CS" or i == "02CS":
                    pass
                elif i != PN: # to prevent an infinite loop
                    CI_finder(i)
        return list(dict.fromkeys(CI_list))

def program_number(PN):
    """Gives general info"""
    for i in PN:
        cursor = conn.cursor()
        cursor.execute(
        f"""SELECT
        DISTINCT([PART_NUMBER]),
        [DESCRIPTION],
        [PROGRAM],
        [LEVEL]
        FROM [TABLE1]
        INNER JOIN [TABLE2]
        ON [TABLE1].[PART] = [TABLE2].[PART]
        WHERE [PART_NUMBER] = '{i}'"""
        )
        data = cursor.fetchall()
        cursor.close()
        for i in data: # prints every tuple in variable data on a new line
            print(i)

def material_description(PN):
    """Return part info"""
    cursor = conn.cursor()
    cursor.execute(
    f"""SELECT [PART_NUMBER], [DESCRIP], [MANUFACTURER]
    FROM [TABLE2]
    WHERE [PART_NUMBER] = '{PN}'"""
    )
    data = cursor.fetchall()
    cursor.close()
    return data

def close():
    conn.close()