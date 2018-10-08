import sys
from models.operator import Operator
from models.methods.methods import Methods

class Input:

	def __init__(self, file):
		self.file = file
		self.operators = []

	def assembleOperations(self):
		f = open(self.file, "r")

		for line in f:
			method = self._parseMethodFromLine(line)
			methodOrder = self._parseMethodOrder(method, line)

			print(method, methodOrder)
			

	@classmethod
	def _parseMethodFromLine(self, line):
		return Methods.fromString(line)

	@classmethod
	def _parseMethodOrder(self, method, line):
		if not method.isDefinedByOrder():
			return None
		return int(line[-2:])




	




	


