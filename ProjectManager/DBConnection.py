#!C:\Users\denis\AppData\Local\Programs\Python\Python36\python

import psycopg2
from datetime import date

class DataBaseInteraction():
	def __init__(self):
		self.user = 'postgres'
		self.password = 'root'
		self.host = 'localhost'
		self.port = '5432'
		self.database = 'ProjectManagement'


	def dbConnect(self, query):
		try:
			connection = psycopg2.connect(user = self.user,
										password = self.password,
										host = self.host,
										port = self.port,
										database = self.database)

			cursor = connection.cursor()

			if (self.query.startswith('SELECT')):
				cursor.execute(self.query)

				data = cursor.fetchall()

				return data
			if(self.query.startswith('INSERT')):
				cursor.execute(self.query)

				connection.commit()

		except (Exception, psycopg2.Error) as error:
			print("Error while connecting to PostgreSQL:", error)
		finally:
			if connection:
				cursor.close()
				connection.close()


	def selectFrom(self, table):
		self.query = 'SELECT * FROM %s' % table

		data = self.dbConnect(self.query)

		for d in data:
			print('Project Code' + '     ' + 'Project Name' + '     ' + 'Description'\
				+ '     ' + 'Project Manager' + '     ' + 'Start Date' + '     ' + 'Count Task')
			print('-----------------------------------------------------------------------------------------------\n')
			print(d[0], '\t\t', d[1], '\t\t ', d[2], '\t\t  ',
			 	d[3], '\t\t     ', d[4], '    ', d[5])


	def insertTo(self, table, pname, desc, mang):
		today = date.today()

		self.query = 'INSERT INTO {0}("ProjectCode", "Project Name", "Description", "ManagerId", "Start Date", "Count Task")\
		 VALUES(1, \'{1}\', \'{2}\', \'{3}\', \'{4}\', (SELECT COUNT(\'tasks.TaskCode\') FROM tasks))'.format(table, pname, desc, mang, today)

		self.dbConnect(self.query)


	def changeTo(self):
		pass


	def deleteFrom(self):
		pass