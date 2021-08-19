#!/usr/bin/python3
import mysql.connector
import csv

def add_to_key(dictionary, key, vals):
	if key not in dictionary:
		dictionary[key] = vals
	else:
		dictionary[key].extend(vals)
	return dictionary

def get_vals_from_val_list(num,r_l,vals):
	tmp = []
	for i in range(r_l):
		tmp.append(vals[i][num])
	return tmp	

def form_dict(rows, columns):
	dict = {}
	col_len=len(columns)
	row_len=len(rows)
	for i in range(0,col_len):
		bruh = get_vals_from_val_list(i, row_len, rows)
		add_to_key(dict, columns[i], bruh)
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
