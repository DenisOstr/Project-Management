import sys
import os

from ProjectManager.core import *

class Application():
	def mainMenu(self):
		print('Project Management\n')
		print('=== Menu ===\n')
		print('1. Select Task and Start Work')
		print('2. Create Project')
		print('3. Create Task')
		print('4. Show all Tasks')
		print('5. Change Task')
		print('6. Delete Task')
		print('7. Settings')
		print('8. Exit')

		userSelect = input('\n> ')

		if (userSelect == '1'):
			os.system('cls')
			self.startWork()
		elif (userSelect == '2'):
			os.system('cls')
			cp = Project()
			cp.createProject()
		elif (userSelect == '3'):
			os.system('cls')
			ct = Task()
			ct.createTask()
		elif (userSelect == '4'):
			os.system('cls')
			st = Task()
			st.showAllTask()
		elif (userSelect == '5'):
			pass
		elif (userSelect == '6'):
			pass
		elif (userSelect == '7'):
			pass
		elif (userSelect == '8'):
			sys.exit()
		else:
			print('Error: Section number %s does not exist' % userSelect)


	def startWork(self):
		sp = Project()
		sp.showAllProjects()


	def start(self):
		os.system('cls')
		self.mainMenu()