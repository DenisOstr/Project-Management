from ProjectManager.core import *

class Project():
	def __init__(self):
		self.table = 'projects'


	def showAllProjects(self):
		showProjects = DataBaseInteraction()
		showProjects.selectFrom(self.table)

		userSelect = input('\n> ')


	def createProject(self):
		pname = input('Enter project name: ')
		desc = input('Enter project description: ')
		mangPerf = input('Enter id`s project manager: ')

		createProject = DataBaseInteraction()
		createProject.projectInsert(self.table, pname, desc, mangPerf)


	def changeProject(self):
		pass


	def deleteProject(self):
		pass