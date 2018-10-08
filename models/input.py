import sys
from models.enums.methodstype import MethodsType
from models.methods.euler import Euler
from models.methods.rungekutta import RungeKutta
from models.methods.adambashforth import AdamBashForth
from models.methods.adammulton import AdamMulton
from models.methods.inversedformula import InversedFormula

class Input:

	def __init__(self, file):
		self.file = file
		self.methods = []

	def parseAndAssembleMethods(self):
		f = open(self.file, "r")

		for line in f:
			splittedLine = self._splitStringsFromLine(line)
			methodType = self._parseMethodFromSplittedLine(splittedLine)

			isMultipleSteps = methodType.isDefinedByOrder()

			y = self._parseYFromSplittedLine(isMultipleSteps, splittedLine)
			t = self._parseTFromSplittedLine(isMultipleSteps, splittedLine)
			stepsSize = self._parseStepsSizeFromSplittedLine(isMultipleSteps, splittedLine)
			steps = self._parseStepsFromSplittedLine(isMultipleSteps, splittedLine)
			function = self._parseFunctionFromSplittedLine(isMultipleSteps, splittedLine)
			order = self._parseMethodOrderFromSplittedLine(isMultipleSteps, splittedLine)

			if methodType.isEuler():
				self.methods.append(Euler(methodType, y, t, stepsSize, steps, function))
			elif methodType.isRungeKutta():
				self.methods.append(RungeKutta(methodType, y, t, stepsSize, steps, function))
			elif methodType.isAdamBashForth():
				self.methods.append(AdamBashForth(methodType, y, t, stepsSize, steps, function, order))
			elif methodType.isAdamMulton():
				self.methods.append(AdamMulton(methodType, y, t, stepsSize, steps, function, order))
			elif methodType.isInversedFormula():
				self.methods.append(InversedFormula(methodType, y, t, stepsSize, steps, function, order))

	@classmethod
	def _splitStringsFromLine(self, line):
		return line.split()

	@classmethod
	def _parseMethodFromSplittedLine(self, splittedLine):
		return MethodsType.fromString(splittedLine[0])

	@classmethod
	def _parseYFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return list(map(float, splittedLine[1:-5]))

		return list(map(float, splittedLine[1:-4]))
	
	@classmethod
	def _parseTFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return [float(splittedLine[-5])]

		return [float(splittedLine[-4])]

	@classmethod
	def _parseStepsSizeFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return float(splittedLine[-4])

		return float(splittedLine[-3])

	@classmethod
	def _parseStepsFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return int(splittedLine[-3])

		return int(splittedLine[-2])

	@classmethod
	def _parseFunctionFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return splittedLine[-2]

		return splittedLine[-1]

	@classmethod
	def _parseMethodOrderFromSplittedLine(self, isMethodMultipleSteps, splittedLine):
		if isMethodMultipleSteps:
			return int(splittedLine[-1])

		return None