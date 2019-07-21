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
		usSoft = input('Enter software what you use for this task: ')
		statusId = input('Enter status id: ')

		createTask = DataBaseInteraction()
		createTask.taskInsert(self.table, pcode, tname, desc, mangPerf, estClosed, usSoft, statusId)


	def changeTask(self):
		pass


	def deleteTask(self):
		pass