from ProjectManager.core import *

class Project():
	def showAllProjects(self):
		table = 'projects'

		showProjects = DataBaseInteraction()
		showProjects.selectFrom(table)


	def createProject(self):
		pname = input('Enter project name: ')
		desc = input('Enter project description: ')
		mangPerf = input('Enter id`s project manager: ')

		table = 'projects'

		createProject = DataBaseInteraction()
		createProject.insertTo(table, pname, desc, mang)


	def changeProject(self):
		pass


	def deleteProject(self):
		pass