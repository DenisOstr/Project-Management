from ProjectManager.core import *

class Task():
	def __init__(self):
		self.table = 'tasks'


	def showAllTask(self):
		showTask = DataBaseInteraction()
		showTask.selectFrom(self.table)


	def createTask(self):
		pcode = input('Enter project code: ')
		tname = input('Enter task name: ')
		desc = input('Enter project description: ')
		mangPerf = input('Enter id`s project performer: ')
		estClosed = input('Enter estimated closed date: ')
		usSoft = input('')
		status = input('')

		createTask = DataBaseInteraction()
		createTask.insertTo(self.table)


	def changeTask(self):
		pass


	def deleteTask(self):
		pass