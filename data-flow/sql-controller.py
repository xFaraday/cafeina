#!/usr/bin/python3
from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error
import csv
import sys

def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if(parser.has_section(section)):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        print("Couldnt load configuration file")

    return db

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    print(db_config)
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if(conn.is_connected()):
            print('Connection established.')
        else:
            print('Connection failed.')
    except:
    	print("exception")

def add_to_key(dictionary, key, vals):
    if key not in dictionary:
        dictionary[key] = vals
    else:
        dictionary[key].extend(vals)
    return dictionary

def get_vals_from_val_list(num, r_l, vals):
    tmp = []
    for i in range(r_l):
        tmp.append(vals[i][num])
    return tmp

def form_dict(rows, columns):
    dict = {}
    col_len = len(columns)
    row_len = len(rows)
    for i in range(0, col_len):
        bruh = get_vals_from_val_list(i, row_len, rows)
        add_to_key(dict, columns[i], bruh)
    for key, value in dict.items():
    	print(dict[key])

def insert_rows(table, column, values):
	#example formed query
	#INSERT INTO books(title, author) VALUES(%s, %s)
	FAT_S="%s,"*len(values[0])
	THIN_S=FAT_S[:-1]
	query = "INSERT INTO " + table + "(" + column + ") VALUES(" + THIN_S + ")"
	print(table)
	print(column)
	
	try:
		print(query)
		#print(query)
		#dbconfig = read_db_config()
		#conn = MySQLConnection(**dbconfig)
		#cursor = conn.cursor()

		#cursor.executemany(query, books)

		#conn.commit()

	except Error as error:
		print(error)

def parse_csv():
    with open("example.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if(line_count == 0):
                columns = row
                line_count += 1
                length = len(columns)
                str_columns=','.join([str(item) for item in columns])
            else:
                rows.append(row)
        print(str_columns)
        print(rows)
        table="training"
        insert_rows(table, str_columns, rows)
        #form_dict(rows, columns)

def add_data():
    print("add the data mate")

def iter_row(cursor, size=10):
	while True:
		rows = cursor.fetchmany(size)
		if not rows:
			break
		for row in rows:
			yield row

def query_safe():
	try:
		dbconfig = read_db_config()
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
		
		cursor.execute("SELECT * FROM books")

		for row in iter_row(cursor, 10):
			print(row)

	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()

def init():
    arguments = len(sys.argv)-1
    iterator = arguments+1
    for i in range(1, iterator):
        if(sys.argv[i] == "csvfile"):
            a = i+1
            parse_csv(sys.argv[a])
        elif(sys.argv[i] == "table"):
            j = i+1
            print("hello")

def orchestrator():
    print("bruh")

if __name__ == '__main__':
	parse_csv()
