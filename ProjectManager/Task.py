from ProjectManager.core import *

class Task():
	def showAllTask(self):
		table = 'tasks'

		showTask = DataBaseInteraction()
		showTask.selectFrom(table)


	def createTask(self):
		pass


	def changeTask(self):
		pass


	def deleteTask(self):
		pass