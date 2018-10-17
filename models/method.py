import sys
from sympy import sympify
from enums.methodstype import MethodsType

class Method:

	def __init__(self, type, y, t, stepsSize, steps, function):
		self.type = type
		self.y = y
		self.t = t
		self.stepsSize = stepsSize
		self.steps = steps
		self.function = sympify(function)

	def evaluateFunction(self, forY, forT):
		return float(self.function.subs([("y", forY), ("t", forT)]))