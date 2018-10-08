import sys
from models.enums.methodstype import MethodsType
from models.methods.method import Method

class RungeKutta(Method):

	def calculate(self):
		for i in range(1, self.steps + 1):
			v = self.calculateByRungeKutta(self.y[i-1], self.t[i-1])
			print(v)
			self.t.append(v[0])
			self.y.append(v[1])

	def calculateByRungeKutta(self, previousY, previousT):
		nextT = previousT + self.stepsSize
		k1 = float(self.function.subs([("y", previousY), ("t", previousT)]))
		k2 = float(self.function.subs([("y", previousY + (self.stepsSize*k1)/2), ("t", previousT + self.stepsSize/2)]))
		k3 = float(self.function.subs([("y", previousY + (self.stepsSize*k2)/2), ("t", previousT + self.stepsSize/2)]))
		k4 = float(self.function.subs([("y", previousY + (self.stepsSize*k3)), ("t", previousT + self.stepsSize)]))
		nextY = previousY + self.stepsSize * (k1 + 2*k2 + 2*k3 + k4)/6
		return (nextT, nextY)