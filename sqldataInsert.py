###	Note :	https://www.tutorialspoint.com/python3/python_database_access.htm			for Mysql server and python connection

import pymysql
from flask import jsonify


class sqldatafetch:

	def mydata(self,name,lastname,age):

		print (name+' ' +lastname+' '+age)
		age_in_int=int(age)
		# Open database connection
		db = pymysql.connect("localhost","root","root","abc123" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		
		# Prepare SQL query to INSERT a record into the database.
		sql = "INSERT INTO student(name, \
		   lastname, age) \
		   VALUES ('%s', '%s', '%d' )" % \
		   (name, lastname, age_in_int)
		#	sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'Mohan', 20, 'M', 2000)

		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()
		
		
		# disconnect from server
		db.close()
		
		
		return jsonify(first_name=name, last_name=lastname,age=age_in_int)
	