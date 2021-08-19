#!/usr/bin/python3
import mysql.connector
import csv

#database
#tables
#values?

def add_to_key(dictionary, key, vals):
	if key not in dictionary:
		dictionary[key] = vals
	dictionary[key].extend(vals)
	return dictionary

def get_vals_from_val_list(num,r_l,vals):
	tmp = []
	for i in range(r_l):
		tmp.append(vals[i][num])
	return tmp	

def form_dict(rows, columns):
	dict = {}
	print(columns, rows)
	col_len=len(columns)
	row_len=len(rows)
	for i in range(0,col_len):
		bruh = get_vals_from_val_list(i, row_len, rows)
		print(bruh)
		#add_to_key(dict, columns[i], bruh)
	print(dict)

def parse_csv():
	with open('example.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		rows = []
		for row in csv_reader:
			if(line_count==0):
				columns = row
				line_count+=1
				length = len(columns)	
			else:
				rows.append(row)
		form_dict(rows,columns)

	#print("cols"+str(cols))
	#print(columns[cols])
	#	for cols in range(0, len(columns)):
	#		for row in csv_reader:
	#			print("hello")
	#			print(row)
	#print("\titem"+str(item))


	#	print("Number of columns " + str(len(columns)))
	#	print("Number of lines " + str(line_count))


#if line_count == 0:
#	print(row[line_count])
#else:
#	print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#	line_count+=1

#add_row = ("INSERT INTO testing"
#			"(first, second, third,"
#
#	)

def add_data():
	print("add the data mate")

#login into mysql
def orchestrator():
	cnx = mysql.connector.connect(
		user='root',
		host='127.0.0.1',
		database='testing',
		auth_plugin='mysql_native_password')
	cursor = cnx.cursor()
	add_data(cnx,cursor)
	cnx.close()

if __name__ == '__main__':
	parse_csv()
