import sys
from enums.methodstype import MethodsType
from models.method import Method

class RungeKutta(Method):

	def calculate(self):
		for i in range(1, self.steps + 1):
			v = self.calculateByRungeKutta(self.y[i-1], self.t[i-1])

			self.t.append(v[0])
			self.y.append(v[1])

	def calculateByRungeKutta(self, previousY, previousT):
		nextT = previousT + self.stepsSize
		k1 = self.evaluateFunction(previousY, previousT)
		k2 = self.evaluateFunction(previousY + (self.stepsSize*k1)/2, previousT + self.stepsSize/2)
		k3 = self.evaluateFunction(previousY + (self.stepsSize*k2)/2, previousT + self.stepsSize/2)
		k4 = self.evaluateFunction(previousY + (self.stepsSize*k3), previousT + self.stepsSize)
		nextY = previousY + self.stepsSize * (k1 + 2*k2 + 2*k3 + k4)/6
		return (nextT, nextY)