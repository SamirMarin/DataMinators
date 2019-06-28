import csv, sqlite3
import os
import sys

def load_sql_table(path, tableName):
    basepath = os.path.expanduser('~/') + path
    create_table_str = "CREATE TABLE IF NOT EXISTS {}".format(tableName)
    insert_table_str = "INSERT INTO {}".format(tableName)
    columns = []
    with open(basepath, "r") as f:
        csv.field_size_limit(sys.maxsize)
        reader = csv.reader(f)
        columns = next(reader)

    column_names = " (" + ",".join(columns) + ");"
    column_names_insert = " (" + ",".join(columns) + ")"
    con = sqlite3.connect("yelpdb")
    cur = con.cursor()
    print("this is my create statement")
    print(create_table_str + column_names)
    cur.execute(create_table_str + column_names) # use your column names here

    print("opening")
    with open (basepath, 'r') as fin:
        dr = csv.DictReader(fin)
        print(dr)
        count = 0
#    for i in dr:
#        if count == 0:
#            print(i)
        to_db = [tuple(i.values()) for i in dr]

    values = " VALUES(?"
    count = 0
    for column in columns:
        if count != 0:
            values = values + " ,?"
        count += 1

    values = values + ");"

    print("this is one column of data")

    print(to_db[0])

    print("this is my insert stm")
    print(insert_table_str + column_names_insert + values)
    print("inserting to table")
    cur.executemany(insert_table_str + column_names_insert + values, to_db)
    print("done inserting")
    con.commit()
    con.close()

def wrap_quotes(col):
    return "'" + col + "'"

def append_to_list(the_list, item):
    list_append = list(the_list)
    list_append.append(item)
    return list_append

def load_sql_table_with_delimiter(path, the_file, tableName, delimiter):
    custFolderPath = os.path.expanduser('~/') + path[0:path.rfind('/')] + "/"
    basepath = os.path.expanduser('~/') + path + "/" + the_file
    print("BASEPATH")
    print(basepath)
    create_table_str = "CREATE TABLE IF NOT EXISTS {}".format(tableName)
    insert_table_str = "INSERT INTO {}".format(tableName)
    columns = []
    current_deli = ","
    if delimiter == "pipe":
        current_deli = "|"
    elif delimiter == "tab":
        current_deli = "\t"
    with open(basepath, "r") as f:
        csv.field_size_limit(sys.maxsize)
        reader = csv.reader(f, delimiter=current_deli)
        columns = next(reader)

    columns.append("file_path")
    columns = list(map(wrap_quotes, columns))

    print("Printing Columns")
    print(columns)

    column_names = " (" + ",".join(columns) + ");"
    column_names_insert = " (" + ",".join(columns) + ")"
    print(column_names_insert)
    con = sqlite3.connect(custFolderPath + "SQLLite.db")
    cur = con.cursor()
    print("this is my create statement")
    print(create_table_str + column_names)
    cur.execute(create_table_str + column_names) # use your column names here

    print("opening")


    with open (basepath, 'r') as fin:
        dr = csv.DictReader(fin, delimiter=current_deli)
        print(dr)
        count = 0
#    for i in dr:
#        if count == 0:
#            print(i)
        to_db = [tuple(append_to_list(i.values(), basepath)) for i in dr]

    values = " VALUES(?"
    count = 0
    for column in columns:
        if count != 0:
            values = values + " ,?"
        count += 1

    values = values + ");"

    print("this is one column of data")

    #print(to_db[0])

    print("this is my insert stm")
    print(insert_table_str + column_names_insert + values)
    print("inserting to table")
    cur.executemany(insert_table_str + column_names_insert + values, to_db)
    print("done inserting")
    con.commit()
    con.close()
