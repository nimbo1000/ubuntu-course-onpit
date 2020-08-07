#This is a template for the grader

from onpit import Grader
from os.path import join, exists
import git

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "ls":
			return True




