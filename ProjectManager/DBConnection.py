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

		self.today = date.today()


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

		if table == 'projects':
			for d in data:
				print('Project Code' + '     ' + 'Project Name' + '     ' + 'Description'\
					+ '     ' + 'Project Manager' + '     ' + 'Start Date' + '     ' + 'Count Task')
				print('-----------------------------------------------------------------------------------------------\n')
				print(d[0], '\t\t', d[1], '\t\t ', d[2], '\t\t  ',
				 	d[3], '\t\t     ', d[4], '    ', d[5])
		if table == 'tasks':
			for d in data:
				print('Project Code' + '     ' + 'Task Code' + '     ' + 'Task Name' + '     ' + 'Description'\
					+ '     ' + 'Project Performer' + '     ' + 'Start Date' + '     ' + 'Time Spent'\
					+ '     ' + 'Estimated Closed' + '     ' + 'Used Software' + '     ' + 'Status')
				print('-----------------------------------------------------------------------------------------------\n')
				print(d[0], '\t\t', d[1], '\t\t ', d[2], '\t\t  ',
				 	d[3], '\t\t     ', d[4], '    ', d[5],
				 	d[6], '\t\t     ', d[7], '    ', d[8], '\t\t     ', d[9])


	def projectInsert(self, table, pname, desc, mangPerf):
		self.query = 'INSERT INTO {0}("ProjectCode", "Project Name", "Description", "ManagerId", "Start Date", "Count Task")\
		 VALUES(1, \'{1}\', \'{2}\', \'{3}\', \'{4}\', (SELECT COUNT(\'tasks.TaskCode\') FROM tasks))'.format(table, pname, desc, mangPerf, self.today)

		self.dbConnect(self.query)


	def taskInsert(self, table, pcode, tname, desc, mangPerf, estClosed, usSoft, statusId):
		self.query = 'INSERT INTO {0} VALUES(\'{1}\', 1, \'{2}\', \'{3}\', \'{4}\',\
		 \'{5}\', \'100\', \'{6}\', \'{7}\', \'{8}\')'.format(table, pcode, tname, desc,
		  mangPerf, self.today, estClosed, usSoft, statusId)

		self.dbConnect(self.query)

	def changeTo(self):
		pass


	def deleteFrom(self):
		pass