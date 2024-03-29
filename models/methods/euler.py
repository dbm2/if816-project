import sys
from enums.methodstype import MethodsType
from models.method import Method

class Euler(Method):

	def calculate(self):
		for i in range(1, self.steps + 1):
			v = (0, 0)
			if self.type == MethodsType.EULER:
				v = self.calculateByEuler(self.y[i-1], self.t[i-1])
			elif self.type == MethodsType.EULER_INVERSE:
				v = self.calculateByInverseEuler(self.y[i-1], self.t[i-1])
			elif self.type == MethodsType.EULER_IMPROVED:
				v = self.calculateByImprovedEuler(self.y[i-1], self.t[i-1])

			self.t.append(v[0])
			self.y.append(v[1])
	
	def calculateByEuler(self, previousY, previousT):
		nextT = previousT + self.stepsSize
		nextY = previousY + self.stepsSize * self.evaluateFunction(previousY, previousT)
		return (nextT, nextY)

	def calculateByInverseEuler(self, previousY, previousT):
		nextT = previousT + self.stepsSize
		predictionNextY = self.calculateByEuler(previousY, previousT)[1]
		nextY = previousY + self.stepsSize * self.evaluateFunction(predictionNextY, nextT)
		return (nextT, nextY)
		
	def calculateByImprovedEuler(self, previousY, previousT):
		nextT = previousT + self.stepsSize
		predictionNextY = self.calculateByEuler(previousY, previousT)[1]
		nextY = previousY + self.stepsSize * (self.evaluateFunction(previousY, previousT) + self.evaluateFunction(predictionNextY, nextT))/2
		return (nextT, nextY)