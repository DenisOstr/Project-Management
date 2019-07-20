import sys

from Project import *
from Task import *

class Application():
	def mainMenu(self):
		print('Project Management')
		print('=== Menu ===')
		print('1. Select Task and Start Work')
		print('2. Create Project')
		print('3. Create Task')
		print('4. Show all Tasks')
		print('5. Change Task')
		print('6. Delete Task')
		print('7. Settings')
		print('8. Exit')

		userSelect = input('> ')

		if (userSelect == '1'):
			self.startWork()
		elif (userSelect == '2'):
			cp = Project()
			cp.createProject()
		elif (userSelect == '3'):
			pass
			# ct = Task()
			# ct.createTask()
		elif (userSelect == '4'):
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
		self.mainMenu()